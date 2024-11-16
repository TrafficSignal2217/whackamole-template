import pygame
import random

# :exe 'edit '.stdpath('config').'/init.vim'


#def mouse_in_rect(top_left, bottom_right):
    #if pygame.mouse.get_pos()[0] > 

def main():
    tile_size = 32
    screen_width = 640
    screen_height = 512
    color_bg = "light green"

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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        main()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):
                        mole_x = random.randint(1, screen_width // tile_size - 1) * tile_size
                        mole_y = random.randint(1, screen_height // tile_size - 1) * tile_size
                        mole_rect.topleft = (mole_x, mole_y)
            screen.fill(color_bg)

            #if pygame.mouse.get_pressed(3)[0]:


            # Render game
            for y in range(screen_height // tile_size):
                pygame.draw.line(screen, "blue", (0, y * tile_size), (screen_width, y * tile_size))

            for x in range(screen_width // tile_size):
                pygame.draw.line(screen, "blue", (x * tile_size, 0), (x * tile_size, screen_height))

            screen.blit(mole_image, (mole_x, mole_y))

            # Flip display to draw to screen
            pygame.display.flip()
            clock.tick(60)


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
