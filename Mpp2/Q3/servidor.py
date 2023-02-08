from operator import truediv
import socket
from time import sleep
from unicodedata import name

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('localhost', 60200))

namefile = server.recvfrom(4096)

if namefile[0] == bytes("comece", 'utf-8'):
    arquivo = open("teste.zip", 'rb')
    for i in arquivo:
        server.sendto(i, namefile[1])

    print("Enviado")
    sleep(5)
    server.sendto(bytes("terminei", 'utf-8'), namefile[1])

server.close()
server.close()