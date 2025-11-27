import pygame
import random

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DOOM SLASHER – Versión Intermedia")

clock = pygame.time.Clock()

# Cargar sonido
try:
    hit_sound = pygame.mixer.Sound("hit.wav")
except:
    hit_sound = None

# ============================================
# COLORES DOOM
# ============================================
BLACK = (10, 10, 10)
RED = (255, 40, 40)
DARK_RED = (150, 0, 0)
YELLOW = (255, 220, 0)
WHITE = (255, 255, 255)

# ============================================
# JUGADOR
# ============================================
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 6
player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

# ============================================
# DEMONIOS
# ============================================
demon_size = 40
demon_count = 3  # 3 demonios en juego

def create_demon():
    return {
        "rect": pygame.Rect(
            random.randint(0, WIDTH - demon_size),
            random.randint(0, HEIGHT - demon_size),
            demon_size,
            demon_size
        ),
        "speed_x": random.choice([-4, -3, -2, 2, 3, 4]),
        "speed_y": random.choice([-4, -3, -2, 2, 3, 4]),
        "strong": random.random() < 0.25  # 25% demonio peligroso
    }

demons = [create_demon() for _ in range(demon_count)]

# ============================================
# SCORE Y GAME OVER
# ============================================
font = pygame.font.Font(None, 40)
score = 0
game_over = False

# ============================================
# LOGICA PRINCIPAL
# ============================================
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # -------------------------
        # Movimiento del jugador
        # -------------------------
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.x > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.x < WIDTH - player_size:
            player_rect.x += player_speed
        if keys[pygame.K_UP] and player_rect.y > 0:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN] and player_rect.y < HEIGHT - player_size:
            player_rect.y += player_speed

        # -------------------------
        # Movimiento demonios
        # -------------------------
        for demon in demons:
            demon["rect"].x += demon["speed_x"]
            demon["rect"].y += demon["speed_y"]

            # Rebotar en paredes
            if demon["rect"].left <= 0 or demon["rect"].right >= WIDTH:
                demon["speed_x"] *= -1
            if demon["rect"].top <= 0 or demon["rect"].bottom >= HEIGHT:
                demon["speed_y"] *= -1

            # -------------------------
            # Colisión jugador - demonio
            # -------------------------
            if player_rect.colliderect(demon["rect"]):
                if demon["strong"]:
                    game_over = True
                else:
                    score += 1
                    if hit_sound:
                        hit_sound.play()
                    # Respawn del demonio
                    demons.remove(demon)
                    demons.append(create_demon())

        # -------------------------
        # Dibujar jugador
        # -------------------------
        pygame.draw.rect(screen, YELLOW, player_rect)

        # -------------------------
        # Dibujar demonios
        # -------------------------
        for demon in demons:
            color = DARK_RED if demon["strong"] else RED
            pygame.draw.rect(screen, color, demon["rect"])

        # Mostrar score
        text = font.render(f"Demonios eliminados: {score}", True, WHITE)
        screen.blit(text, (10, 10))

    else:
        # -------------------------
        # GAME OVER
        # -------------------------
        go_text = font.render("GAME OVER", True, RED)
        screen.blit(go_text, (WIDTH//2 - 100, HEIGHT//2 - 40))

        retry_text = font.render("Presiona R para reiniciar", True, WHITE)
        screen.blit(retry_text, (WIDTH//2 - 150, HEIGHT//2 + 10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Reiniciar juego
            player_rect.x = WIDTH // 2
            player_rect.y = HEIGHT // 2
            demons = [create_demon() for _ in range(demon_count)]
            score = 0
            game_over = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
