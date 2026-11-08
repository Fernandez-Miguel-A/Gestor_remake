import sqlite3
from pathlib import Path

from PySide6.QtCore import QPoint, QPointF, Qt, Signal, QSizeF
from PySide6.QtGui import QColor, QLinearGradient, QPixmap
from PySide6.QtWidgets import (
    QGraphicsScene,
    QGraphicsTextItem,
    QGraphicsView,
    QMessageBox,
)

from .imageitem import ImageItem
from .informationwindow import InformationWindow


IMAGE_DIRECTORY = Path(__file__).resolve().parent / "../images"


class View(QGraphicsView):
    GItemPressed = Signal(ImageItem)
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.database = None
        self._index = 0
        self.scene = QGraphicsScene(self)
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
        print(f"\n\n data: {data}")
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
            image.setData(0, index)
            image.setData(1, index)
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
        image.setData(0, data[0])
        image.setData(1, self._index)
        image.setPos(p)
        image.set_model(data)
        self.scene.addItem(image)
        self.image_items[record_id] = image

        self._index += 1

    def UpdateGItem(self, datos) -> None:
        print("UpdateGItem:", len(self.scene.items()), datos)
        r = datos[0]
        for i in self.scene.items():
            #print("\n\nGItem:", i, i.data(0), r)
            if i.data(0) == r:
                i.set_model(datos)
                return

    def removeGItem(self, datos) -> None:
        r = datos[0]
        index2 = None
        for item in self.scene.items():
            if item.data(0) == r:
                index2 = item.data(1)
                self.scene.removeItem(item.text_item)
                self.scene.removeItem(item)
                self._index -= 1
                break  

        for item in self.scene.items():
            #print("item.data: ", item.data(0), item.data(1), self._index, index2, item)
            if item.data(1) and index2 and item.data(1) > index2: ## el item puede ser un 'QGraphicsTextItem'
                new_index = item.data(1) - 1
                p = self.getPosGItem(new_index)

                item.setPos(p)
                item.setData(1, new_index)


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
    def resizeEvent(self, event):
        self.scene.setSceneRect(0, 0, event.size().width(), event.size().height()*3)
        super().resizeEvent(event)

    def mouseReleaseEvent(self, event) -> None:
        item = self.itemAt(event.position().toPoint())
        print("\n\n\n mouseReleaseEvent: ", item)
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
        image.setPixmap(pixmap)
        image.setTransformOriginPoint(image.boundingRect().center())
        image.setScale(1.0)
