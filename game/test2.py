import pygame
import time
pygame.init()
display = pygame.display.set_mode((320, 568))
image = pygame.image.load('img.png')
bird = pygame.image.load('img_1.png')
gun =  pygame.image.load('gun.jpg')
bullet = pygame.image.load('bullet.png')
blast = pygame.image.load('blast.png')
bird_x = 10
move = "Right"
FPS = 60
blast_available = True
point = 0
gun_x = 100
gun_y = 500
bullet_y = gun_y - 20
bullettrue = False
clock = pygame.time.Clock()
while True:
    #clock.tick(FPS)
    pygame.event.get()
    keys = pygame.key.get_pressed()
    '''
    if keys[pygame.K_SPACE]:
        print("Space")
    elif keys[pygame.K_LEFT]:

        print("Left")#bam
    '''

    #incorrect code
    '''display.blit(image, (0, 0))
    display.blit(bird, (bird_x, 0))
    move = 'Right'
    if move == 'Right':
        bird_x = bird_x + 1
        #time.sleep(.01)
        print(bird_x)
        if bird_x == 269:
            move = 'Left'
    '''


    display.blit(image, (0, 0))
    display.blit(bird, (bird_x, 0))

    #fire
    display.blit(bullet,(gun_x,bullet_y))
    if keys[pygame.K_UP]:
        #print('us')
        bullettrue = True
    if bullettrue:
        display.blit(bullet, (gun_x, bullet_y))
        bullet_y -= 1
        print("TTTTT", bullet_y)
        if bullet_y == -140:
            blast_available = True
        if blast_available:
             display.blit(blast, (0, 0))


        '''
    if keys[pygame.K_UP]:
        bullet_available = True
        print(bullet_available)
    if bullet_available:
        display.blit(bullet,(gun_x,bullet_y))

        bullet_y -= 1
        '''

    #fire

    #gun start
    display.blit(gun,(gun_x,gun_y))
    if keys[pygame.K_RIGHT]:
        gun_x = gun_x + .1
    elif keys[pygame.K_LEFT]:
        gun_x = gun_x - .1

    #gun end

    if move == 'Right':
        bird_x = bird_x + .01
        #time.sleep(.01)
        print(bird_x)
        if bird_x == 257.84999999991066:
            move = 'Left'
    else:
        bird_x = bird_x - .01
        if (bird_x == 3.620000000000159 ):
            move = 'Right'
        print(bird_x)
    pygame.display.update()
