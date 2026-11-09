import sqlite3
from pathlib import Path

from PySide6.QtCore import QPoint, QPointF, Qt, Signal, QSizeF
from PySide6.QtGui import QColor, QLinearGradient, QPixmap, QBrush, QPen
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
    QMessageBox,
    QGraphicsRectItem
)

from .imageitem import ImageItem
from .informationwindow import InformationWindow


IMAGE_DIRECTORY = Path(__file__).resolve().parent / "../images"

class RuberBand(QGraphicsRectItem):
    def __init__(self, parent= None):
        super().__init__(parent)
    def paint(self, painter, opt, w=None):
        painter.save()
        painter.setOpacity(0.6)     ## Rectangulo con Opacidad al %60.
        painter.setPen(QPen(QColor(0, 120, 215)))
        painter.setBrush(QBrush(QColor(170, 204, 238)))
        painter.drawRoundedRect(self.rect(), 5, 5)
        painter.restore()


class GView(QGraphicsView):
    GItemPressed = Signal(ImageItem)
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.database = None
        self._index = 0
        self._rect = RuberBand()
        self._rect.setRect(0, 0, 0, 0)
        self._rect.setAcceptedMouseButtons(Qt.MouseButton.NoButton)
        self._rect.setZValue(10)
        self._drag_start = None
        self._selectedItems: list[ImageItem] = []
        self.scene = QGraphicsScene(self)
        self.scene.addItem(self._rect)
        self.scene.setSceneRect(0, 0, 465*2, 365*2)
        self.setScene(self.scene)
        self.information_windows: list[InformationWindow] = []
        self.image_items: dict[int, ImageItem] = {}

        #self.setFixedSize(470, 370)

        gradient = QLinearGradient(QPointF(0, 0), QPointF(0, 370))
        gradient.setColorAt(0, QColor("#868482"))
        gradient.setColorAt(1, QColor("#5d5b59"))
        self.setBackgroundBrush(gradient)
        
    def set_database(self, database: sqlite3.Connection) -> None:
        self.database = database

    def find_Image_fromCode(self, cod_clie: int):
        sql = f"SELECT file FROM images WHERE itemid = {cod_clie}"
        data = self.database.execute(sql)
        one = data.fetchone()
        if not one:
            d = self.database.execute("SELECT file FROM images WHERE itemid = 0")
            one = d.fetchone()
        return one

    def getPosGItem(self, index) -> QPointF:
        image_offset = 150
        left_margin = 70
        top_margin = 40

        column_offset = (index % 4) * 37
        x = (index % 4) * image_offset + left_margin + column_offset
        y = (index // 4) * image_offset #+ top_margin
        return QPointF(x, y)

#    def getGPOS(self):
#        self.getPosGItem(index)

    def add_items(self) -> None:
        rows = self.database.execute(
            """
            SELECT items.id, images.file, items.itemtype
            FROM items
            JOIN images ON images.itemid = items.imagefile
            ORDER BY items.id
            """
        ).fetchall()

        for index, (record_id, filename, item_type) in enumerate(rows):
            print(f"Adding item {record_id}: {filename} ({item_type}), index: {index}")
            p = self.getPosGItem(index)
            pixmap = self.load_image(filename)
            image = ImageItem(record_id, pixmap)
            image.setGID(index)
            image.setGIndex(index)
            image.setPos(p)
            image.set_model(None)
            self.scene.addItem(image)
            self.image_items[record_id] = image

            label = QGraphicsTextItem(item_type)
            label.setDefaultTextColor(QColor("#d7d6d5"))
            label.setPos(
                p
                + QPointF((120 - label.boundingRect().width()) / 2, 120.0)
            )
            self.scene.addItem(label)
        self._index = index + 1

    def addGItem(self, data) -> None:
        print("addGItem:", data, data[2])
        row = self.database.execute(
            f"""
            SELECT items.id, images.file
            FROM items
            JOIN images ON images.itemid = items.imagefile
            WHERE items.imagefile == {data[2]}
            ORDER BY items.id
            """
        ).fetchone()
        print("_addGItem", row)
        #if not row: ## cod_clie: (5) o otro
        #    return

        if not row:
            defaultImage = self.database.execute(
                """
                SELECT items.id, images.file
                FROM items
                JOIN images ON images.itemid = items.imagefile
                WHERE items.imagefile == 0
                ORDER BY items.id
                """
            ).fetchone() ## cargo la Imagen por defecto, la imagen 'Qt-def'
            record_id, filename = data[0], defaultImage[1] ## 'id', 'pixmap vacio'
        else:
            record_id, filename = data[0], row[1]

        #for index, (record_id, filename, item_type) in enumerate(rows):
        print(f"__addGItem() {record_id}, {filename} index: {self._index}")
        p = self.getPosGItem(self._index)
        pixmap = self.load_image(filename)
        image = ImageItem(record_id, pixmap)
        #image.setGID(data[0])       ## 'id'
        image.setGIndex(self._index)   ## 'index'
        image.setPos(p)
        image.set_model(data)
        self.scene.addItem(image)
        self.image_items[record_id] = image

        self._index += 1

    def UpdateGItem(self, datos) -> None:
        print("UpdateGItem:", datos)
        r = datos[0]
        for i in self.scene.items():
            #print("\n\nGItem:", i, i.getGID(), r)
            if isinstance(i, ImageItem) and i.getGID() == r:
                i.set_model(datos)
                return

    def removeGItem(self, datos) -> None:
        r = datos[0]
        index2 = None
        for item in self.scene.items():
            if isinstance(item, ImageItem) and item.getGID() == r:
                index2 = item.getGIndex()
                self.scene.removeItem(item.text_item)
                self.scene.removeItem(item)
                self._index -= 1
                break  

        for item in self.scene.items():
            #print("item.data: ", item.getGID(), item.getGIndex(), self._index, index2, item)
            if isinstance(item, ImageItem) and index2 and item.getGIndex() > index2: ## el item puede ser un 'QGraphicsTextItem'
                new_index = item.getGIndex() - 1
                p = self.getPosGItem(new_index)

                item.setPos(p)
                item.setGIndex(new_index)


    def load_image(self, filename: str) -> QPixmap:
        if filename == "":
            return QPixmap()
        image_path = IMAGE_DIRECTORY / filename
        pixmap = QPixmap(str(image_path))
        if pixmap.isNull():
            raise FileNotFoundError(f"Unable to load image: {image_path}")
        return pixmap.scaled(
            120,
            120,
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )

    def PrintSelectedGItems(self):
        print("PrintSelectedGItems:")
        [print(f"\ndatos: {item.getGID()}, {item.model()}\n") for item in self._selectedItems]

    def selectedGItems(self) -> list:
        return self._selectedItems

    def _update_selected_items(self) -> None:
        selection_rect = self._rect.sceneBoundingRect()
        self._selectedItems = [
            item
            for item in self.scene.items(
                selection_rect,
                Qt.ItemSelectionMode.IntersectsItemShape,
            )
            if isinstance(item, ImageItem)
        ]
        selected_items = set(self._selectedItems)
        for image in self.image_items.values():
            image.set_selected(image in selected_items)
    
    def resizeEvent(self, event):
        self.scene.setSceneRect(0, 0, event.size().width(), event.size().height()*3)
        super().resizeEvent(event)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self._drag_start = self.mapToScene(event.position().toPoint())
            self._rect.setPos(self._drag_start)
            self._rect.setRect(0, 0, 1, 1)
            self._update_selected_items()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event) -> None:
        if self._drag_start is not None and event.buttons() & Qt.MouseButton.LeftButton:
            current = self.mapToScene(event.position().toPoint())
            left = min(self._drag_start.x(), current.x())
            top = min(self._drag_start.y(), current.y())
            self._rect.setRect(
                0,
                0,
                abs(current.x() - self._drag_start.x()),
                abs(current.y() - self._drag_start.y()),
            )
            self._rect.setPos(left, top)
            self._update_selected_items()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self._update_selected_items()
            ## self.PrintSelectedGItems()
        self._drag_start = None
        item = next(
            (
                item
                for item in self.items(event.position().toPoint())
                if item is not self._rect
            ),
            None,
        )
        self._rect.setRect(0, 0, 1, 1)
        if isinstance(item, ImageItem):
            model = item.model()
            if model is not None:
                self.GItemPressed.emit(item)
                super().mouseReleaseEvent(event)
                return ## GItem creados con addGItem()
            self.show_information(item)
        super().mouseReleaseEvent(event)

    def show_information(self, image: ImageItem) -> None:
        window = next(
            (
                window
                for window in self.information_windows
                if window.id() == image.record_id
            ),
            None,
        )
        if window is None:
            window = InformationWindow(image.record_id, self.database, self)
            window.imageChanged.connect(self.update_image)
            window.move(self.pos() + QPoint(20, 40))
            self.information_windows.append(window)

        if window.isVisible():
            window.raise_()
            window.activateWindow()
        else:
            window.show()

    def update_image(self, record_id: int, filename: str) -> None:
        image = self.image_items.get(record_id)
        if image is None:
            return
        try:
            pixmap = self.load_image(filename)
        except FileNotFoundError as error:
            QMessageBox.critical(self, "Image error", str(error))
            return
        image.set_image_pixmap(pixmap)
        image.setTransformOriginPoint(image.boundingRect().center())
        image.setScale(1.0)
