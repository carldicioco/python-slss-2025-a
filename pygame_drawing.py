# Pygame Drawing
# Author: Ubial
# 5 January 2026

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)
    YELLOW = (255, 230, 0)

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Beautiful Drawing")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)

        # Draw shapes
        pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 2 - 80), 80)
        pygame.draw.circle(screen, WHITE, (350, 200), 10)
        pygame.draw.circle(screen, BLACK, (350, 200), 5)
        pygame.draw.circle(screen, WHITE, (450, 200), 10)
        pygame.draw.circle(screen, BLACK, (450, 200), 5)
        pygame.draw.rect(screen, BLACK, (350, 250, 100, 10))  # FIXED

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
