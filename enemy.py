import pygame

RED = (255, 0, 0)
GREEN = (0,100,0)

class Enemy:

    #The images of enemy
    enemy_left = [pygame.image.load("images/enemy/L1E.png"),pygame.image.load("images/enemy/L2E.png"),
                   pygame.image.load("images/enemy/L3E.png"),pygame.image.load("images/enemy/L4E.png"),
                   pygame.image.load("images/enemy/L5E.png"),pygame.image.load("images/enemy/L6E.png"),
                   pygame.image.load("images/enemy/L7E.png"),pygame.image.load("images/enemy/L8E.png")]

    enemy_right = [pygame.image.load("images/enemy/R1E.png"),pygame.image.load("images/enemy/R2E.png"),
                   pygame.image.load("images/enemy/R3E.png"),pygame.image.load("images/enemy/R4E.png"),
                   pygame.image.load("images/enemy/R5E.png"),pygame.image.load("images/enemy/R6E.png"),
                   pygame.image.load("images/enemy/R7E.png"),pygame.image.load("images/enemy/R8E.png")]


    def __init__ (self, x ,y , w , h, end):
        self.x = x  #X-Coordination of Enemy
        self.y = y  #y-Coordination of Enemy
        self.w = w  #Heigh of Enemy
        self.h = h  #Width of Enemy
        self.end = end
        self.start = x
        self.step = 3
        self.moves = 0
        self.hitbox = (self.x, self.y, self.w, self.h) #Tupple (hitting frame)
        self.health = 10
        self.visible = True


    def draw (self, screen):
        if self.visible:
            self.move(screen)
            if self.step <0:
               # enemy = pygame.transform.scale(self.hero_left[self.moves], (self.w, self.h))
                screen.blit(self.enemy_left[self.moves], (self.x, self.y))
                self.moves += 1
                if self.moves == 7:
                    self.moves = 0

            else:
                #enemy = pygame.transform.scale(self.enemy_right[self.moves], (self.w, self.h))
                screen.blit(self.enemy_right[self.moves], (self.x, self.y))
                self.moves += 1
                if self.moves == 7:
                    self.moves = 0

            #Enemy Health Bar
            pygame.draw.rect (screen, RED,(self.hitbox[0], self.hitbox[1]-15, 50 , 10))
            pygame.draw.rect (screen, GREEN,(self.hitbox[0], self.hitbox[1]-15, self.health * 5, 10))


    def move(self,screen):
        global RED
        self.hitbox = (self.x+15 , self.y, self.w-25, self.h)
        #pygame.draw.rect(screen, RED, self.hitbox, 2)
        if self.step > 0 :
           if self.x + self.step > self.end:
                self.step *=-1      #Change direction of enemy
           else:
               self.x += self.step

        else:
            if self.x - self.step < self.start:
                self.step *=-1

            else:
                self.x += self.step

    #Bullet hit the enemy
    def hit(self, hit_sound):
        self.health -=1
        hit_sound.play()
        if self.health ==0:
            self.visible = False
            self.hitbox = (0,0,0,0)

