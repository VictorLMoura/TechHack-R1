import socket
import subprocess
import sys
from datetime import datetime
import threading

def TCP_connect(ip, port_number, delay):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        return True
    except:
        return False

#Estabelece uma comunicacao para cada uma das portas
def port_scan(hostIP, porta_in, porta_fim, timeout):
    for port in range(porta_in, porta_fim):
        res = TCP_connect(hostIP, port, timeout)
        if(res == True):
            print("Aberta: ", port)
        else:
            print("Fechada: ", port)

    print("Servicos: ")
    protocolname = "tcp" 
    for port in range(1,1024):
        TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        TCPsock.settimeout(timeout)
        try:
            TCPsock.connect((hostIP, port))
            print ("Port(Tcp): %s => service name: %s" %(port, socket.getservbyport(port, protocolname))) 
            print ("Port(Udp): %s => service name: %s" %(port, socket.getservbyport(port, 'udp')))
        except Exception as e:
            print("port", e)  
        

def network_scan(network, ip_in, ip_fim, port, timeout):
    last_ip_in = network.rfind(".")
    ip_in = int(ip_in[last_ip_in+1:])
    last_ip_fim = network.rfind(".")
    ip_fim = int(ip_fim[last_ip_fim+1:])
    for ip in range(ip_in, ip_fim):
        addr = net2 + str(ip)
        res = TCP_connect(addr, port, timeout)
        if(res == True):
            print("Aberta: ", addr)
        else:
            print("Fechada: ", addr)

print("-" * 60)
print("Modo de utilizacao:")
print("Tipos de scan suportados (digite o codigo a esquerda): ")
print("1 - scan de rede")
print("2 - scan de host")
print("-" * 60)

timeout = 0.5
tipo_scan = int(input("Selecao: "))
if(tipo_scan == 1):
    print("Agora em modo scan de rede...")
    network = str(input("Insira a rede a ser escaneada: "))
    net1 = network.split('.')
    a = '.'
    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    ip_in = str(input("Ip de inicio: "))
    ip_fim = str(input("Ip de fim: "))
    port = int(input("Porta para conexao: "))
    network_scan(network, ip_in, ip_fim, port, timeout)
    print("Fim")

elif(tipo_scan == 2):
    print("Agora em modo scan de host...")
    hostIP = str(input("Insira o IP do host: "))
    print ("A ser scanneado: ", hostIP)
    porta_in = int(input("Porta de inicio: "))
    porta_fim = int(input("Ate a porta: "))
    port_scan(hostIP, porta_in, porta_fim, timeout)
    print("Fim")

else:
    print("Selecao invalida!")