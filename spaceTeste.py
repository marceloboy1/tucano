from random import randint
from time import sleep
import pygame, threading
import sys
import pygame.sprite as sprite
from player import *

class MainGame(object):
    """The Main Game Class - This class handles the main 
    initialization and creating of the Game."""
    
    def __init__(self, width=600,height=900):
 
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.lives = 3
 
        
    def Message(self, text, color, loc, size):
        
     
    	self.font = pygame.font.Font(None, size)
        self.text = self.font.render(text, 1, (color))
        #self.text.rect = (660,300)
        #self.textpos = self.text.get_rect()
        #self.textpos.rect = (600,300)
        self.screen.blit(self.text, (loc))
        
    def LoadSprites(self):
        #ADD ALL SPRITES HERE WITH THEIR GROUPS
        print planes_list
        self.ship = Player(300, 600, planes_list, all_sprites_list, self.lives)
        #clouds_list.add(clouds)
        all_sprites_list.add(self.ship)
        
        
        
    def SpriteUpdate(self):
        
        """ This update all sprite lists in the game"""
        #all_sprites_list.update()
        #planes_list.update()
        bullet_list.update()
        clouds_list.update()
        enemy_list.update()
        enemy_bullet_list.update()
        bg.update()
        self.ship.update(x_change, y_change, enemy_bullet_list)
        #cl.update()
 
 
    def MainLoop(self):
        
        
        """This is the Main Loop of the Game"""
        global x_pos, y_pos, x_change, y_change, velocity, bg_pos, dificulty, playing, reset, shooting, score, lives
        
        #Load all sprites
        self.LoadSprites()

        
        
        #Creates the multi threading components and starts them for timing
        if reset == False:
        
            e_thread = threading.Thread(target=e.enemy, args=([dificulty]))
            b_thread = threading.Thread(target=e.bullet, args=([dificulty]))
            c_thread = threading.Thread(target=e.cloud, args=([dificulty]))
            pb_thread = threading.Thread(target=e.player_bullet, args=())
            e_thread.start()
            b_thread.start()
            c_thread.start()
            pb_thread.start()
        
        #MAIN LOOP, read every frame until GAME OVER
        while self.ship.GameOver() == False:
           
                        
             #KEYBOARD MAPPING
            for event in pygame.event.get():
                
                #FOR QUIT
                if event.type == pygame.QUIT: 
                    playing = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        playing = False
                        pygame.quit()
                        quit()
                        
                #FOR CONTINUE
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.Reset()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -8

                    elif event.key == pygame.K_RIGHT:
                        x_change = +8
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                       
                        
                # Y Axis Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        y_change = -5
                        #velocity = 2
                    elif event.key == pygame.K_DOWN:
                        y_change = +5
                        #velocity = 0.5
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        y_change = 0
        
            

                        #velocity = 1
        
                #SHOOTING
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        shooting = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        shooting = False
                    
                        #       BULLET 1
                        # bullet = Bullet()
                        # bullet.rect.x = x_pos + 5
                        # bullet.rect.y = y_pos
                            
                  #      adding bullet1 1 to the lists
                        # all_sprites_list.add(bullet)
                        # bullet_list.add(bullet)
                               
                   #     BULLET 2
                        # bullet = Bullet()
                        # bullet.rect.x = x_pos + 50
                        # bullet.rect.y = y_pos
                         
                    #    adding bullet 2 to the lists
                        # all_sprites_list.add(bullet)
                        # bullet_list.add(bullet)
            
            
            
            for bullet in bullet_list:
            #Removes the bullet if it goes of the screen
                if bullet.rect.y < -10:
                    bullet.kill()
                    
                #Check for bullet hitting enemy planes
                enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
                for enemy in enemy_hit_list:
                    score += 10
                    bullet.kill()
                    enemy.kill()
            

            #Draw all sprites and update them (EVERY FRAME)
            all_sprites_list.draw(self.screen)
            planes_list.draw(self.screen)
            bullet_list.draw(self.screen)
            #clouds_list.draw(self.screen)
            enemy_list.draw(self.screen)
            enemy_bullet_list.draw(self.screen)
            self.ship.render(self.screen)
            self.Message("SCORE: ", black, (30, 30), 36)
            self.Message(str(score), yellow, (150, 30), 36)
            self.Message("PLANES: ", black, (430, 30), 36)
            self.Message(str(self.lives),yellow, (540, 30), 36)            
            pygame.display.flip()
            self.clock.tick(60)
            self.SpriteUpdate()

  
        
        while True: 
            
             #KEYBOARD MAPPING
            for event in pygame.event.get():
                
                #FOR QUIT
                if event.type == pygame.QUIT: 
                    playing = False
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        playing = False
                        pygame.quit()
                        quit()
                        
                        #Draw all sprites and update them (EVERY FRAME)
            all_sprites_list.draw(self.screen)
            planes_list.draw(self.screen)
            bullet_list.draw(self.screen)
            #clouds_list.draw(self.screen)
            enemy_list.draw(self.screen)
            enemy_bullet_list.draw(self.screen)
            self.ship.render(self.screen)
            self.Message("SCORE: ", black, (30, 30), 36)
            self.Message(str(score), yellow, (150, 30), 36)
            self.Message("PLANES: ", black, (430, 30), 36)
            self.Message(str(self.lives), yellow, (540, 30), 36)  
            self.Message("GAME OVER!!!", red, (50, 450), 100)
            
            
            pygame.display.flip()
            self.clock.tick(60)
            self.SpriteUpdate()
  
    def Reset(self):
        
        
        global x_pos, y_pos, x_change, y_change, velocity, bg_pos, reset, playing
        print "All sprites ", all_sprites_list
        print "Planes ", planes_list
        print "Enemy bullets ",enemy_bullet_list
        print "Bullets ",bullet_list
        print "Enemys ",enemy_list
        

        for sprite in all_sprites_list:
            sprite.kill()
        
        reset = True
        velocity = 1
        x_pos = 300 #largura
        y_pos = 600 #altura
        x_change = 0   
        y_change = 0   
        self.lives -=1
        #bg_pos = -5800
        #clouds_pos = -5800
        
        self.MainLoop()

class Background(object):
    """This is our background class, and the velocity"""
    
    def __init__(self):

        
        self.image = pygame.image.load('bg_img3.png')
        self.background_size = self.image.get_size()
        self.background_rect = self.image.get_rect()
        
        #seta w e h com o tamanho do background
        self.w,self.h = self.background_size 
        self.x = 0
        self.y = 0

        #seta o segundo background
        self.x1 = 0
        self.y1 = -self.h

        
    def update(self):
        global velocity
        self.y1 += velocity
        self.y += velocity
        
        Game.screen.blit(self.image,(self.x,self.y))
        Game.screen.blit(self.image,(self.x1,self.y1))
        
        # se o background estiver na posicao menor q a altura, ele volta ao comeco
        if self.y > self.h:
            self.y = -self.h
        if self.y1 > self.h:
            self.y1 = -self.h
            
class Clouds(pygame.sprite.Sprite):
    """This is clouds class, and the velocity"""
    
    def __init__(self):
        self.images = [pygame.image.load('cloud_1.png'),
                       pygame.image.load('cloud_2.png'),
                       pygame.image.load('cloud_3.png'),
                       pygame.image.load('cloud_4.png'),
                       pygame.image.load('cloud_5.png'),
                       pygame.image.load('cloud_6.png'),
                       pygame.image.load('cloud_7.png'),
                       pygame.image.load('cloud_8.png'),
                       pygame.image.load('cloud_9.png'),
                       pygame.image.load('cloud_10.png'),
                       pygame.image.load('cloud_11.png'),
                       pygame.image.load('cloud_12.png'),
                       pygame.image.load('cloud_13.png'),
                       pygame.image.load('cloud_14.png'),
                       pygame.image.load('cloud_15.png'),
                       pygame.image.load('cloud_16.png')]
                       
                       
                       
                       
        self.x = -200
        self.y = -200
        pygame.sprite.Sprite.__init__(self) 
        self.image = self.images[randint(10,15)]
        self.clouds_size = self.image.get_size()
        self.rect = self.image.get_rect()
        
        #seta w e h com o tamanho das nuvens
        self.w,self.h = self.clouds_size 
        self.x = randint(0,600)
        self.y = -200

        
    def update(self):
        self.y += 3
        self.rect = (self.x,self.y,self.w,self.h)
            
class Bullet(pygame.sprite.Sprite):
    
    """ This class makes the bullets and update them"""
    
    def __init__(self):
       
        self.color = yellow
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([2,8])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y -= 12
        
class Enemy(pygame.sprite.Sprite):
    """This is our player Class, makes it moves in the sky"""
    def __init__(self):
        

        self.x_pos = randint(50,550)
        self.y_pos = randint(-300,0)
        
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load('mig29.png')
        self.rect = (self.x_pos,self.y_pos,59,57)
        
    def update(self):
        
        self.y_pos += velocity + 4
        self.rect = (self.x_pos, self.y_pos, 59, 57)
        
class EnemyBullet(Bullet):
    
    def update(self):
        self.rect.y += 10

class Create(object):
    global playing
    global shooting
    
    '''This class creates multi thread sprites
    
        USAGE: 
        First create an instance as for exemple: enenmy = Create()
        Then you create an instance for the threading, example: enemy_thread = threading.Thread(target = enemy.enemy, args ([10]))
        where target is the function (in this case enemy function of the enemy intance of the Create Class, passing the number ten as argument)
        '''
    
    #ENEMY (change the sleep value for more enemys, the less the number is, more enemys will apear)
    def enemy(self, time):
        while playing == True:
            
            #use this variable to control the amount of enemys
            self.time = time
            
            #Creates the enemys
            if len(enemy_list) < 30:
                self.enemy1 = Enemy()
                all_sprites_list.add(self.enemy1)
                enemy_list.add(self.enemy1)
            
            #this remove the enemys from every list if it goes off the screen
            for enemy in enemy_list:
                if enemy.rect[1] > 900:
                    #enemy_list.remove(enemy)
                    #all_sprites_list.remove(enemy)
                    enemy.kill()
            # Enemy creating interval
            sleep((float(self.time)) * 2)
    
    #Bullets (change the sleep value for more bullets, the less the number is, faster is the fire rate)
    def bullet(self, time):
        self.time = time
        while playing == True:
            
            #Create bullets for all enemys
            for enemy in enemy_list:
                
                enemy_bullet = EnemyBullet()
                enemy_bullet.rect.x = enemy.rect[0] + enemy.rect[3] / 2
                enemy_bullet.rect.y = enemy.rect[1] + 57
                all_sprites_list.add(enemy_bullet)
                enemy_bullet_list.add(enemy_bullet)
     
            #this remove the enemys from every list if it goes off the screen   
            for enemy_bullet in enemy_bullet_list:
                if enemy_bullet.rect.y > 900:
                    #enemy_bullet_list.remove(enemy_bullet)
                    #all_sprites_list.remove(enemy_bullet)
                    enemy_bullet.kill()
           
            #Fire rate
            sleep((float(self.time)) * 1.5)
            
    
    def player_bullet(self):
        
        self.time = 1
        while playing == True:
            
            while shooting == True:    
            
                #BULLET 1
                bullet = Bullet()
                bullet.rect.x = Game.ship.rect[0] + 5
                bullet.rect.y = Game.ship.rect[1]
                 
                #adding bullet1 1 to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                            
                #BULLET 2
                bullet = Bullet()
                bullet.rect.x = Game.ship.rect[0] + 50
                bullet.rect.y = Game.ship.rect[1]
                         
                #adding bullet 2 to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
                    
                sleep(0.15)
            
            
            #this remove the enemys from every list if it goes off the screen   
                for bullet in bullet_list:
                    if bullet.rect.y < 0:
                    #enemy_bullet_list.remove(enemy_bullet)
                    #all_sprites_list.remove(enemy_bullet)
                        bullet.kill()
                        
            
    
    def cloud(self, time):
        while playing == True:
            
            #use this variable to control the amount of enemys
            self.time = time
            
            #Creates the enemys
            if len(clouds_list) < 30:
                self.cloud = Clouds()
                all_sprites_list.add(self.cloud)
                clouds_list.add(self.cloud)
            
            #this remove the enemys from every list if it goes off the screen
            for cloud in clouds_list:
                if cloud.rect[1] > 900:
                    cloud.kill()
            # Enemy creating interval
            sleep(2)
    
            
#VARIABLES

dificulty = 1
playing = True
shooting = False
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
velocity = 1
x_pos = 300 #largura
y_pos = 600 #altura
x_change = 0   
y_change = 0   
bg_pos = -5800
clouds_pos = -5800
reset = False
score = 000


#INSTANCES
all_sprites_list = pygame.sprite.Group()
planes_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
clouds_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
enemy_bullet_list = pygame.sprite.Group()
e = Create()
bg = Background()


#RUNS THE GAME

dificulty = raw_input("Choose the dificulty (1: Hard / 2: Medium / 3: Easy) >>>")

if __name__ == "__main__":
    Game = MainGame()
    Game.MainLoop()

