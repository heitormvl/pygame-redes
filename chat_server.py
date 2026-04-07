import socket

TCP_IP = '127.0.0.1' # Usando localhost para testes, se for em máquinas diferentes use o IP
TCP_PORTA = 32271     # Porta TIA
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((TCP_IP, TCP_PORTA))
servidor.listen(1)

print(f"Servidor aguardando conexão em {TCP_IP}:{TCP_PORTA}...")
conn, addr = servidor.accept()
print(f'Conexão estabelecida com: {addr}')

while True:
    # 1. Receber mensagem do cliente
    try:
        data = conn.recv(1024)
        mensagem_cliente = data.decode('utf-8').strip()
    except Exception as e:
        print(f"Erro ao receber dados: {e}")
        break

    if not data or mensagem_cliente.upper() == 'QUIT':
        print("cliente encerrou a conexão ou enviou QUIT.")
        break
    
    print(f"Cliente: {mensagem_cliente}")

    # 2. Enviar resposta do servidor
    resposta = input("Você: ")
    conn.send(resposta.encode('utf-8'))

    if resposta.upper() == 'QUIT':
        print("Servidor encerrando a conexão.")
        break

conn.close()
servidor.close()
print("Chat encerrado.")
