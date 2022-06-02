import socket

print("INCICIO");

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

s.bind(('', 5555)) # Esta linha define para qual IP e porta o servidor deve aguardar a conexão, que no nosso caso é qualquer IP, por isso o Host é ”

ip_local = socket.gethostbyname(socket.gethostname())
print(f'IP Local: {ip_local}')

while True: # roda enquanto tiver conexão

    print("AGUARDANDO CONEXAO"); 

    data = s.recvfrom(2000) # o recv recebe os dados de quem está requisitando
    # 2000 é o número máx de bytes aceitos

    message = data[0]

    address = data[1]

    if data == 'dcs':
        print('Cliente escolheu desconectar o servidor.')
        break       
    else:        
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
s.close()
