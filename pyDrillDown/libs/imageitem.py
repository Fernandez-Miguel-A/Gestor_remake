from PySide6.QtCore import QObject, QTimeLine
from PySide6.QtWidgets import QGraphicsPixmapItem


class ImageItem(QObject, QGraphicsPixmapItem):
    def __init__(self, record_id: int, pixmap) -> None:
        QObject.__init__(self)
        QGraphicsPixmapItem.__init__(self, pixmap)
        self.record_id = record_id
        self.z = 0.0
        self.setAcceptHoverEvents(True)
        self.setTransformOriginPoint(self.boundingRect().center())

        self.time_line = QTimeLine(150, self)
        self.time_line.setFrameRange(0, 150)
        self.time_line.frameChanged.connect(self.set_frame)
        self.time_line.finished.connect(self.update_item_position)

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
