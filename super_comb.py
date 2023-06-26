import pygame


class Grande_attaque(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.jeu=game
        self.vitesse=10
        self.point_attaque = 25
        self.coup_critique = 0
        self.max_coup_critique = 130
        self.angle=0
        self.image = pygame.image.load("assets/projectile.png")
        self.image_originelle=pygame.image.load("assets/projectile.png")
        self.rect = self.image.get_rect()



    def deplacement(self):
       self.rect.x+=self.vitesse
       self.rotation()
       for monstre in self.jeu.check_collision(self,self.jeu.groupe_cheban ):
           monstre.point_de_vie-=self.point_attaque
           if self.rect.x>=800:
               self.jeu.player.group_projectiles.remove(self)

    def rotation(self):
        self.angle+=9
        self.image=pygame.transform.rotozoom(self.image_originelle,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)
