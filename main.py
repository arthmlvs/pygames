import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("pygame artemijs")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 50))
square.fill('Orange')

myfont = pygame.font.Font('fonts/YujiMai-Regular.ttf', 40)
text_surface = myfont.render('itartemijs', False, 'blue')

player = pygame.image.load('images/icon.png')

running = True 
while running:

    screen.blit(square, (600/2-50/2, 300/2-50/2))
    screen.blit(player, (0, 0))
    screen.blit(text_surface, (500, 100))




    pygame.draw.circle(square, 'blue', (1, 1), 6)
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        