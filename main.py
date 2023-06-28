import pygame
import time
from game import Game
from time import sleep as delay



pygame.init()

# creer la fenetre

pygame.display.set_caption("popolan")
ecran_de_fond = pygame.display.set_mode((1000, 500))

# importer images
arriere_plan = pygame.image.load("image/bg.jpg")
banniere= pygame.image.load("assets/banner.png")
banniere=pygame.transform.scale(banniere,(400,300))
boutton_play=pygame.image.load("assets/button.png")
boutton_play_rect=boutton_play.get_rect()
boutton_play=pygame.transform.scale(boutton_play,(300,100))
introduction=pygame.image.load("image/intro.png")
introduction=pygame.transform.scale(introduction,(1000,500))
premier_joueur = True
deuxieme_joueur = False

# charger notre jeu
game = Game()

game_on = True
arriere_x = 0
temps_depart = time.time()
son=pygame.mixer.Sound('assets/sounds/Rocket Empire - SriSro.mp3')


while game_on:

 ecran_de_fond.blit(arriere_plan, (arriere_x, -515))
 # on essai de faire l"ecran d'accueil
 if game.game_on is True and game.intro is False:
     arriere_x=game.Jouer(ecran_de_fond,arriere_x,premier_joueur,deuxieme_joueur)
 elif game.game_on is False and game.intro is True:

    temps_fin=time.time()
    ecran_de_fond.blit(introduction,(0,0))
    temps = temps_fin - temps_depart
    if temps>=9:
     game.intro=False
 elif game.game_on is False and game.intro is False:
     ecran_de_fond.blit(boutton_play,(360,225))
     ecran_de_fond.blit(banniere, (300, 10))

 #ici on se chqrge d'executer les "frames"...

 pygame.time.delay(10)
 # On fait les sauts...

 game.player.jump()
 game.player2.jump()

 #on effectue le coup de poings

 game.player.animation_coup_de_poing()







 pygame.display.flip()


 for evenement in pygame.event.get():
     for monstre in game.groupe_cheban:
         monstre.deplacer()
     if evenement.type == pygame.KEYDOWN:
         game.utilise[evenement.key] = True

         if evenement.key == pygame.K_SPACE:
             game.player.operation_coup_de_poing=True
             game.player.lancement(False)

         if evenement.key == pygame.K_b:
             if game.player.coup_critique >= 130:
              game.player.lancement(True)

         elif game.utilise.get(pygame.K_UP):
             game.player.saut=True

         elif game.utilise.get(pygame.K_z):
             game.player2.saut=True

     elif evenement.type == pygame.KEYUP:
         game.utilise[evenement.key] = False

     elif evenement.type == pygame.QUIT:
         game_on = False
         print("on ferme le jeu")

     elif evenement.type == pygame.MOUSEBUTTONDOWN:
         if game.intro is False:
          if boutton_play_rect.collidepoint(evenement.pos):
              game.game_on=True




pygame.quit()

