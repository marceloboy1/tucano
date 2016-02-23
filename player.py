import pygame



class Player(pygame.sprite.Sprite):

    """This is our player Class, makes it moves in the sky"""
    def __init__(self, x, y, planes_list, all_sprite_list, lives):
        
        self.lives = lives
        self.planes_list = planes_list
        self.all_sprite_list = all_sprite_list
        self.player_hit_list = pygame.sprite.Group()
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('f22.png')
        self.rect = (self.x,self.y,57,57)
        
        self.planes_list.add(self)
        self.all_sprite_list.add(self)
        
        
    def update(self, x_change, y_change, enemy_bullet_list):
        self.enemy_bullet_list = enemy_bullet_list
        self.x_change = x_change
        self.y_change = y_change
        self.x += self.x_change
        self.y += self.y_change
        self.rect = (self.x,self.y,57,57)
        self.colisions()
        
    def render(self, window):
    
        #window.blit(self.image,(self.x,self.y))
        pass
    def movement(self):
        pass

    
    def colisions(self):

        
        #SCREEN COLISIONS
        if self.x >= 540 or self.x < 0:
            self.x -= self.x_change
        if self.y >= 840 or self.y < 0:
            self.y -= self.y_change

        for bullet in self.enemy_bullet_list:
            
            self.player_hit_list = pygame.sprite.spritecollide(bullet, self.planes_list, True)
            for player in self.player_hit_list:
                self.planes_list.remove(player)
                self.lives -= 1
                print self.lives
                self.kill()
            
        
    def GameOver(self):
        if self.lives < 0:
            print "GAME OVER"
            return True
        else:
            print self.lives
            return False
                