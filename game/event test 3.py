import pygame
import time
pygame.init()
display = pygame.display.set_mode((320, 568))
image = pygame.image.load('img.png')
bird = pygame.image.load('img_1.png')
bird_x = 1
FPS = 60
clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    '''
    if keys[pygame.K_SPACE]:
        print("Space")
    elif keys[pygame.K_LEFT]:

        print("Left")#bam
    '''

    display.blit(image, (0, 0))
    display.blit(bird, (bird_x, 0))
    move = 'Right'
    if move == 'Right':
        bird_x = bird_x + 1
        #time.sleep(.01)
        print(bird_x)
        if bird_x == 269:
            move = 'Left'
    else:
        bird_x = bird_x - 1
        if (bird_x == 0 ):
            move = 'Right'
    pygame.display.update()