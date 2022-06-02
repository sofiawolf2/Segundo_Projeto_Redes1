import socket
import time

# 1 Server Setup
print("Configurando servidor UDP")

ip_local = socket.gethostbyname(socket.gethostname())
print(f'IP Local: {ip_local}')

HOST = ip_local
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))
sock.settimeout(70.0)


# 2/5 Esperando receber lista de arquivos do cliente
print("Recebendo lista de arquivos\n")
files = []
while True:
    data, address = sock.recvfrom(512)
    if data.decode(errors="ignore") == "stop":
        break
    file_name = data.decode()
    print(f"[{len(files)}] {file_name}")
    files.append(file_name)

# 6 Enviando ao cliente qual arquivo baixar
file_choice = int(input("\nQual arquivos receber?"))
while not (0 <= file_choice < len(files)):
    print("Opcao invalida!")
    file_choice = int(input("Qual arquivos receber? "))

sock.sendto(file_choice.to_bytes(4, "little"), address)


# 10 Recebendo numero de pacotes
# Queremos saber em quantos pacotes o arquivo sera mandado
data = sock.recv(4)
numero_de_pacotes = int.from_bytes(data, "little")

# 12 Recebendo pacotes
sock.settimeout(5.0)
file = open(files[file_choice], "wb")
pacote_em_kilobytes = 512
pacote_em_bytes = pacote_em_kilobytes * 8

print(f"Recebendo {numero_de_pacotes} pacotes...")
start = time.time()
for i in range(numero_de_pacotes):
    data = sock.recv(pacote_em_bytes)
    file.write(data)
    porcentagem = f"Baixando... {round((100*(i+1))/numero_de_pacotes, 2)}%"
    # print(porcentagem)
    print('\r'+porcentagem, end='')

tempo_de_download = round(time.time()-start, 2)
print(f"\nO download foi completo em {tempo_de_download} sec")

# Limpando buffers e sockets
file.close()
sock.close()