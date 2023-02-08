from operator import truediv
import socket
from unicodedata import name

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 60200))
server.listen(1)

connection, address = server.accept()

namefile = connection.recv(2048).decode()

if namefile == "comece":
    arquivo = open("teste.zip", 'rb')
    for i in arquivo:
        connection.sendall(i)

    print("Enviado")
    connection.sendall(bytes("terminei", 'utf-8'))

server.close()
connection.close()