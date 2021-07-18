# pylint: disable=too-few-public-methods
from os import path
import yaml


class SettingsHandler:
    handler = None
    current_directory = path.dirname(path.realpath(__file__))
    file_path = path.normpath(path.join(current_directory, "settings.yaml"))
    with open(file_path, "r") as f:
        handler = yaml.safe_load(f)
