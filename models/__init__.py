#!/usr/bin/python3
"""Create a unique FileStorage instance for the app."""


from models.engine.file_storage import FileStorage as storage


storage.reload()
