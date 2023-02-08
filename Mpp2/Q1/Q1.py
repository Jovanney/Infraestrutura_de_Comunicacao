from ipaddress import ip_address
import ipaddress
import sys
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipAddress = socket.gethostbyname('smtp.cin.ufpe.br')

portas = [21, 22, 23, 25, 43, 53, 80, 81, 110, 443, 902, 1214, 1434, 1863, 5000, 5500, 5800]
nomes = ['FTP', 'SSH', 'Telnet', 'SMTP', 'WHOIS', 'DNS', 'HTTP', 'Skype', 'POP3', 'HTTPS', 'VMWARE Server Console', 'Kazaa', 
'Microsoft SQL Monitor', 'Windows Live Messenger', 'UPnP', 'VNC remote desktop protocol', 'VNC remote desktop protocol (over HTTP)']

for i in range(len(portas)):
    if s.connect_ex((ipAddress, portas[i])) == 0:
        print(f"Porta {portas[i]} - {portas[i]} aberta!")
    else:
        print(f"Falha ao acessar a porta {portas[i]} - {nomes[i]}!")

s.close()
