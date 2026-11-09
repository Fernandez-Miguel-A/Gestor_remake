from PySide6.QtCore import QObject, QTimeLine, QPointF, Property, QSizeF
from PySide6.QtGui import QColor, QPainter, QPixmap
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsTextItem


class ImageItem(QGraphicsPixmapItem):
    def __init__(self, record_id: int, pixmap) -> None:
        super().__init__(pixmap)
        self._source_pixmap = pixmap
        self._is_selected = False
        self.m = None
        #self.pixmap_item = QGraphicsPixmapItem(pixmap)#, parent=self
        self.text_item = None
        self.record_id = record_id
        self.z = 0.0
        self.setAcceptHoverEvents(True)
        self.setTransformOriginPoint(self.boundingRect().center())

        self.time_line = QTimeLine(150)
        self.time_line.setFrameRange(0, 150)
        self.time_line.frameChanged.connect(self.set_frame)
        self.time_line.finished.connect(self.update_item_position)
        
    def set_model(self, data):
        if data is None:
            return
        self.m = data
        self.set_text(data)
        self.setGID(data[0])
        print("\n\n\n set_model::", data[0], self.getGID(), self.getGID() == data[0])

    def model(self):
        return self.m

    def set_image_pixmap(self, pixmap: QPixmap) -> None:
        self._source_pixmap = pixmap
        self.set_selected(self._is_selected)

    def set_selected(self, selected: bool) -> None:
        self._is_selected = selected
        if not selected or self._source_pixmap.isNull():
            self.setPixmap(self._source_pixmap)
            return

        tinted_pixmap = self._source_pixmap.copy()
        painter = QPainter(tinted_pixmap)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
        painter.fillRect(tinted_pixmap.rect(), QColor(0, 120, 215, 100))
        painter.end()
        self.setPixmap(tinted_pixmap)

    def getGIndex(self) -> int:
        return self.data(1)

    def setGIndex(self, i: int) -> None:
        self.setData(1, i)


    def setGID(self, i: int) -> None:
        print("setGID")
        self.setData(0, i)

    def getGID(self) -> int:
        return self.data(0)

#    def getGPos(self) -> QPointF:
#        return QPointF(self.data(1)//4, self.data(1)%4)

    def set_text(self, data): ## nuevo texto
        if self.text_item:
            print("self.text_item: ", self.text_item)
            self.scene().removeItem(self.text_item)
        text = f":{data[0]}: {data[1]}\n{data[3]}"
        self.text_item = QGraphicsTextItem(str(text), self)
        self.text_item.setDefaultTextColor(QColor("#d7d6d5"))
        #self.text_item.setPos(self.boundingRect().center() - self.text_item.boundingRect().center())
        self.text_item.setPos(self.boundingRect().topLeft()+
                         QPointF((120 - self.text_item.boundingRect().width()) / 2, 120.0))


    def hoverEnterEvent(self, event) -> None:
        self.time_line.setDirection(QTimeLine.Direction.Forward)
        if self.z != 1.0:
            self.z = 1.0
            self.update_item_position()
        if self.time_line.state() == QTimeLine.State.NotRunning:
            self.time_line.start()
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event) -> None:
        self.time_line.setDirection(QTimeLine.Direction.Backward)
        self.z = 0.0
        if self.time_line.state() == QTimeLine.State.NotRunning:
            self.time_line.start()
        super().hoverLeaveEvent(event)

    def set_frame(self, frame: int) -> None:
        self.setScale(1.0 + frame / 300.0)

    def update_item_position(self) -> None:
        self.setZValue(self.z)
