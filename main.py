import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("pygame artemijs")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 50))
square.fill('Orange')

running = True 
while running:

    screen.blit(square, (600/2-50/2, 300/2-50/2))

    pygame.draw.circle(square, 'blue', (1, 1), 6)
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        