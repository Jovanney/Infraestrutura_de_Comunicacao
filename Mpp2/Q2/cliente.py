from http import server
import socket
from unicodedata import name

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind(('0.0.0.0', 50000))
client.connect(('localhost', 60200))
print('conectado!\n')


client.sendall(bytes("comece", "utf-8"))
arquivo = []    

while True:
    file = client.recv(2048)

    if file == bytes('terminei', 'utf-8'):
        break
    arquivo.append(file)

salvar = open('Saida.rar', 'wb')

for byte in arquivo:
    salvar.write(byte)

salvar.close()
client.close()
