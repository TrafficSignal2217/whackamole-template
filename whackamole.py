import pygame


def main():
    tile_size = 32
    screen_width = 640
    screen_height = 512



    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect()
        mole_x = 0
        mole_y = 0
        screen = pygame.display.set_mode((screen_width, screen_height))
        clock = pygame.time.Clock()
        running = True

        # Game loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")

            # Render game
            for y in range(screen_height // tile_size):
                pygame.draw.line(screen, "blue", (0, y * tile_size), (screen_width, y * tile_size))

            for x in range(screen_width // tile_size):
                pygame.draw.line(screen, "blue", (x * tile_size, 0), (x * tile_size, screen_height))

            screen.blit(mole_image, mole_rect)

            # Flip display to draw to screen
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
