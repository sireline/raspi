import socket

HOST = '192.168.0.200'
PORT = 24581
try:
    with socket.socket() as server:
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Server: {HOST} , Listen Port: {PORT}")

        while True:
            conn, addr = server.accept()
            print(f"Connection: {addr}({conn}) acceepted.")
            with conn:
                while True:
                    data = conn.recv(1024)
                    print(data)
                    if not data:
                        break
                    print(f"IP address: {addr} => {data}")
                    conn.sendall(b"Received: " + data)
            print(f"Connection: {addr}({conn}) closed.")
except KeyboardInterrupt:
    print("Server Closed.")
