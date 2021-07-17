from time import sleep
from arg_parser.arg_parser import parse_arguments
from config.config_handler import SettingsHandler
from src.client import HamletReciter
from src.server import Server

SPEED = int(SettingsHandler().handler["reader"]["speed"])
READ_SPEED = 60.0 / SPEED


def run_server():
    server = Server()
    while True:
        server.listen()


def run_client():
    hr = HamletReciter()
    with open("hamlet.txt", "r") as f:
        hamlet_lines = f.readlines()

    for line in hamlet_lines:
        hr.recite(line)

        words = len(line.split())
        sleep(READ_SPEED * words)


if __name__ == "__main__":
    args = parse_arguments()
    if args.type == "client":
        run_client()
    elif args.type == "server":
        run_server()
    else:
        raise ValueError("Wrong argument provided!")
