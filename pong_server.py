import socket
import threading
import pygame
# ---------------- CONFIGURAÇÕES DO JOGO ----------------
WIDTH, HEIGHT = 600, 400          # Tamanho da tela
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_SIZE = 10
# ---------------- ESTADO INICIAL ----------------
paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2   # posição inicial da raquete
ball_x, ball_y = WIDTH // 2, HEIGHT // 2      # posição inicial da bola
ball_dx, ball_dy = 4, 4                       # velocidade da bola
# lock = garante segurança no acesso a variáveis globais quando há múltiplas threads
lock = threading.Lock()
# ---------------- THREAD PARA CLIENTE ----------------
def client_thread(conn):
    """
    Esta função roda em uma thread separada.
    O cliente envia comandos "UP" ou "DOWN",
    e o servidor atualiza a posição da raquete.
    """
    global paddle_y
    while True:
        try:
            # Recebe mensagem do cliente
            data = conn.recv(1024).decode()
            if not data:
                break
            # Atualiza posição da raquete
            with lock:
                if data == "UP" and paddle_y > 0:
                    paddle_y -= 10
                elif data == "DOWN" and paddle_y < HEIGHT - PADDLE_HEIGHT:
                    paddle_y += 10
        except:
            break
    conn.close()
# ---------------- LOOP PRINCIPAL DO JOGO ----------------
def game_loop():
    """
    Este loop mantém o jogo rodando:
    - Atualiza a posição da bola
    - Verifica colisões (paredes e raquete)
    - Desenha a tela
    """
    global ball_x, ball_y, ball_dx, ball_dy, paddle_y

    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        # Verifica se o jogador fechou a janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # ---------------- MOVIMENTO DA BOLA ----------------
        ball_x += ball_dx
        ball_y += ball_dy
        # Rebote no topo e base
        if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
            ball_dy *= -1
        # Rebote nas laterais (simples, sem pontuação)
        if ball_x <= 0 or ball_x >= WIDTH - BALL_SIZE:
            ball_dx *= -1
        # Colisão da bola com a raquete
        if (ball_x <= 20 and paddle_y <= ball_y <= paddle_y + PADDLE_HEIGHT):
            ball_dx *= -1
        # ---------------- DESENHO NA TELA ----------------
        win.fill((0,0,0))  # fundo preto
        pygame.draw.rect(win, (255,255,255), (10, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # raquete
        pygame.draw.rect(win, (255,255,255), (ball_x, ball_y, BALL_SIZE, BALL_SIZE))        # bola
        pygame.display.flip()
        clock.tick(60)  # 60 FPS
# ---------------- SERVIDOR TCP ----------------
def start_server():
    """
    O servidor:
    - Cria um socket TCP
    - Aguarda um cliente se conectar
    - Inicia uma thread para escutar os comandos do cliente
    - Roda o loop do jogo
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))   # Escuta em todas interfaces na porta 5000
    server.listen(1)
    print("Servidor aguardando cliente...")
    conn, addr = server.accept()
    print("Cliente conectado:", addr)
    # Inicia a thread para receber comandos do cliente
    threading.Thread(target=client_thread, args=(conn,), daemon=True).start()
    # Inicia o jogo
    game_loop()
if __name__ == "__main__":
    start_server()
