from arg_parser.arg_parser import parse_arguments
from src.client import HamletReciter
from src.server import Server


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


if __name__ == "__main__":
    args = parse_arguments()
    if args.type == "client":
        run_client()
    if args.type == "server":
        run_server()
