import json
import socket
from config.config_handler import SettingsHandler


class HamletReciter:
    host_ip = SettingsHandler().handler["server"]["server_ip"]
    server_port = SettingsHandler().handler["server"]["port"]

    def __init__(self):
        # Initialize a TCP client socket using SOCK_STREAM
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def recite(self, line):
        try:
            data = json.dumps({"data": line})
            # Establish connection to TCP server and exchange data
            self.tcp_client.connect((self.host_ip, self.server_port))
            self.tcp_client.sendall(data.encode())

            # Read data from the TCP server and close the connection
            received = self.tcp_client.recv(1024)
            print("received: ", received)
        finally:
            self.tcp_client.close()
