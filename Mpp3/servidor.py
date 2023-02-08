import threading
import socket

def tratandoMensagens(Clientes, cliente):
    while True:
        try:
        
            msg = cliente.recv(2048).decode('utf-8')
            if (msg == 'Online'):
                msg = cliente.recv(2048).decode('utf-8') #dados

                #Colocando os dados numa lista para enviar para cada cliente depois
                lista_msg.append(msg)
                if (len(Clientes) == 2): # só enviamos se tiver mais de um cliente
                    Clientes[0].send(lista_msg[1].encode('utf-8'))
                    Clientes[1].send(lista_msg[0].encode('utf-8'))
        except:
            break


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Clientes = []
lista_msg = []

try:
    servidor.bind(('localhost', 55555))
    servidor.listen()
    print('Conexão estabelecida!')

    while True:
        #Aceitando conexão com cliente e colocando ele numa lista
        cliente, addr = servidor.accept()
        Clientes.append(cliente)

        thread = threading.Thread(target=tratandoMensagens, args=[Clientes, cliente])
        thread.start()

except:
    print('Falha ao conectar!')
    exit()