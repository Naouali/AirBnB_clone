#!/usr/bin/python3
"""
write class filestorage
"""

import json

class FileStorage:
    """ private class attributes """
    __file_path = "file.json"
    __objects = {}

    """ public instance methods """

    def all(self):
        """ return filestorage.object """
        return FileStorage.__objects

    def new(self, obj):
        """ add obj in __object with key """
        new = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[new] = obj

    def save(self):
        """ serializes __objects to the JSON file """

    def reload(self):
        """ deserializes the JSON file to __objects """
