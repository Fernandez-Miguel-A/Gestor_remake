import sqlite3

from PySide6.QtWidgets import QMessageBox


def create_connection() -> sqlite3.Connection | None:
    try:
        database = sqlite3.connect(":memory:")
        database.executescript(
            """
            CREATE TABLE person (
                id INTEGER PRIMARY KEY,
                firstname VARCHAR(20),
                lastname VARCHAR(20)
            );
            INSERT INTO person VALUES
                (101, 'Danny', 'Young'),
                (102, 'Christine', 'Holand'),
                (103, 'Lars', 'Gordon'),
                (104, 'Roberto', 'Robitaille'),
                (105, 'Maria', 'Papadopoulos'),
                (106, 'Danny', 'Young'),
                (107, 'Christine', 'Holand'),
                (108, 'Lars', 'Gordon'),
                (109, 'Roberto', 'Robitaille'),
                (110, 'Maria', 'Papadopoulos');

            CREATE TABLE items (
                id INTEGER PRIMARY KEY,
                imagefile INTEGER,
                itemtype VARCHAR(20),
                description VARCHAR(100)
            );
            INSERT INTO items VALUES
                (0, 0, 'Qt', 'Qt is a full development framework with tools designed to streamline the creation of stunning applications and amazing user interfaces for desktop, embedded and mobile platforms.'),
                (1, 1, 'Qt Quick', 'Qt Quick is a collection of techniques designed to help developers create intuitive, modern-looking, and fluid user interfaces using a CSS & JavaScript like language.'),
                (2, 2, 'Qt Creator', 'Qt Creator is a powerful cross-platform integrated development environment (IDE), including UI design tools and on-device debugging.'),
                (3, 3, 'Qt Project', 'The Qt Project governs the open source development of Qt, allowing anyone wanting to contribute to join the effort through a meritocratic structure of approvers and maintainers.'),
                (4, 0, 'Qt', 'Qt is a full development framework with tools designed to streamline the creation of stunning applications and amazing user interfaces for desktop, embedded and mobile platforms.'),
                (5, 1, 'Qt Quick', 'Qt Quick is a collection of techniques designed to help developers create intuitive, modern-looking, and fluid user interfaces using a CSS & JavaScript like language.'),
                (6, 2, 'Qt Creator', 'Qt Creator is a powerful cross-platform integrated development environment (IDE), including UI design tools and on-device debugging.'),
                (7, 3, 'Qt Project', 'The Qt Project governs the open source development of Qt, allowing anyone wanting to contribute to join the effort through a meritocratic structure of approvers and maintainers.');
;

            CREATE TABLE images (
                itemid INTEGER PRIMARY KEY,
                file VARCHAR(40)
            );
            INSERT INTO images VALUES
                (0, 'qt-logo.png'),
                (1, 'qt-logo.png'),
                (2, 'qt-quick.png'),
                (3, 'qt-creator.png'),
                (4, 'qt-project.png');
            """
        )
        return database
    except sqlite3.Error as error:
        QMessageBox.critical(
            None,
            "Cannot open database",
            f"Unable to establish a database connection: {error}",
        )
        return None
