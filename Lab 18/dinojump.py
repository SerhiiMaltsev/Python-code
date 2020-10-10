#Serhii Maltsev (sm5zj)

'''
This game has all the basic features and two features from the list of additional components:
1) Gamesprites:
        - Dinosaur looks like dinosaur and has running animations.
        - Cactuses look like cactuses.
2) Acceleration and nighttime:
        - every 750 points daytime changes to the opposite (day to night or night to day).
        - every 10 frames (5 point) speed of the cactuses increses by 0.1 frame per second.
'''

import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
ground = gamebox.from_image(400, 550, 'ground.png')
dino = gamebox.from_image(250, 451, 'dino1.png')
arrayOfCactuses = []
circlesOnGround = []

arrayOfCactuses.append(gamebox.from_image(1000, 475, 'cactus5050.png'))
arrayOfCactuses.append(gamebox.from_image(1500, 465, 'cactus7070.png'))
arrayOfCactuses.append(gamebox.from_image(2000, 455, 'cactus9090.png'))

acceleration = 1.5
inAir = False
verticalSpeed = 0
cactusesSpeed = -10
cactusesAcceleration = 0.1
notlost = True
score = 0
sprite = 1
dinoAnimation = True

measureTicks = 0
day = True

def reset():
    '''
    This function is used to reset the value of all variables after the player looses
    :return: None
    '''
    global arrayOfCactuses, day, acceleration, inAir, verticalSpeed, cactusesSpeed, notlost, score
    arrayOfCactuses = []

    arrayOfCactuses.append(gamebox.from_image(1000, 475, 'cactus5050.png'))
    arrayOfCactuses.append(gamebox.from_image(1500, 465, 'cactus7070.png'))
    arrayOfCactuses.append(gamebox.from_image(2000, 455, 'cactus9090.png'))

    acceleration = 1.5
    inAir = False
    verticalSpeed = 0
    cactusesSpeed = -10
    notlost = True
    score = 0
    day = True

def tick(keys):
    """
    This function is place where all code of the game is executes
    :param keys: build in function of pygame that helps user to do input using keyboard and mouse
    :return: None
    """
    global sprite, inAir, acceleration, verticalSpeed, cactusesSpeed, notlost, measureTicks, dino, dinoAnimation, \
         score, day, cactusesAcceleration

    if notlost:
        measureTicks += 1

        scoresign = gamebox.from_text(700, 100, "Score: " + str(score), 20, "white")
        if measureTicks %1 ==0:
            score +=2
            scoresign = gamebox.from_text(700, 100, "Score: " + str(score), 20, "white")

        if measureTicks % 10 ==0:
            cactusesSpeed -= cactusesAcceleration

        if (score %750 ==0) and (day == True):
            day = False
        elif (score %750 ==0) and (day == False):
            day = True

        if pygame.K_SPACE in keys:
            if (inAir == False):
                verticalSpeed = -25
                inAir = True
                dino.image = 'dinowhilejump.png'
                dinoAnimation = False

        if measureTicks % 3 == 0 and dinoAnimation == True:
            if sprite == 1:
                dino.image = 'dino2.png'
                sprite = 2
            elif sprite == 2:
                dino.image = 'dino1.png'
                sprite = 1

        dino.move(0, verticalSpeed)
        verticalSpeed += acceleration

        if dino.touches(other = ground):
            verticalSpeed = 0
            inAir = False
            dino.y = 451
            if dinoAnimation == False:
                dino.image = 'dino1.png'
                dinoAnimation = True


        for i in arrayOfCactuses:
            i.move(cactusesSpeed, 0)

        for i in arrayOfCactuses:
            if i.x < -100:
                i.x = random.randrange(1000, 2000)

        for i in arrayOfCactuses:
            if i.touches(other = dino):
                notlost = False

        if day == True:
            camera.clear("blue")
        else:
            camera.clear("black")

        camera.draw(ground)
        camera.draw(dino)

        for i in arrayOfCactuses:
            camera.draw(i)

        camera.draw(scoresign)
        camera.display()

    if notlost == False:
        lostsign = gamebox.from_text(400, 300, "You lost! Press space to try again", 40, "red")
        if pygame.K_SPACE in keys:
            reset()
        inAir = True

        camera.draw(lostsign)
        camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)