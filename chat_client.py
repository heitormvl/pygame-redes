# Transcrição do arquivo ClientChat.py
import socket

TCP_IP = '127.0.0.1' # Usando localhost para testes, se for em máquinas diferentes use o IP
TCP_PORTA = 32271     # Porta TIA
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Tentando conectar a {TCP_IP}:{TCP_PORTA}...")

try:
    cliente.connect((TCP_IP, TCP_PORTA))
    print("Conexão estabelecida. Digite 'QUIT' para sair.")
except ConnectionRefusedError:
    print("Erro: Servidor não encontrado ou não está escutando na porta.")
    exit()

while True:
    # 1. Enviar mensagem do cliente
    MENSAGEM = input("Você: ")
    cliente.send(MENSAGEM.encode('UTF-8'))
    
    if MENSAGEM.upper() == 'QUIT':
        print("Cliente encerrando a conexão.")
        break

    # 2. Receber resposta do servidor
    try:
        data = cliente.recv(1024)
        if not data:
            print("Servidor encerrou a conexão.")
            break
        
        mensagem_servidor = data.decode('utf-8').strip()
        print(f"Servidor: {mensagem_servidor}")
        
        if mensagem_servidor.upper() == 'QUIT':
            print("Servidor enviou QUIT. Encerrando.")
            break
            
    except Exception as e:
        print(f"Erro ao receber dados: {e}")
        break

cliente.close()
print("Chat encerrado.")
