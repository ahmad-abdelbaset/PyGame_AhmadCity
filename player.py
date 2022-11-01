import pygame

RED = (255, 0, 0)

class Player():

    #Images of Hero
    hero_right = [pygame.image.load("images/hero/Walk (1).png"), pygame.image.load("images/hero/Walk (2).png"),
                  pygame.image.load("images/hero/Walk (3).png"), pygame.image.load("images/hero/Walk (4).png"),
                  pygame.image.load("images/hero/Walk (5).png"), pygame.image.load("images/hero/Walk (6).png"),
                  pygame.image.load("images/hero/Walk (7).png"), pygame.image.load("images/hero/Walk (8).png"),
                  pygame.image.load("images/hero/Walk (9).png"), pygame.image.load("images/hero/Walk (10).png"),
                  pygame.image.load("images/hero/Walk (11).png"), pygame.image.load("images/hero/Walk (12).png"),
                  pygame.image.load("images/hero/Walk (13).png"), pygame.image.load("images/hero/Walk (14).png"),
                  pygame.image.load("images/hero/Walk (15).png")]

    hero_left = [pygame.image.load("images/hero/Walk (1l).png"), pygame.image.load("images/hero/Walk (2l).png"),
                 pygame.image.load("images/hero/Walk (3l).png"), pygame.image.load("images/hero/Walk (4l).png"),
                 pygame.image.load("images/hero/Walk (5l).png"), pygame.image.load("images/hero/Walk (6l).png"),
                 pygame.image.load("images/hero/Walk (7l).png"), pygame.image.load("images/hero/Walk (8l).png"),
                 pygame.image.load("images/hero/Walk (9l).png"), pygame.image.load("images/hero/Walk (10l).png"),
                 pygame.image.load("images/hero/Walk (11l).png"), pygame.image.load("images/hero/Walk (12l).png"),
                 pygame.image.load("images/hero/Walk (13l).png"), pygame.image.load("images/hero/Walk (14l).png"),
                 pygame.image.load("images/hero/Walk (15l).png")]

    def __init__(self, x , y , w , h):

        self.x = x  #X-Coordination (relative to the (0,0) of the screen)
        self.x_start= x #The initail starting x-point (player will back to this point)
        self.y = y  #The initail starting x-point (player will back to this point)
        self.y_start = y    #Y-Coordination (relative to the (0,0) of the screen)
        self.w = w  #Width of Hero
        self.h = h  #Heigh of Hero
        self.step = 5   #Walking Steps
        self.left = False
        self.right = False
        self.moves = 0
        self.speed = 10    #Speed of Jumping
        self.isJump= False
        self.idle_to_left = False
        self.neg_speed = -1 *(self.speed)
        self.hitbox= (self.x,self.y,self.w / 2,self.h)

        #Images when idle
        self.hero_idle_right = pygame.image.load("images/hero/Idle (1).png")
        self.hero_idle_right = pygame.transform.scale(self.hero_idle_right, (self.w,self.h))

        self.hero_idle_left = pygame.image.load("images/hero/Idle (1l).png")
        self.hero_idle_left = pygame.transform.scale(self.hero_idle_left, (self.w, self.h))

    def draw (self,screen):
        global RED

        if self.left:

            #Note: This Player is not in the middle of the image, so frame dimensions different according to direction
            self.hitbox = ((self.x + self.w/2), self.y, self.w / 2, self.h)
            hero = pygame.transform.scale(self.hero_left[self.moves], (self.w, self.h)) #Fit image sizw
            screen.blit(hero, (self.x, self.y))
            hero = pygame.transform.scale(hero, (self.w, self.h))
            self.moves += 1
            if self.moves == 14:
                self.moves = 0

        elif self.right:
            self.hitbox = (self.x, self.y, self.w / 2, self.h)
            hero = pygame.transform.scale(self.hero_right[self.moves], (self.w, self.h))
            screen.blit(hero, (self.x, self.y))
            self.moves += 1
            if self.moves == 14:
                self.moves = 0

        elif self.idle_to_left:
            screen.blit(self.hero_idle_left, (self.x, self.y))

        else:
            screen.blit(self.hero_idle_right, (self.x, self.y))

        #pygame.draw.rect(screen, RED, self.hitbox,2)

    #When Enemy Touch the Hero
    def hit(self,screen,screenWidth):
        self.isJump = False
        self.speed = 10
        self.x = self.x_start
        self.y = self.y_start
        if self.right:
             self.hitbox = (self.x, self.y, self.w / 2, self.h)
        else:
            self.hitbox = ((self.x + self.w / 2), self.y, self.w / 2, self.h)

        self.moves = 0
        font = pygame.font.SysFont("conicsans",80)
        text = font.render("-5",1,RED)
        screen.blit(text,(screenWidth//2 - 1, 200))
        pygame.display.update()

        i=0
        while i<50:
            i += 1
            pygame.time.delay(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
