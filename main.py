import pygame
import random
import os
import sys

# Fonction pour gérer les chemins des ressources avec PyInstaller
def resource_path(relative_path):
    try:
        # PyInstaller crée un dossier temporaire et stocke le chemin dans _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initialisation de Pygame
pygame.init()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
PURPLE = (128, 0, 128)
SKY_BLUE = (135, 206, 235)
RED = (200, 0, 0)

# Dimensions de l'écran AJUSTÉES (Format paysage/standard pour fond de château)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Harry Potter Flappy Wings")

# Polices
font_score = pygame.font.SysFont("georgia", 40, bold=True)
font_title = pygame.font.SysFont("georgia", 60, bold=True)
font_menu = pygame.font.SysFont("georgia", 30)

def load_image(name, size):
    path = resource_path(name)
    try:
        img = pygame.image.load(path)
        return pygame.transform.scale(img, size)
    except:
        surf = pygame.Surface(size)
        surf.fill((0, 0, 255)) 
        return surf

def main_menu():
    clock = pygame.time.Clock()
    menu_bg = load_image("HarryPotter.png", (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True
    while running:
        screen.blit(menu_bg, (0, 0))
        
        instr_surf = font_menu.render("Appuyez sur ESPACE pour Jouer", True, WHITE)
        instr_rect = instr_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        instr_shadow = font_menu.render("Appuyez sur ESPACE pour Jouer", True, BLACK)
        screen.blit(instr_shadow, (instr_rect.x+2, instr_rect.y+2))
        screen.blit(instr_surf, instr_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return 

        pygame.display.flip()
        clock.tick(60)

def game_loop():
    clock = pygame.time.Clock()
    
    # Harry (Le joueur)
    player_size = (70, 70)
    player_img = load_image("harry_transparent.png", player_size)
    player_rect = player_img.get_rect(center=(200, SCREEN_HEIGHT // 2))
    
    # Fond d'écran CHANGÉ en fond_chateau_clair.png
    background_img = load_image("fond_chateau_clair.png", (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    gravity = 0.25
    bird_movement = 0
    
    # Obstacles (Sorcières)
    enemy_size = (80, 80)
    initial_speed = 5
    enemies = [] 
    
    witch_images_files = [
        "sorciere_rouge_gauche (1).png", "sorciere_verte_gauche.png", 
        "sorciere_violette_gauche.png"
    ]
    witch_images = [load_image(img, enemy_size) for img in witch_images_files]
    
    SPAWNENEMY = pygame.USEREVENT
    pygame.time.set_timer(SPAWNENEMY, 1500)

    score = 0
    running = True
    game_over = False

    while running:
        screen.blit(background_img, (0, 0))
        
        current_speed = initial_speed + (score * 0.2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird_movement = -8 
                
                if game_over:
                    if event.key == pygame.K_r:
                        game_loop()
                        return
                    if event.key == pygame.K_q:
                        main_menu()
                        game_loop()
                        return

            if event.type == SPAWNENEMY and not game_over:
                random_witch_img = random.choice(witch_images)
                random_y = random.randint(50, SCREEN_HEIGHT - 100)
                enemy_rect = pygame.Rect(SCREEN_WIDTH, random_y, enemy_size[0], enemy_size[1])
                enemies.append({"rect": enemy_rect, "img": random_witch_img})

        if not game_over:
            bird_movement += gravity
            player_rect.centery += bird_movement
            
            if player_rect.top <= 0 or player_rect.bottom >= SCREEN_HEIGHT:
                game_over = True

            for enemy in enemies[:]:
                enemy["rect"].x -= current_speed
                if player_rect.colliderect(enemy["rect"]):
                    game_over = True
                if enemy["rect"].right == 200:
                    score += 1
                if enemy["rect"].right < 0:
                    enemies.remove(enemy)

        # DESSIN
        for enemy in enemies:
            screen.blit(enemy["img"], enemy["rect"])
            
        screen.blit(player_img, player_rect)
        
        title_surf = font_title.render("HARRY POTTER", True, GOLD)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH // 2, 40))
        shadow_surf = font_title.render("HARRY POTTER", True, BLACK)
        screen.blit(shadow_surf, (title_rect.x+2, title_rect.y+2))
        screen.blit(title_surf, title_rect)

        score_text = font_score.render(f"Score : {score}", True, WHITE)
        speed_text = font_menu.render(f"Vitesse : {current_speed:.1f}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - 80, 100))
        screen.blit(speed_text, (SCREEN_WIDTH // 2 - 80, 140))

        if game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150)) 
            screen.blit(overlay, (0,0))

            over_text = font_title.render("GAME OVER", True, RED)
            screen.blit(over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
            
            r_text = font_menu.render("Appuyez sur R pour Recommencer", True, WHITE)
            q_text = font_menu.render("Appuyez sur Q pour Menu Principal", True, WHITE)
            
            screen.blit(r_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 20))
            screen.blit(q_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 60))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main_menu()
    game_loop()
