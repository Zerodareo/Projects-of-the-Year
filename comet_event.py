import pygame
from comet import Comet

# // Création d'une classe qui va gérer cet événement à intervales réguliers //
class CometFallEvent:

    # // Lors du chargement, on souhaite créer un compteur qui contrôler le pourcentage actuel de cette barre //
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

    # // Définition d'un groupe de sprite pour stocker nos comètes //
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def comet_fall(self):
        # // Création d'un boucle entre les valeurs 1 et 10 //
        for i in range(1, 10):
            # // Faire apparaitre la première boule de feu //
              self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # // Elle s'exécutera uniquement si la jauge est complètement chargé //
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("Pluie de comète !!!")
            self.comet_fall()
            self.fall_mode = True #// Activation de l'événement //

    def update_bar(self,surface):

        # // Ajout de pourcetntage à la barre //
        self.add_percent()


        # // Barre noir (en arrière plan) //
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # // l'axe des x //
            surface.get_height() - 20, # // l'axe des y //
            surface.get_width(), # // longueur de la fenêtre //
            10 # // épaisseur de la barre //
        ])
        # // Barre rouge (jauge d'événément) //
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # // l'axe des x //
            surface.get_height() - 20,  # // l'axe des y //
            (surface.get_width() / 100) * self.percent,  # // longueur de la fenêtre //
            10  # // épaisseur de la barre //
        ])
