from http import server
import socket
from unicodedata import name

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(bytes("comece", "utf-8"), ('localhost', 60200))
arquivo = []    

while True:
    file = client.recvfrom(4096)

    if file[0] == bytes('terminei', 'utf-8'):
        break
    arquivo.append(file[0])

salvar = open('questao3.rar', 'wb')

for byte in arquivo:
    salvar.write(byte)

salvar.close()
client.close()