import socket
import os
import time

# 3 Inicializando client
print("Configurando cliente UDP\n")

hostServer = '192.168.56.1'

HOST = hostServer
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ADDRESS = (HOST, PORT)
sock.connect(ADDRESS)
sock.settimeout(70.0)

# 4 Enviando arquivos ao servidor
file_paths = os.listdir()
print("Enviando nomes dos arquivos...")
for file in file_paths:
    sock.sendall(file.encode())

sock.sendall("stop".encode())


# 7 Esperando resposta do servidor sobre qual arquivo enviar
print("Esperando resposta do servidor...")
msg = sock.recv(4)
index = int.from_bytes(msg, "little")

# 8 Abrindo arquivo para ser enviado

file = open(file_paths[index], "rb")
file_size = os.path.getsize(file_paths[index])  # Size in bits
pacote_em_kilobytes = 512
pacote_em_bytes = pacote_em_kilobytes * 8

# 9 Enviando o numero de pacotes ao servidor
numero_de_pacotes = (file_size // pacote_em_bytes) + 1
sock.sendall(numero_de_pacotes.to_bytes(4, "little"))

# 11 Enviando pacotes
delay = 0.004
tempo_estimado = numero_de_pacotes*(delay*1.2)

print(f"Enviando {numero_de_pacotes} pacotes ao servidor")
print(f"Tempo estimado: {round(tempo_estimado)} sec")


for i in range(numero_de_pacotes):
    packet = file.read(pacote_em_bytes)
    sock.sendall(packet)
    enviado = f"{int((i+1)*pacote_em_kilobytes)}/{int(pacote_em_kilobytes*numero_de_pacotes)}Kb"
    print('\r'+enviado, end='')
    time.sleep(delay)


# Limpando buffers e sockets
sock.close()
file.close()