import sqlite3

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QGraphicsView,
    QLabel,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)


class InformationWindow(QDialog):
    imageChanged = Signal(int, str)

    def __init__(
        self, record_id: int, database: sqlite3.Connection, parent: QGraphicsView
    ) -> None:
        super().__init__(parent)
        self.record_id = record_id
        self.database = database

        row = database.execute(
            "SELECT itemtype, imagefile, description FROM items WHERE id = ?",
            (record_id,),
        ).fetchone()
        if row is None:
            raise LookupError(f"No item exists with id {record_id}")

        item_label = QLabel("Item:")
        description_label = QLabel("Description:")
        image_file_label = QLabel("Image file:")
        self.item_text = QLabel(row[0])
        self.description_editor = QTextEdit()
        self.image_file_editor = QComboBox()

        image_rows = database.execute(
            "SELECT itemid, file FROM images ORDER BY itemid"
        ).fetchall()
        for image_id, filename in image_rows:
            self.image_file_editor.addItem(filename, image_id)

        self.image_file_editor.setCurrentIndex(
            self.image_file_editor.findData(row[1])
        )
        self.description_editor.setPlainText(row[2])
        self.displayed_image = self.image_file_editor.currentText()

        self.close_button = QPushButton("&Close")
        self.revert_button = QPushButton("&Revert")
        self.submit_button = QPushButton("&Submit")
        self.close_button.setDefault(True)
        self.close_button.clicked.connect(self.close)
        self.revert_button.clicked.connect(self.revert)
        self.submit_button.clicked.connect(self.submit)

        button_box = QDialogButtonBox(self)
        button_box.addButton(
            self.submit_button, QDialogButtonBox.ButtonRole.AcceptRole
        )
        button_box.addButton(
            self.revert_button, QDialogButtonBox.ButtonRole.ResetRole
        )
        button_box.addButton(
            self.close_button, QDialogButtonBox.ButtonRole.RejectRole
        )

        self.description_editor.textChanged.connect(
            lambda: self.enable_buttons(True)
        )
        self.image_file_editor.currentIndexChanged.connect(
            lambda _index: self.enable_buttons(True)
        )

        form_layout = QFormLayout()
        form_layout.addRow(item_label, self.item_text)
        form_layout.addRow(image_file_label, self.image_file_editor)
        form_layout.addRow(description_label, self.description_editor)
        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(button_box)
        self.setLayout(layout)

        self.setWindowFlags(Qt.WindowType.Window)
        self.enable_buttons(False)
        self.setWindowTitle(self.item_text.text())

    def id(self) -> int:
        return self.record_id

    def revert(self) -> None:
        row = self.database.execute(
            "SELECT imagefile, description FROM items WHERE id = ?",
            (self.record_id,),
        ).fetchone()
        if row is None:
            raise LookupError(f"No item exists with id {self.record_id}")
        self.image_file_editor.setCurrentIndex(
            self.image_file_editor.findData(row[0])
        )
        self.description_editor.setPlainText(row[1])
        self.enable_buttons(False)

    def submit(self) -> None:
        image_id = self.image_file_editor.currentData()
        new_image = self.image_file_editor.currentText()
        try:
            self.database.execute(
                "UPDATE items SET imagefile = ?, description = ? WHERE id = ?",
                (image_id, self.description_editor.toPlainText(), self.record_id),
            )
            self.database.commit()
        except sqlite3.Error as error:
            self.database.rollback()
            QMessageBox.critical(self, "Database error", str(error))
            return

        if self.displayed_image != new_image:
            self.displayed_image = new_image
            self.imageChanged.emit(self.record_id, new_image)
        self.enable_buttons(False)

    def enable_buttons(self, enabled: bool) -> None:
        self.revert_button.setEnabled(enabled)
        self.submit_button.setEnabled(enabled)
