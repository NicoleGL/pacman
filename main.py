import pygame


pygame.display.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Pac-Man")


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        clock.tick(60)



main()