# Samuel Sheppard (sms8hny) #Serhii Maltsev (sm5zj)

import gamebox
import pygame
import math
import sys
import random

camera = gamebox.Camera(800, 600)

ticker = 0

background = gamebox.from_image(400, 300, 'background.png')
player = gamebox.from_image(600, 300, 'player.png')
arrayOfBullets = []
arrayOfCoins = []
enemies = []
flag = gamebox.from_image(400, 300, 'flag.png')
health = [gamebox.from_image(30, 30, 'hp.png'), gamebox.from_image(110, 30, 'hp.png'), gamebox.from_image(190, 30, 'hp.png')]

currentangle = 0
hp = 3
numberOfTicksToShoot = 30
measureticks = numberOfTicksToShoot

numberOfCoins = 0
score = 0

delayForEnemies = 30
delayForInterface = 30
bullet_speed = 15
gun_price = 10
hp_price = 10

game = False

interfaceForUpgrades = False

StartOfTheGame = True

Lost = False

view_hs = False

def reset():
    global currentangle, measureticks, numberOfTicksToShoot, arrayOfCoins, game, hp, delayForEnemies, numberOfCoins, \
        score, interfaceForUpgrades, delayForInterface, StartOfTheGame, ticker, background, player, arrayOfBullets, \
        enemies, flag, health, bullet_speed, gun_price, hp_price, Lost, view_hs
    ticker = 0

    view_hs = False

    Lost = False

    background = gamebox.from_image(400, 300, 'background.png')
    player = gamebox.from_image(600, 300, 'player.png')
    arrayOfBullets = []
    arrayOfCoins = []
    enemies = []
    flag = gamebox.from_image(400, 300, 'flag.png')
    health = [gamebox.from_image(30, 30, 'hp.png'), gamebox.from_image(110, 30, 'hp.png'),
              gamebox.from_image(190, 30, 'hp.png')]

    currentangle = 0
    hp = 3
    numberOfTicksToShoot = 30
    measureticks = numberOfTicksToShoot

    numberOfCoins = 0
    score = 0

    delayForEnemies = 30
    delayForInterface = 30

    interfaceForUpgrades = False
    bullet_speed = 15

    gun_price = 10
    hp_price = 10

def tick(keys):
    global currentangle, measureticks, numberOfTicksToShoot, arrayOfCoins, game, hp, delayForEnemies, numberOfCoins, \
        score, interfaceForUpgrades, delayForInterface, StartOfTheGame, gun_price, hp_price, bullet_speed, Lost, view_hs

    if StartOfTheGame:
        if pygame.mouse.get_pressed()[0] and (pygame.mouse.get_pos()[0]>275) and (pygame.mouse.get_pos()[0]<525) and (pygame.mouse.get_pos()[1]<234) and (pygame.mouse.get_pos()[1]>166):
            StartOfTheGame = False
            game = True
            reset()

        if pygame.mouse.get_pressed()[0] and (pygame.mouse.get_pos()[0]>275) and (pygame.mouse.get_pos()[0]<525) and (pygame.mouse.get_pos()[1]<434) and (pygame.mouse.get_pos()[1]>366):
            sys.exit()

        if pygame.mouse.get_pressed()[0] and (pygame.mouse.get_pos()[0]>275) and (pygame.mouse.get_pos()[0]<525) and (pygame.mouse.get_pos()[1]<334) and (pygame.mouse.get_pos()[1]>266):
            view_hs = True


        camera.draw(gamebox.from_image(400, 300, "StartInterfaceBackground.png"))
        camera.draw(gamebox.from_image(400, 200, 'StartGameButton.png'))
        camera.draw(gamebox.from_image(400, 300, "HighScoresButton.png"))
        camera.draw(gamebox.from_image(400, 400, "ExitButton.png"))
        camera.draw(gamebox.from_text(150, 40, "Defend flag from zombies!", 30, "red"))
        camera.draw(gamebox.from_text(180, 560, "Use W, A, S, D to move character.", 30, "red"))
        camera.draw(gamebox.from_text(620, 40, "Use the mouse to rotate player", 30, "red"))
        camera.draw(gamebox.from_text(670, 560, "Press LMB to shoot", 30, "red"))


        if view_hs:
            camera.draw(gamebox.from_image(400, 300, "StartInterfaceBackground.png"))
            if pygame.K_SPACE in keys:
                view_hs = False
            camera.draw(gamebox.from_text(300, 25, "Press Space to go back", 40, "red"))

            stream = open('HighScores.txt', 'r')
            scores = stream.readlines()
            delta = 40
            for i in scores:
                camera.draw(gamebox.from_text(400, 100+delta, i[0:len(i)-1], 25, 'blue'))
                delta += 30

        camera.display()
    if game:

        measureticks +=1

        if pygame.K_w in keys:
            player.move(0, -5)

        if pygame.K_s in keys:
            player.move(0, 5)

        if pygame.K_a in keys:
            player.move(-5, 0)

        if pygame.K_d in keys:
            player.move(5, 0)

        if delayForInterface < 30:
            delayForInterface += 1

        if (pygame.K_SPACE in keys) and (delayForInterface >= 30):
            interfaceForUpgrades = True
            delayForInterface = 0

        if interfaceForUpgrades:
            game = False

        x = -(player.x - pygame.mouse.get_pos()[0])
        y = -(player.y - pygame.mouse.get_pos()[1])


        if delayForEnemies <= 30:
            delayForEnemies +=1

        for i in enemies:
            if i.touches(other=player):
                if delayForEnemies >= 30:
                    hp -= 1
                    delayForEnemies = 0

        if x == 0:
            x = 0.0001
        angle = int((math.atan2(x, y))*360/(math.pi*2))-90
        player.rotate((angle - currentangle))
        currentangle = angle

        if pygame.mouse.get_pressed()[0] == 1:
            vx = bullet_speed * (x/(math.sqrt(abs(x*x+y*y))))
            vy = bullet_speed * (y/(math.sqrt(abs(x*x+y*y))))

            if measureticks > numberOfTicksToShoot:
                arrayOfBullets.append([gamebox.from_image(player.x, player.y, 'bullet.png'), vx, vy])
                measureticks = 0

        for i in arrayOfBullets:
            i[0].move (i[1], i[2])

        for i in arrayOfBullets:
            for j in enemies:
                if i[0].touches(other=j):
                    arrayOfCoins.append(gamebox.from_circle(j.x, j.y, 'yellow', 5))
                    j.x = -2000000
                    j.y = -2000000
                    i[0].x = -1000000
                    i[0].y = -1000000
                    score += 10

        for i in arrayOfCoins:
            if i.touches(other=player):
                i.x = -1000000
                i.y = -1000000
                numberOfCoins += 1

        if hp == 0:
            game = False
            Lost = True

        for i in enemies:
            if i.touches(other=flag):
                Lost = True
                game = False

        if measureticks%50 == 0:
            if random.randint(1, 8) == 1:
                enemies.append(gamebox.from_image(random.randrange(-200, 0), random.randrange(-200, 0), 'New Piskel.png'))
                enemies[-1].rotate(
                    int((math.atan2(400 - enemies[-1].x, 300 - enemies[-1].y)) * 360 / (math.pi * 2)) - 90)
            elif random.randint(1, 8) == 2:
                enemies.append(gamebox.from_image(random.randrange(-200, 0), random.randrange(200, 400), 'New Piskel.png'))
                enemies[-1].rotate(
                    int((math.atan2(400 - enemies[-1].x, 300 - enemies[-1].y)) * 360 / (math.pi * 2)) - 90)
            elif random.randint(1, 8) == 3:
                enemies.append(gamebox.from_image(random.randrange(-200, 0), random.randrange(600, 800), 'New Piskel.png'))
                enemies[-1].rotate(
                    int((math.atan2(400 - enemies[-1].x, 300 - enemies[-1].y)) * 360 / (math.pi * 2)) - 90)
            elif random.randint(1, 8) == 4:
                enemies.append(gamebox.from_image(random.randrange(300, 500), random.randrange(-200, 0), 'New Piskel.png'))
                enemies[-1].rotate(
                    int((math.atan2(400 - enemies[-1].x, 300 - enemies[-1].y)) * 360 / (math.pi * 2)) - 90)
            elif random.randint(1, 8) == 5:
                enemies.append(gamebox.from_image(random.randrange(800, 1000), random.randrange(-200, 0), 'New Piskel.png'))
                enemies[-1].rotate(
                    int((math.atan2(400 - enemies[-1].x, 300 - enemies[-1].y)) * 360 / (math.pi * 2)) - 90)
            elif random.randint(1, 8) == 6:
                enemies.append(gamebox.from_image(random.randrange(800, 1000), random.randrange(200, 400), 'New Piskel.png'))
                enemies[-1].rotate(
                    int((math.atan2(400 - enemies[-1].x, 300 - enemies[-1].y)) * 360 / (math.pi * 2)) - 90)
            elif random.randint(1, 8) == 7:
                enemies.append(gamebox.from_image(random.randrange(800, 1000), random.randrange(600, 800), 'New Piskel.png'))
                enemies[-1].rotate(
                    int((math.atan2(400 - enemies[-1].x, 300 - enemies[-1].y)) * 360 / (math.pi * 2)) - 90)
            elif random.randint(1, 8) == 8:
                enemies.append(gamebox.from_image(random.randrange(300, 500), random.randrange(600, 800), 'New Piskel.png'))
                enemies[-1].rotate(
                    int((math.atan2(400 - enemies[-1].x, 300 - enemies[-1].y)) * 360 / (math.pi * 2)) - 90)


        for i in enemies:
            i.move(5*(400-i.x)/(math.sqrt((400-i.x)*(400-i.x) +(300-i.y)*(300-i.y))), 5*(300-i.y)/(math.sqrt((400-i.x)*(400-i.x)+(300-i.y)*(300-i.y))))

        camera.draw(background)
        camera.draw(player)
        for i in arrayOfBullets:
            camera.draw(i[0])

        for i in enemies:
            camera.draw(i)
        for i in arrayOfCoins:
            camera.draw(i)

        if hp == 1:
            camera.draw(health[0])
        if hp == 2:
            camera.draw(health[0])
            camera.draw(health[1])
        if hp == 3:
            camera.draw(health[0])
            camera.draw(health[1])
            camera.draw(health[2])

        camera.draw(gamebox.from_text(600, 30, "Coins: " + str(numberOfCoins), 30, 'Yellow'))
        camera.draw(gamebox.from_text(700, 30, "Score: " + str(score), 30, 'green'))

        camera.draw(flag)
        camera.draw(gamebox.from_text(500, 570, "Press Space to upgrade gun or restore hp", 30, "red"))
        camera.display()

    if (game == False) and (Lost == True):
        camera.draw(gamebox.from_text(400, 300, 'You lost! Press Space to exit.', 40, "red"))
        camera.draw(gamebox.from_text(400, 350, 'Score: '+str(score), 40, "green"))
        camera.display()
        if pygame.K_SPACE in keys:
            Lost = False
            StartOfTheGame = True

            stream = open("HighScores.txt", "r")
            highscores = stream.readlines()
            scores_to_compare = []
            for i in highscores:
                scores_to_compare.append(i.split())

            NewHS = False
            try:
                for i in range (0, len(scores_to_compare)):
                    if (score > int(scores_to_compare[i][2])) and (NewHS == False):
                        for j in range (len(scores_to_compare)-1, i, -1):
                            scores_to_compare[j][2]=scores_to_compare[j-1][2]
                        scores_to_compare[i][2] = str(score)
                        NewHS = True
            except:
                x = None

            stream.close()
            if NewHS == True:
                stream = open("HighScores.txt", "w")
                for i in range(0, len(scores_to_compare)):
                    scores_to_compare[i] = scores_to_compare[i][0]+' '+scores_to_compare[i][1]+' '+scores_to_compare[i][2]
                    stream.write(scores_to_compare[i]+'\n')
                stream.close()
                NewHS = False

    if (game == False) and (interfaceForUpgrades == True):
        if delayForInterface < 30:
            delayForInterface += 1
        if (pygame.K_SPACE in keys) and (delayForInterface >= 30):
                game = True
                interfaceForUpgrades = False
                delayForInterface = 0

        if (pygame.K_e in keys) and (numberOfCoins>=gun_price):
            bullet_speed *= 2
            numberOfCoins = numberOfCoins - gun_price
            gun_price *= 2
            camera.draw(gamebox.from_text(400, 150, "Speed of the bullet was doubled! Press Space to exit.", 20, "red"))

        if pygame.K_r in keys:
            if hp<3 and numberOfCoins>=hp_price:
                hp+=1
                numberOfCoins = numberOfCoins - hp_price
                hp_price *= 2
                camera.draw(gamebox.from_text(400, 150, "1 hp was restored! Press Space to exit.", 20, "red"))

            if hp>=3 and numberOfCoins>=hp_price:
                camera.draw(gamebox.from_text(400, 150, "You already have maximum hp! Press Space to exit.", 20, "red"))

        camera.draw(gamebox.from_image(400, 300, 'interfaceForUpgrades.png'))
        camera.draw(gamebox.from_text(300, 375, str(gun_price), 20, "yellow"))
        camera.draw(gamebox.from_text(450, 375, str(hp_price), 20, "yellow"))
        camera.display()

ticks_per_second = 30
# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)