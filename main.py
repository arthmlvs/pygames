import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("pygame artemijs")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

running = True 
while running:

    # screen.fill((255, 120, 3))

    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type  == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((3, 230, 255))    
