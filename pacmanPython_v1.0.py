import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración del juego
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Carreras de Autos")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Jugador
player_width, player_height = 50, 100
player_x = width // 2 - player_width // 2
player_y = height - 2 * player_height
player_speed = 7

# Enemigos (otros autos)
enemy_width, enemy_height = 50, 100
enemies = [{"x": random.randint(0, width - enemy_width), "y": -enemy_height, "speed": random.randint(2, 5)} for _ in range(5)]

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Función para mostrar la puntuación
def show_score():
    score_text = font.render(f"Puntuación: {score}", True, white)
    screen.blit(score_text, (10, 10))

# Función para mostrar un mensaje en pantalla
def show_message(message):
    font_large = pygame.font.Font(None, 72)
    text = font_large.render(message, True, white)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

# Bucle principal del juego
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    # Mover jugador
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Mover enemigos
    for enemy in enemies:
        enemy["y"] += enemy["speed"]
        if enemy["y"] > height:
            enemy["y"] = -enemy_height
            enemy["x"] = random.randint(0, width - enemy_width)
            score += 1

    # Colisiones con enemigos
    for enemy in enemies:
        if player_x < enemy["x"] + enemy_width and player_x + player_width > enemy["x"] and \
                player_y < enemy["y"] + enemy_height and player_y + player_height > enemy["y"]:
            # Has chocado con un enemigo, mostrar mensaje y reiniciar posición
            show_message("¡Has chocado!")
            player_x = width // 2 - player_width // 2
            score = 0

    # Dibujar fondo
    screen.fill(black)

    # Dibujar jugador
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    # Dibujar enemigos
    for enemy in enemies:
        pygame.draw.rect(screen, red, (enemy["x"], enemy["y"], enemy_width, enemy_height))

    # Dibujar puntuación
    show_score()

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(60)

# Finalizar Pygame
pygame.quit()
sys.exit()
