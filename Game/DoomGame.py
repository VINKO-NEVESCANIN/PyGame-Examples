import pygame
import random

# --------------------------
# CONFIGURACIÓN INICIAL
# --------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DOOM SLASHER – Mini Game")

clock = pygame.time.Clock()

# --------------------------
# COLORES DOOM
# --------------------------
RED = (200, 0, 0)
BLACK = (20, 20, 20)
YELLOW = (255, 200, 0)
WHITE = (255, 255, 255)

# --------------------------
# JUGADOR (DOOM SLAYER)
# --------------------------
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 6

# --------------------------
# DEMONIO
# --------------------------
demon_size = 40

def spawn_demon():
    """Devuelve una nueva posición aleatoria del demonio."""
    return (
        random.randint(0, WIDTH - demon_size),
        random.randint(0, HEIGHT - demon_size)
    )

demon_x, demon_y = spawn_demon()

# --------------------------
# SCORE
# --------------------------
score = 0
font = pygame.font.Font(None, 36)

# --------------------------
# LOOP PRINCIPAL DEL JUEGO
# --------------------------
running = True
while running:
    screen.fill(BLACK)

    # --------------------------
    # EVENTOS
    # --------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --------------------------
    # MOVIMIENTO DEL JUGADOR
    # --------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed

    # --------------------------
    # COLISIÓN (Matar demonio)
    # --------------------------
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    demon_rect = pygame.Rect(demon_x, demon_y, demon_size, demon_size)

    if player_rect.colliderect(demon_rect):
        score += 1
        demon_x, demon_y = spawn_demon()

    # --------------------------
    # DIBUJAR
    # --------------------------
    # Jugador (Slayer)
    pygame.draw.rect(screen, YELLOW, player_rect)

    # Demonio
    pygame.draw.rect(screen, RED, demon_rect)

    # Score
    text = font.render(f"Demonios eliminados: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    # Actualizar pantalla
    pygame.display.update()
    clock.tick(60)

pygame.quit()
