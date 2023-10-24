import pygame
from projectile import projectile
from projectile import gros_projectile
from projectile import button
from super_comb import Grande_attaque


class joueur(pygame.sprite.Sprite):
    
    def __init__(self,game):
        super().__init__()
        self.point_de_vie = 130
        self.max_point_de_vie = 130
        self.game = game
        self.droite = True
        self.attaque_super = Grande_attaque(self.game)
        self.vitesse = 6
        self.coup_critique = 0
        self.super_combo = False
        self.lancement_combo = False
        self.max_coup_critique = 130
        self.group_projectiles = pygame.sprite.Group()
        self.groupe_boutton = pygame.sprite.Group()
        # self.image = pygame.image.load("image/player.png")
        self.image = pygame.transform.scale(pygame.image.load("image/player.png"),(165,165))
        self.sound = pygame.mixer.Sound("assets/sounds/tir.ogg")

        self.rect = self.image.get_rect()
        self.rect.y = 217
        self.rect.x = 400
        self.x = self.rect.x+45
        self.y = self.rect.y+45
        self.saut = False
        self.vitesse_saut = 20
        self.frame = 1
        self.operation_coup_de_poing = False
        self.liste_image = self.remplissage()

    def remplissage(self):
        liste_image = list()
        frame = 0
        while frame <= 23:
            liste_image.append(pygame.image.load("assets/player/player" + str(frame+1) + ".png"))
            liste_image[frame] = pygame.transform.scale(liste_image[frame],(165,165))
            frame += 1
        return liste_image

    def animation_coup_de_poing(self):
        if self.operation_coup_de_poing is True:
            self.image = self.liste_image[self.frame]
            self.frame += 1
            if self.frame == 23:
                self.frame = 1
                self.operation_coup_de_poing = False

    def boutton_combo(self):
        if self.coup_critique >= 130:
            self.groupe_boutton.add(button(self))
        elif self.coup_critique <= 130 :
            self.groupe_boutton.remove(button(self))

    def direction(self):
        distance_joueur1=self.game.player2.distance(self.rect,950,250)
        distance_joueur2=self.game.player2.distance(self.game.player2.rect,950,250)
        if distance_joueur1<distance_joueur2:
            return True
        else:
            return False

    def vers_la_droite(self):
        self.droite=True
        droite=self.direction()
        if droite :
          if not self.game.check_collision(self, self.game.groupe_cheban):
             self.rect.x += self.vitesse
          else:
            self.point_de_vie -= self.game.monstre.point_attaque
        else:
            if not self.game.check_collision(self,self.game.groupe_player2):
                if not self.game.check_collision(self, self.game.groupe_cheban):
                    self.rect.x += self.vitesse
                else:
                    self.point_de_vie -= self.game.monstre.point_attaque


    def vers_la_gauche(self):
        self.droite=False
        droite = self.direction()
        if droite:
            if not self.game.check_collision(self, self.game.groupe_player2):
             self.rect.x -= self.vitesse
        else:
            self.rect.x -= self.vitesse

    def jump(self):
        if self.saut is True:
            self.rect.y-=self.vitesse_saut
            self.vitesse_saut-=1
            if self.vitesse_saut < -20:
                self.saut=False
                self.vitesse_saut=20





    def lancement(self,combo):

       self.boutton_combo()
       if combo==True:
           self.group_projectiles.add(gros_projectile(self))
           self.coup_critique=0
       else:
           self.group_projectiles.add(projectile(self))


    def barre_de_vie(self,surface):
        barre_color=(0,255,0)
        barre_position=(self.rect.x+2,self.rect.y-12,self.point_de_vie,5)
        pygame.draw.rect(surface,barre_color,barre_position)

    def barre_max_de_vie(self,surface):
        barre_color=(54,68,53)
        barre_position=(self.rect.x+2,self.rect.y-12,self.max_point_de_vie,5)
        pygame.draw.rect(surface,barre_color,barre_position)

    def barre_coup_critique(self,surface):
        barre_color = (16,123,220)
        barre_position=(self.rect.x+2,self.rect.y-5,self.coup_critique,5)

        # donnees de la barre arriere grise

        barre_grise_color=(86,99,95)
        barre_grise_position=(self.rect.x+2,self.rect.y-5,self.coup_critique,5)

        pygame.draw.rect(surface,barre_grise_color,barre_grise_position)
        pygame.draw.rect(surface,barre_color,barre_position)


    def Game_over(self):
        self.coup_critique = 0
        self.super_combo = False
        self.lancement_combo = False
        self.game.groupe_cheban=pygame.sprite.Group()
        self.game.lancement_cheban()
        self.game.lancement_cheban()
        self.game.score=0
        self.point_de_vie=self.max_point_de_vie
        self.game.game_on=False
        self.rect.y = 217
        self.rect.x = 400












