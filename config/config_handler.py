# pylint: disable=too-few-public-methods
from configparser import ConfigParser
from os import path


class SettingsHandler:
    current_directory = path.dirname(path.realpath(__file__))
    file_path = path.normpath(path.join(current_directory, "settings.ini"))
    handler = ConfigParser()
    handler.read(file_path)
