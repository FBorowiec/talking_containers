import socket
from config.config_handler import SettingsHandler


class HamletReciter:
    host_ip = SettingsHandler().handler["server"]["server_ip"]
    server_port = int(SettingsHandler().handler["server"]["port"])

    def __init__(self):
        # Initialize a TCP client socket using SOCK_STREAM
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def recite(self, line):
        try:
            # Establish connection to TCP server and exchange data
            self.tcp_client.connect((self.host_ip, self.server_port))
            self.tcp_client.sendall(line.encode())

            # Read data from the TCP server and close the connection
            received = self.tcp_client.recv(1024)
        finally:
            self.tcp_client.close()
