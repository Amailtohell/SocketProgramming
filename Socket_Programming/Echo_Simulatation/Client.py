import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 1222

s.connect(('localhost', port))
while True:
    user_input = str(input())
    if not user_input:
        break
    s.sendall(user_input.encode())
    data = s.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
