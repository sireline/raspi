import socket

HOST = '192.168.0.200'
PORT = 24581

with socket.socket() as client:
    client.connect((HOST, PORT))

    try:
        while True:
            cmd = input().encode()
            client.sendall(cmd)
            res = client.recv(1024)
            print(repr(res))
    except EOFError:
        print('Client Closed.')
