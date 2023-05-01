import pygame
from projectile import Projectile
import animation
# //Création d'une première classe qui va représenter notre personnage joueur //
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
             self.health -= amount
        else:
            # // Dans le cas où le joueur n'a plus de point de vie //
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # Après avoir défini les caractéristiques de notre barre de vie, il est nécessaire de la dessiner à l'écran //
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5])

    def launch_projectile(self):
        # Création d'une nouvelle instance de la classe projectile
        projectile = Projectile(self)
        self.all_projectiles.add(Projectile(self))

        # // Au moment du lancer du projectile, nous allons démarrer l'animation du lancer du projectile //
        self.start_animation()
        # // Jouer le son du projectile //
        self.game.sound_manager.play('tir')

# // La variable ci-dessus permet non seulement de générer un projectile, mais va automatiquement l'ajouter à un groupe de projectile pour que le joueur puisse en lancer plusieurs //
    def move_right(self):
        # // Le déplacement ne pourra se faire que si le joueur n'est pas en collision avec un monstre //
        if not self.game.check_collision(self, self.game.all_monsters):
         self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity