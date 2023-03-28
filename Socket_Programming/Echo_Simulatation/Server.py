import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port: int = 1222

s.bind(('', port))

s.listen()

c, addr = s.accept()
print("Got Connection from", addr)

while True:
    data = c.recv(1024)
    if not data:
        break
    c.sendall(data)
c.close()


