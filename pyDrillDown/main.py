import sys

from PySide6.QtWidgets import QApplication, QMessageBox

from connection import create_connection
from libs.view import GView


def main() -> int:
    app = QApplication(sys.argv)
    database = create_connection()
    if database is None:
        return 1

    try:
        view = GView()
        view.set_database(database)
        view.add_DefaultItems()
    except FileNotFoundError as error:
        QMessageBox.critical(None, "Image error", str(error))
        database.close()
        return 1

    view.show()
    result = app.exec()
    database.close()
    return result


if __name__ == "__main__":
    sys.exit(main())
