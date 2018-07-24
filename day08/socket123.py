import socket

host = ''
port = 22345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
while True:
    cli_sock, cli_addr = s.accept()
    print('Client connect from:', cli_addr)
    while True:
        data=cli_sock.recv(1024)
        if data.strip() == b'end':
            break
        print(data)
        sendata=input('>')+'\r\n'
        cli_sock.send(sendata)
    cli_sock.close()
s.close()
