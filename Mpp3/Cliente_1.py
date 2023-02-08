import threading
import socket
from datetime import datetime


def main():

    Cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Cliente.bind(('localhost', 5555))
    try:
        Cliente.connect(('localhost', 55555))
    except:
        return print('Falha ao conectar-se ao servidor')

    username = input('Digite seu nome de usuário')
    print(f'{username} conectado')

    #Enviando os dados do user
    status = 'Online'
    Cliente.send(status.encode('utf-8'))
    ip = Cliente.getsockname()[0]
    porta = Cliente.getsockname()[1]
    Cliente.send(f'{username} {ip} {porta}'.encode('utf-8'))

    #Pegando dados do outro par
    info_cliente = Cliente.recv(2048).decode('utf-8').split()

    #Fechando conexão para iniciar o p2p puro
    Cliente.close()
    #Criando um socket para o servidor do cliente atual e para o cliente do cliente atual
    sp2p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sp2p.bind((str(ip), int(porta)))
    cp2p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cp2p.bind((str(ip), 24242))

    #criação das threads para o envio e recebimento simultâneo de mensagens 
    thread1 = threading.Thread(target=receiveMessages, args=[sp2p, cp2p, username])
    thread2 = threading.Thread(target=sendMessages, args=[cp2p, info_cliente, username])

    #Iniciando as threads
    thread1.start()
    thread2.start()
    
#Recebendo mensagens com o socket do servidorP2P
def receiveMessages(server, cliente, user):
    server.listen()
    conn, addr = server.accept() #permitindo conexão
    while True:
        try:
            #pegando as mesagens
            msg = conn.recv(2048).decode('utf-8').split()
            msg_inicial = ''
            msg_final = ''            
            #Data pela biblioteca datetime
            date = datetime.now()
            date = date.strftime('%d-%m-%y %H:%Mh')

            if (len(msg) > 4):

                #Formatação de print
                for i in range(5):
                    msg_inicial += (str(msg[i]) + ' ')
                
                for i in range(6, len(msg)):
                    msg_final += (str(msg[i]) + ' ')

                print(f'{msg_inicial}\ recebido {date}): {msg_final}')
                #Enviando confirmação de mensagem
                cliente.send(f'{user} diz {str(msg[1])} recebida'.encode('utf-8'))
            else:
                #Recebendo confirmação de mensagem
                msg_final = ''
                for i in msg:
                    msg_final += (i + ' ')
                #Pritando a mensagem de confirmação
                print(msg_final)

        except:
            return


def sendMessages(s, info_cliente, user):
    contador = 0
    #Conectando ao outro cliente
    s.connect((str(info_cliente[1]), int(info_cliente[2])))

    while True:
        try:
            #Recebendo qual mensagem será enviada e formatando com horario e data
            msg = input()
            date = datetime.now()
            date = date.strftime('%d-%m-%y %H:%Mh')
            contador += 1
            s.send(f'{user} #{contador} (enviado {date} ): {msg}'.encode('utf-8'))

            #Printando a mensagem enviada
            print(f'{user} #{contador} (enviado {date}): {msg}')

        except:
            return

main()