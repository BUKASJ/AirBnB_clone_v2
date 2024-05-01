#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage based
on environment variable"""

from os importgetenv

if __name__ == "__main__":
    storage_type = getenv("HBNB_TYPE_STORAGE", "fs")

    if storage_type == "db":
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
    else:
        from models.engine.file_storage import FileStorage
        storage = FileStorage()

    storage.reload()
