import pygame
import random

# // Création d'une classe pour gérer les comètes //
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # // Définition de l'image associé à l'événement comète //
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # // Jouer le son //
        self.comet_event.game.sound_manager.play('meteorite')
        # // Vérification de si le nombre de comète est de 0 //
        if len(self.comet_event.all_comets) == 0:
            print("L'événement est fini")
            # // Remettre alors la barre à zéro //
            self.comet_event.reset_percent()
            # // Faire apparaitre les 2 monstres //
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        # // Si la comète ne tombe pas sur le sol //
        if self.rect.y >= 500:
            print("Sol")
            # // Supprimer la boule de feu si elle est en dehors de l'écran //
            self.remove()

            # // Vérifier s'il n'y a plus de boule de feu sur le jeu //
            if len(self.comet_event.all_comets) == 0:
                print("l'événement est fini")
                # //Remettre alors la jauge au départ //
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        # // Vérification de si la boule de feu touche le joueur //
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print("Joueur touché !")
            # // Retirer la boule de feu //
            self.remove()
            # // Faire subir 20 points de dégats au joueur //
            self.comet_event.game.player.damage(20)
