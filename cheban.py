import pygame
import random

vitesses=[0.5,0.6,0.9,1]
instanciation=["droite","gauche"]

class cheban(pygame.sprite.Sprite):

    def __init__(self,game):
        
        super().__init__()
        self.point_de_vie=100
        self.max_point_de_vie=100
        self.point_attaque=0.3
        self.frame=1
        self.instanciation=random.choice(instanciation)
        self.game=game
        self.direction_droite=False
        self.image=pygame.image.load("image/mummy.png")
        self.image.set_colorkey((255,255,255))
        self.image=pygame.transform.scale(self.image,(100,80))
        self.image_originelle= pygame.image.load("image/mummy.png")
        self.rect=self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 400)
        self.rect.y=250
        self.x = self.rect.x + 76
        self.y = self.rect.y + 117
        self.vitesse = 1
        self.image=pygame.transform.scale(self.image,(100,100))
        self.liste_image=self.chagement_liste()


    def chagement_liste(self):
        liste_image=list()
        frame=0
        while frame <= 23:
            liste_image.append(pygame.image.load("assets/mummy/mummy"+str(frame+1)+".png"))
            liste_image[frame]=pygame.transform.scale(liste_image[frame],(110,110))
            frame+=1
            # print(frame+4)
        return liste_image

    def dommage(self,damage):
       self.point_de_vie-=damage
       if self.point_de_vie<=0:
           self.game.groupe_cheban.remove(self)
           self.game.lancement_cheban()
       return 12

    def animation(self):

        self.image=self.liste_image[self.frame]
        if self.frame < 23:
         self.frame+=1
        else:
            self.frame=1

    def barre_de_vie(self,surface):
        barre_color=(217,9,14)
        barre_position=[self.rect.x+1,self.rect.y-15,self.point_de_vie,5]
        pygame.draw.rect(surface,barre_color,barre_position)

    def barre_max(self,surface):
        barre_position = [self.rect.x + 1, self.rect.y - 15, self.max_point_de_vie, 5]
        barre_color = (75, 78, 61)
        pygame.draw.rect(surface, barre_color, barre_position)

    def deplacer(self):
        self.animation()
        if not self.game.check_collision(self,self.game.group_joueur):
         self.rect.x -= self.vitesse

        elif self.game.check_collision(self,self.game.group_joueur):
            self.game.player.point_de_vie-=self.point_attaque
            if self.game.player.point_de_vie<=0:
               self.game.player.Game_over()


class Cheban_gauche(pygame.sprite.Sprite):


   def __init__(self,game):
     super().__init__()
     self.point_de_vie = 100
     self.max_point_de_vie = 100
     self.point_attaque = 0.3
     self.instanciation = random.choice(instanciation)
     self.game = game
     self.frame=1
     self.image = pygame.image.load("image/mummy.png")
     self.image.set_colorkey((255, 255, 255))
     self.image = pygame.transform.scale(self.image, (100, 80))
     self.image_originelle = pygame.image.load("image/mummy.png")
     self.rect = self.image.get_rect()
     self.rect.x = random.randint(0,50)
     self.rect.y = 250
     self.x = self.rect.x + 76
     self.y = self.rect.y + 117
     self.vitesse = 2
     self.image = pygame.transform.scale(self.image, (100, 100))
     self.liste_image=self.chargement_images()

   def chargement_images(self):
       liste_image = list()
       frame = 0
       while frame <= 23:
           print(frame)
           liste_image.append(pygame.image.load("assets/mummy/mummy" + str(frame + 1) + ".png"))
           liste_image[frame] = pygame.transform.scale(liste_image[frame], (110, 110))
           frame += 1
       return liste_image


   def animation(self):

       self.image = self.liste_image[self.frame]
       if self.frame < 23:
           self.frame += 1
       else:
           self.frame = 1

   def dommage(self, damage):
       self.point_de_vie -= damage
       if self.point_de_vie <= 0:
           self.game.groupe_cheban.remove(self)
           self.game.lancement_cheban()
       return 12

   def barre_de_vie(self, surface):
       barre_color = (217, 9, 14)
       barre_position = [self.rect.x + 1, self.rect.y - 15, self.point_de_vie, 5]
       pygame.draw.rect(surface, barre_color, barre_position)

   def barre_max(self, surface):
       barre_position = [self.rect.x + 2, self.rect.y - 15, self.max_point_de_vie+1, 6]
       barre_color = (75, 78, 61)
       pygame.draw.rect(surface, barre_color, barre_position)

   def deplacer(self):
       self.animation()
       if not self.game.check_collision(self, self.game.group_joueur):
           if self.rect.x <= 950:
            self.rect.x += self.vitesse


       elif self.game.check_collision(self, self.game.group_joueur):
           self.game.player.point_de_vie -= self.point_attaque
           if self.game.player.point_de_vie <= 0:
               self.game.player.Game_over()


