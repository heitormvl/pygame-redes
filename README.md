### Conteúdo
 * Questão 1 e 2: Aplicação de chat cliente/servidor utilizando Sockets TCP.
    * O servidor aguarda conexões em `127.0.0.1:32271`.
    * O cliente envia mensagens para o servidor e ambos podem encerrar a conversa com `QUIT`.
 * Questão 3 (Desafio): Aplicação de jogo Pong utilizando Sockets, Threads e Pygame.
   * O servidor gerencia a lógica do jogo e a renderização via Pygame.
   * O servidor utiliza threads para tratar a conexão do cliente sem interromper o loop principal do jogo.
   * O cliente envia comandos de movimento (UP/DOWN) via socket TCP para controlar a raquete remotamente.

### Requisitos e Dependências
   * Python 3.12
   * Para a execução das Questões 1 e 2, não há dependências adicionais além da biblioteca padrão `socket`.
   * Para a execução da Questão 3, é necessário instalar as seguintes bibliotecas Python: ˋpip install pygame keyboardˋ
   * _Nota 1: A biblioteca keyboard pode exigir permissões de administrador (root/sudo) para capturar eventos do teclado dependendo do sistema operacional._
   * _Nota 2: Pode ser necessário configurar o firewall para permitir conexões na porta utilizada para ambos os servidores._

### Como Executar
Chat TCP (Questões 1 e 2)
 * Servidor: Inicie o arquivo chat_server.py. O servidor ficará em estado de escuta aguardando a conexão.
 * Cliente: Inicie o arquivo chat_client.py. Após a conexão, envie mensagens e use `QUIT` para encerrar.

Jogo Pong Remoto (Questão 3)
 * Servidor: Inicie o arquivo pong_server.py. O servidor ficará em estado de escuta aguardando a conexão.
 * Cliente: Inicie o arquivo pong_client.py. Após a conexão, utilize as setas do teclado para controlar a raquete na tela do servidor.

### Vídeo
   * [Link do Vídeo Questão 1 e 2 no Youtube](https://youtu.be/8QN2vfcjfJQ)
   * [Link do Vídeo Questão 3 no Youtube](https://youtu.be/N5aYZoOxo8s)

Integrantes
 * Heitor Maciel - 10402559
 * Murilo Nascimento - 10403318
 * Leonardo Magalhães - 10395913
