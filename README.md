### Conteúdo
 * Questão 3 (Desafio): Aplicação de jogo Pong utilizando Sockets, Threads e Pygame.
   * O servidor gerencia a lógica do jogo e a renderização via Pygame.
   * O servidor utiliza threads para tratar a conexão do cliente sem interromper o loop principal do jogo.
   * O cliente envia comandos de movimento (UP/DOWN) via socket TCP para controlar a raquete remotamente.

### Requisitos e Dependências
Para a execução da Questão 3, é necessário instalar as seguintes bibliotecas Python: ˋpip install pygame keyboardˋ
 * Nota: A biblioteca keyboard pode exigir permissões de administrador (root/sudo) para capturar eventos do teclado dependendo do sistema operacional.

### Como Executar
Jogo Pong Remoto (Questão 3)
 * Servidor: Inicie o arquivo pong_server.py. O servidor ficará em estado de escuta aguardando a conexão.
 * Cliente: Inicie o arquivo pong_client.py. Após a conexão, utilize as setas do teclado para controlar a raquete na tela do servidor.

### Vídeo
   * [Link do Vídeo Questão 3 no Youtube]()

Integrantes
 * Heitor Maciel - 10402559
 * Murilo Nascimento - 10403318
 * Leonardo Magalhães - 10395913
