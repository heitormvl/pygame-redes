import socket
import keyboard
import time
# ---------------- CLIENTE TCP ----------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))  # conecta ao servidor (mesma máquina)
print("Use as setas ↑ e ↓ para mover a raquete.")
while True:
    try:
        # Se o usuário pressiona a seta ↑, envia "UP" para o servidor
        if keyboard.is_pressed("up"):
            client.sendall(b"UP")
            time.sleep(0.05)  # pequena pausa para evitar flood
        # Se o usuário pressiona a seta ↓, envia "DOWN"
        elif keyboard.is_pressed("down"):
            client.sendall(b"DOWN")
            time.sleep(0.05)
    except:
        break
