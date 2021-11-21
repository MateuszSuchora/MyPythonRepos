import socket


def server():
    proto = socket.getprotobyname('tcp')  # [1]
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto)

    serv.bind(("192.168.2.120", 8080))  # [2]
    serv.listen(1)  # [3]
    return serv


serv = server()
print("one")
while True:
    conn = serv.accept()  # [4]
    while 1:
        message = conn.recv(64)  # [5]
        if message:
            conn.send('Hi, I am a server, I received: ' + message)
            print("three")
        else:
            break
    conn.close()