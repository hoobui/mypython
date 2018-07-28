import socket
from time import strftime
import os


class TcpTimeServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self, c_socket):
        while True:
            data = c_socket.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode('utf8'))
            c_socket.send(data.encode('utf8'))
        c_socket.close()

    def mainloop(self):
        while True:
            cli_socket, cli_addr = self.serv.accept()
            pid = os.fork()
            if pid:
                cli_socket.close()
            else:
                self.serv.close()
                self.chat(cli_socket)
                exit()
        self.serv.close()


if __name__ == '__main__':
    s = TcpTimeServer()
    s.mainloop()
