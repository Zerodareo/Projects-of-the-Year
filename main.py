import pygame
import math
from game import Game
pygame.init()
# // L'étape ci-dessus permet entre autre de générer les éléments contenus dans le fichier pygame, on fait donc une déclaration afin d'utiliser les éléments du fichier //
# // Définition d'une clock //
clock = pygame.time.Clock()
FPS = 60

# Les commandes ci-dessus définissent les premiers paramètres de notre joueur //

pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1200, 750))

# // La variable ci-dessus permet non seulement d'afficher la fenêtre de jeu, mais va aussi permettre d'afficher le fond d'écran du jeu //

# // Ici, nous allons charger l'image qui servira de background au jeu vidéo //
background = pygame.image.load("assets/bg.jpg")

# // Importation de notre banniére de jeu (écran d'accueil //
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Importation du bouton qui permettra de lancer la partie //
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# La classe Game jusque là ne charge rien pour le moment, donc nous allons placer juste après notre variable "background" une fonction qui va générer notre jeu //

game = Game()


running = True

# // Cette variable servira notamment à savoir si notre notre fenêtre est en cours d'éxécution ou non, si l'écran est fermé ou bien ouvert //

# // Pour que la fenêre reste constament ouverte, il est nécessaire de créer une boucle qui vérifiera que tant que la variable RUNNING sera sur Vrai, alors la fenêtre rertera ouverte //

while running:
    # // Nous allons donc utiliser la boucle principale du jeu pour appliquer l'arrière plan voulu. La fonction ".Blit" permet d'injecter une image à un endroit spécifique //
    screen.blit(background, (0, -200))

    # // Vérification de si le jeu a commencé ou non //
    if game.is_playing:
        # // Déclencechement des instructions de la partie //
        game.update(screen)
    # / Vérification de si notre jeu n'a pas commencé //
    else :
        # // Ajout de l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    print(game.player.rect.x)

    # // A cette étape du code, il est important de mettre à jour les informations du jeu. Pour se faire, nous allons utiliser la commande ".flip" //
    pygame.display.flip()
    for event in pygame.event.get():
        # // nous entronss désormais dans la condition de la boucle à savoir si l'événement récupéré est égale à False, alors on ferme la fenêtre //
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

            # // Nous allons rajouter une condition qui va s'occuper de détecter si un joueur enclenche une touche du clavier //
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # // Dans cette condition, nous essayerons de détecter si le joueur enclenche la touche ESPACE pour lancer un projectile //
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # // Si la souris est en intéraction avec le bouton "Play", alors on passe de la fenêtre Accueil à celle du jeu réel //
                    game.start()
                    # // Jouer le son en question //
                    game.sound_manager.play('click')
                    
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # // Nous allons essayer de savoir ici si la souris est en collision avec le bouton "Play", si la souris se situe sur l'icône //
            if play_button_rect.collidepoint(event.pos):
                # // Si la souris est en intéraction avec le bouton "Play", alors on passe de la fenêtre Accueil à celle du jeu réel //
                game.start()
                # // Jouer le son en question //
                game.sound_manager.play('click')

    # // Fixer le nombre de FPS sur la clock //
    clock.tick(FPS)




