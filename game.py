import random

import pygame
from class_joueur import joueur
from cheban import cheban
from cheban import Cheban_gauche
from deuxieùe_joueur import Deuxieme_joueur





class Game:
    
    def __init__(self):
        # est ce qu'on joue ?

        self.game_on = False
        self.intro = True
        self.ajout = True
        self.player = joueur(self)
        self.type_monstre = False
        self.score = 0
        self.niveau = 0
        self.group_joueur = pygame.sprite.Group()
        self.group_joueur.add(self.player)
        self.player2 = Deuxieme_joueur(self)
        self.groupe_player2=pygame.sprite.Group()

        self.groupe_cheban = pygame.sprite.Group()
        self.lancement_cheban()
        self.lancement_cheban()
        self.monstre = cheban(self)
        self.utilise = {}
        self.image_monstre_faible = pygame.image.load("image/projectile.png")
        self.image_monstre_faible = pygame.transform.scale(self.image_monstre_faible,(30,30))


    def evolution(self):
        if self.score>=10 and self.score<=20:
            self.niveau=1
            self.monstre.vitesse=2
            self.monstre2.vitesse=2
        elif self.score>=20 and self.score<=30:
            self.niveau=2

            if self.ajout is True:
             self.lancement_cheban()
            self.ajout=False
        elif self.score>=30 and self.score<=40:
            self.niveau=3

    def Jouer(self,ecran_de_fond,arriere_x,premier_joueur,deuxieme_joueur):


        ecran_de_fond.blit(self.player.image, self.player.rect)


        self.player.barre_max_de_vie(ecran_de_fond)
        self.player.barre_de_vie(ecran_de_fond)
        self.player.barre_coup_critique(ecran_de_fond)

        # dessinerles projectiles

        for projectile in self.player.group_projectiles:
            projectile.deplacement()

        for button in self.player.groupe_boutton:
            button.existance()

        for monstre in self.groupe_cheban:
            monstre.deplacer()
            monstre.barre_max(ecran_de_fond)
            monstre.barre_de_vie(ecran_de_fond)
            if monstre.point_de_vie<=30:
                ecran_de_fond.blit(self.image_monstre_faible,(monstre.rect.x+40,monstre.rect.y-30))


        self.player.group_projectiles.draw(ecran_de_fond)
        self.groupe_cheban.draw(ecran_de_fond)
        self.player.groupe_boutton.draw(ecran_de_fond)
        self.evolution()
        # deplacement

        # deplacement premier joueur
        while premier_joueur:

         if self.utilise.get(pygame.K_RIGHT):
            if self.player.rect.x >= 840:
                if arriere_x >= -1407:
                    arriere_x -=6
            else:

                self.player.vers_la_droite()

         elif self.utilise.get(pygame.K_LEFT):
            if self.player.rect.x <= 12 and arriere_x <= 2:
                arriere_x += 6

            else:
                if self.player.rect.x >= 10:
                    self.player.vers_la_gauche()

         premier_joueur=False
         deuxieme_joueur=True

        #deplacement deuxieme joueur
        while deuxieme_joueur:

         if self.utilise.get(pygame.K_d):
            if self.player2.rect.x >= 840:
                if arriere_x >= -1407:
                    arriere_x -= 1.7
            else:
                self.player2.deplacement(True)


         elif self.utilise.get(pygame.K_q):
            if self.player2.rect.x <= 12 and arriere_x <= 2:
                arriere_x += 1.7
            else:
                self.player2.deplacement(False)
         premier_joueur = True
         deuxieme_joueur = False
        return arriere_x

    def check_collision(self,sprite,group):

        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def lancement_cheban(self):
        self.monstre = cheban(self)
        self.monstre2 = Cheban_gauche(self)
        self.type_monstre = random.choice([True,False])
        if self.type_monstre:
          self.groupe_cheban.add(self.monstre)
        else:
            self.groupe_cheban.add(self.monstre2)







