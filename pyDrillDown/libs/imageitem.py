from PySide6.QtCore import QObject, QTimeLine, QPointF, Property
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsTextItem


class ImageItem(QGraphicsPixmapItem):
    def __init__(self, record_id: int, pixmap) -> None:
        super().__init__(pixmap)
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

    def model(self):
        return self.m

    def setData__(self, i, index: int) -> None:
        if self.m:
            self.m[0] = index
        else:
            self.m = [index]
        super().setData(0, index)

    def set_text(self, data): ## nuevo texto
        if self.text_item:
            print("self.text_item: ", self.text_item)
            self.scene().removeItem(self.text_item)
        text = data[1] + "\n" + data[3]
        self.text_item = QGraphicsTextItem(str(text), self)
        self.text_item.setDefaultTextColor(QColor("#d7d6d5"))
        #self.text_item.setPos(self.boundingRect().center() - self.text_item.boundingRect().center())
        print("set_text: ", self.boundingRect().topLeft())
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
