import socket
from config.config_handler import SettingsHandler


class HamletReciter:
    host_ip = SettingsHandler().handler["server"]["server_ip"]
    server_port = int(SettingsHandler().handler["server"]["port"])

    def recite(self, line):
        tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            tcp_client.connect((self.host_ip, self.server_port))
            tcp_client.sendall(line.encode())

            # Read data from the TCP server and close the connection
            received = tcp_client.recv(1024)
        finally:
            tcp_client.close()
