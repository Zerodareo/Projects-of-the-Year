import pygame
import random
import animation

# // Création d'une classe qui va gérer la notion de monstre sur notre jeu //
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size) # // Cette commande permet d'appeler la super classe de Sprite afin de la charger dans le jeu //
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.game = game
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
         self.default_speed = speed
         self.velocity = random.randint(1, self.default_speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # // Afin d'infliger des dégats aux ennemis, nous allons créer une variable qui va soutirer des points de vie à l'ennemi //
        self.health -= amount

        # // Nous allons tenter de vérifier si le nouveau nombre de points de vie est inférieur ou égal à zéro, et dans ce cas la supprimer le monstre ou non //
        if self.health <= 0:
         # // Faire réapparaitre comme un nouveau monstre //
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 1)
            self.health = self.max_health
            # // Ajouter le nombre de points a ce jeu //
            self.game.add_score(self.loot_amount)

            # // Vérifier si la barre dévénement est chargé à son maximum //
            if self.game.comet_event.is_full_loaded():
                # // Dans ce cas la on retire les monstres du jeu //
                self.game.all_monsters.remove(self)

                # // Appel de la méthode pour essayer de déclencher la pluie de comète //
                self.game.comet_event.attempt_fall()


    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # Après avoir défini les caractéristiques de notre barre de vie, il est nécessaire de la dessiner à l'écran //
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y -20, self.health, 5])


    def forward(self):
        # // Le déplacement ne se fait que s'il n'y a pas de collision avec un groupe de joueur //
        if not self.game.check_collision(self, self.game.all_players):
         self.rect.x -= self.velocity
        # // Nous allons cette fois-ci vérifier la condition inverse c'est-à-dire si le monstre est en collision avec le joueur //
        else:
            # // Infliger des dégats (au joueur) //
            self.game.player.damage(self.attack)


# // Définition d'une classe pour la mummy //
class Mummy(Monster):

        def __init__(self, game):
            super().__init__(game, "mummy", (130, 130))
            self.set_speed(5)
            self.set_loot_amount(20)
        # // Lors de la création d'une nouvelle instance de la classe Mummu, ça va appeler le constructeur de cette classe qui va lui même appeler le constructeur de Monster //

# // Définition d'une classe pour l'alien //
class Alien(Monster):

        def __init__(self, game):
            super().__init__(game, "alien", (300, 300), 120)
            self.health = 250
            self.max_health = 250
            self.attack = 0.8
            self.set_speed(3)
            self.set_loot_amount(80)