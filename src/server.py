import logging
import socket
from config.config_handler import SettingsHandler

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(message)s")


class Server:
    # operating on IPv4 addressing scheme
    host_ip = SettingsHandler().handler["server"]["server_ip"]
    server_port = int(SettingsHandler().handler["server"]["port"])

    def __init__(self):
        self.server_socket = self.setup_server()

    def setup_server(self):
        # Create a stream based socket(i.e, a TCP socket)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host_ip, self.server_port))
        server_socket.listen()

        return server_socket

    def listen(self):
        (clientConnected, clientAddress) = self.server_socket.accept()

        data = clientConnected.recv(1024)

        # Send some data back to the client
        clientConnected.send("received".encode())

        logging.info(data.decode())
