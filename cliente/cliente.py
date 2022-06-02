import socket
import time
from time import sleep

print("INICIO")

msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

hostServer = input('Digite o IP do servidor: ')

#"192.168.56.1"

serverAddressPort   = (hostServer, 5555)

bufferSize          = 2000

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
# Send to server using created UDP socket

print('\n1 - Enviar um arquivo !')
print('dc - Desligar o cliente')
print('dcs - Desligar o cliente e o servidor\n')

while True:
    i = input('Digite uma mensagem ou um comando: ')

    if i == '1':
        #UDPClientSocket.sendto('Irá ser enviado um arquivo !', serverAddressPort)
        caminho_arquivo = input('Informe o caminho do arquivo que deseja enviar !\n')
        ini = time.time()
        UDPClientSocket.sendto("Enviou arquivo", serverAddressPort)
        fim = time.time()
        print('Envio levou %.2f segundos' % (fim - ini))
    elif i == 'dc':
        break
    else:
         UDPClientSocket.sendto(str.encode(i), serverAddressPort)

    if i == 'dcs':
        break
""" 
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0])

print(msg) """