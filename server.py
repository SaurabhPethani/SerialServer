import socket

soc = socket.socket()

soc.bind(('localhost', 3690))

soc.listen(5)

while True:
    print("Waiting for Client to connect....")
    client,addr = soc.accept()

    print("Client connected with address ",addr)

    msg = ''
    while msg != 'q':
        msg = client.recv(1024).decode('utf-8')
        print('client -> ',msg)
        client.send(msg.upper().encode('utf-8'))

soc.close()