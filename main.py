"""
------------This Game was made by Ahmad Abdelbaset-------------
For any issue or any question, I will be glad to help,
linkedin:  https://il.linkedin.com/in/ahmadabdelbaset
Email: ahmad.abdelbaset@outlook.com

"""

import pygame
from player import Player
from bullet import Bullet
from enemy import Enemy

#Check if Pygame initiated correctly
sucess, fail = pygame.init()
print(sucess,fail)


#Screen Settings
screenWidth = 800
screenHeight = 550
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Ahmad's City")
bg = pygame.image.load("images/bg.jpg") #Background Image
bg = pygame.transform.scale(bg, (screenWidth, screenHeight)) #Change the dimensions of the game to fit the screen
font = pygame.font.SysFont("comicsans",20,True) #(Font name, Size, Bold)


#Used Colors
RED = (255,0,0)
BLACK = (255,255,255)


#Creat Instances of the game characters
man = Player(700,400,100,100)
enemy = Enemy (100,400,64,64,620)

#Sounds used in the game
bullet_sound = pygame.mixer.Sound("sounds/bullet.wav")
hit_sound = pygame.mixer.Sound("sounds/hit.wav")


score = 0 #The initial score
clock = pygame.time.Clock() #For layers and movements
bullets = [] #The list of bullets


"""This function used to show the elements"""
def redraw_game ():
    global moves

    screen.blit(bg,(0,0))  #Add background image to the screen
    text = font.render("Score = " + str(score),20,True, BLACK)
    screen.blit(text,(screenWidth/2 - 50, 20))#Add scores to the screen

    #pygame.draw.rect(screen,RED,(x,y,w,h)) #For Rectanle object   #This is the fame of the man (you can see it if you remove the '#')
    #screen.blit(hero,(x,y)) # same image of hero    #To show image

    #To show the man and the enemy on the screen
    man.draw(screen)
    enemy.draw(screen)

    #To show the bullets on the screen
    for bullet in bullets:
        bullet.draw(screen)

    #To update the screen after each change
    pygame.display.update()


"""Loop will keep running during the game"""
while True:
    clock.tick(30)

    #To decide the frame of the man (used to check if the man touched the enemy)
    x_mid = (man.hitbox[0] + man.hitbox[0] + man.hitbox[2]) //2
    y_mid = (man.hitbox[1] + man.hitbox[1] + man.hitbox[3]) //2

    if  enemy.hitbox[0] < x_mid  < enemy.hitbox[0] + enemy.hitbox[2]:
        if enemy.hitbox[1] < y_mid  < enemy.hitbox[1] + enemy.hitbox[3]:
            score -=5    #If man touched the enemy, will lose 5 points from the score
            man.hit(screen, screenWidth)


    """------- Keys and events ------------"""
    for event in pygame.event.get():


        if event.type == pygame.QUIT:         # When user click [X], close the game
            quit()

        if event.type == pygame.KEYDOWN:    #When user press on a key
            if event.key == pygame.K_s:
                if len(bullets) < 5:        #The user can shoot 5 bullets maximum
                    bullet_sound.play()     #Sound

                    # The direction of the bullet
                    if man.idle_to_left:
                        direction = -1
                    else:
                        direction = 1

                    #This will create a bullet and add it to the list and will be shooted from the center of man
                    bullets.append(Bullet(round(man.x + man.w // 2), round(man.y + man.h // 2), 5, RED, direction, 10))

    keys = pygame.key.get_pressed()

    #Check if the bullet touched the enemy
    for bullet in bullets:
        if bullet.x >enemy.hitbox[0] and bullet.x < enemy.hitbox[0] + enemy.hitbox[2]:
            if bullet.y > enemy.hitbox[1] and bullet.y < enemy.hitbox[1] + enemy.hitbox[3]:
                bullets.remove(bullet)
                enemy.hit(hit_sound)
                score +=1

        #Bullet movement and range
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.step
        else: bullets.remove(bullet)


    """---------------------------- Man Movement ---------------"""
    if keys[pygame.K_LEFT] and man.x-man.step >= 0:
        man.x -= man.step
        man.left = True
        man.right = False
        man.idle_to_left= True

    elif keys[pygame.K_RIGHT] and man.x+ man.step < screenWidth:
        man.x += man.step
        man.left = False
        man.right = True
        man.idle_to_left= False

    else:
        man.left = False
        man.right = False
        man.moves = 0

    if not man.isJump:
        if keys[pygame.K_UP] and man.y-man.step >= 0:
            man.y -= man.step
        if keys[pygame.K_DOWN] and man.y+ man.step < screenHeight:
            man.y += man.step
        if keys[pygame.K_SPACE]:
            man.isJump = True

    else:

        if man.speed >= man.neg_speed:
            neg = 1
            if man.speed < 0:
                neg = -1
            man.y -= (man.speed ** 2) * 0.25 * neg #Equation of jumping
            man.speed -= 1

        else:
            man.isJump = False
            man.speed = 10

    redraw_game()


