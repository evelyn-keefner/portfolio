import pygame

def main() -> None:
    pygame.init()
    pygame.event.pump()

    screen = pygame.display.set_mode()
    window_x, window_y = screen.get_size()
    x_center = int(window_x / 2)
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        screen.fill('gray')

        pygame.draw.circle(screen, "white", (x_center, 500), 50)
        pygame.draw.circle(screen, "white", (x_center, 450), 30)
        pygame.draw.circle(screen, "white", (x_center, 420), 20)


        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
