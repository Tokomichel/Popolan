import pygame


class button(pygame.sprite.Sprite):
    def __init__(self,player):
      super().__init__()
      self.player=player
      self.image=pygame.image.load("image/OKI.bmp").convert()
      self.image=pygame.transform.scale(self.image,(30,30))
      self.rect=self.image.get_rect()
      self.rect.x=self.player.rect.x+50
      self.rect.y=self.player.rect.y-43

    def existance(self):
        self.rect.x = self.player.rect.x + 50
        self.rect.y = self.player.rect.y - 43
        if self.player.coup_critique<=130:
         self.player.groupe_boutton.remove(self)

class gros_projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.vitesse = 6
        self.attaque = 2
        self.angle = 0
        self.player = player
        self.direction=self.player.droite
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image_originelle=self.image
        self.rect = self.image.get_rect()
        if self.direction:
         self.rect.x = self.player.rect.x + 80
        else:
            self.rect.x=self.player.rect.x
        self.rect.y = self.player.rect.y + 20.5


    def rotation(self):
        self.angle -= 9
        self.image = pygame.transform.rotozoom(self.image_originelle, self.angle, 3)
        self.rect = self.image.get_rect(center=self.rect.center)

    def deplacement(self):
        self.player.boutton_combo()
        if self.direction:
         self.rect.x += self.vitesse
        else:
            self.rect.x-=self.vitesse
        self.rotation()
        for monstre in self.player.game.check_collision(self, self.player.game.groupe_cheban):
            monstre.dommage(self.attaque)
            self.player.game.score+=1
            print(self.player.game.score)
            if self.rect.x > 1000:
                self.player.group_projectiles.remove(self)



class projectile(pygame.sprite.Sprite):
    def __init__(self,player):
        super().__init__()
        self.vitesse=10
        self.player=player
        self.attaque=15
        self.direction=self.player.droite
        self.image=pygame.image.load("assets/projectile.png")
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect=self.image.get_rect()
        if self.direction:
            self.rect.x = self.player.rect.x + 80
        else:
            self.rect.x = self.player.rect.x
        self.rect.y=player.rect.y+20.5
        self.x = self.rect.x + 38
        self.y = self.rect.y + 12
        self.image_originelle=self.image
        self.angle=0
        self.lancement=True


    def rotation(self):
        self.angle+=15
        self.image=pygame.transform.rotozoom(self.image_originelle,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def deplacement(self):

        self.lancement=True
        if self.direction:
         self.rect.x += self.vitesse
        else:
            self.rect.x -= self.vitesse
        self.rotation()
        for monstre in self.player.game.check_collision(self,self.player.game.groupe_cheban):
         if self.rect.x >= monstre.rect.x-40:
          if self.player.coup_critique<=130:
             self.player.coup_critique+=monstre.dommage(self.attaque)
             self.player.game.score+=1
             print(self.player.game.score)
          else:
             monstre.dommage(self.attaque)
          self.player.group_projectiles.remove(self)


        if self.rect.x>1000:
            self.player.group_projectiles.remove(self)

    def deplacement_vers_la_gauche(self):
        self.rect.x-=self.vitesse
        self.rotation()







