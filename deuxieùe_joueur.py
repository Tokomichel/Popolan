import pygame
from math import sqrt as racine

class Deuxieme_joueur(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.point_de_vie=130
        self.game=game
        self.max_point_de_vie=130
        self.vitesse=6
        self.image=pygame.image.load("image/marche.bmp")
        self.rect=self.image.get_rect()
        self.rect.y=250
        self.rect.x=100
        self.saut=False
        self.hauteur_saut=20


    def jump(self):
        if self.saut is True:
            self.rect.y-=self.hauteur_saut
            self.hauteur_saut-=1
            if self.hauteur_saut < -20:
                self.saut=False
                self.hauteur_saut=20
    def distance(self,rect,x,y):
        carre1=(rect.x-x)*(rect.x-x)
        carre2=(rect.y-y)*(rect.y-y)
        somme=carre1+carre2
        distance=racine(somme)
        return distance
    def direction(self):
        distance_joueur1=self.distance(self.game.player.rect,950,250)
        distance_joueur2=self.distance(self.rect,950,250)
        if distance_joueur1<distance_joueur2:
            return True
        else:
            return False






    def deplacement(self,direction):

          droite=self.direction()


          if direction:
             #vers la droite
             if droite is False:
               self.rect.x+=self.vitesse
             else:
                  if not self.game.check_collision(self, self.game.group_joueur):
                      self.rect.x+=self.vitesse
          else:
              #vers la gauche
              if droite is True:
                self.rect.x-=self.vitesse
              else:
                  if not self.game.check_collision(self, self.game.group_joueur):
                      self.rect.x-=self.vitesse


