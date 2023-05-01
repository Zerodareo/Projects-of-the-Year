from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
import pygame


# // Création d'une seconde classe qui va représenter notre jeu //
from sound import SoundManager


class Game:

    def __init__(self):
        # // Définition de si notre jeu a commencé ou non //
        self.is_playing = False
        # // Dans ce constructeur, nous souhaitons générer notre personnage à chaque fois que le joueur créera une nouvelle session //
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # // générer l'événément "Pluie de comète" //
        self.comet_event = CometFallEvent(self)
        # // Nous souhaitons faire "spawner" plusieurs monstres à l'écran //
        self.all_monsters = pygame.sprite.Group()
        # // Gérer le son //
        self.sound_manager = SoundManager()
        # // Au chargement du jeu, nous allons faire en sorte de mettre le score à zéro //
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # // Remettre le jeu à zéro (retirer les mosntres, remetrre le joueur à 100 de vie et mettre le jeu en attente //
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # // Jouer le son du game over //
        self.sound_manager.play('game_over')

    def update(self, screen):
        # // Afficher le score sur l'écran //
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # // Nous allons donc appliquer l'image de notre joueur sur le background du jeu //
        screen.blit(self.player.image, self.player.rect)

        # // Actualisation de la barre de vie du joueur //
        self.player.update_health_bar(screen)

        # // Actualisation de la barre d'événement du jeu //
        self.comet_event.update_bar(screen)

        # // Actualisation de l'animation du joueur //
        self.player.update_animation()

        # // Noux allons donc récupérer les projectiles de notre personnage joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # // Nous allons récupérer les monstres de notre jeu //
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # // Récupération des comètes de notre jeu //
        for comet in self.comet_event.all_comets:
            comet.fall()

        # // Nous allons ici appliquer l'ensemble des images de mon groupe de projectiles //
        self.player.all_projectiles.draw(screen)

        # // Nous allons appliquer l'ensemble des images de mon groupe de monstres //
        self.all_monsters.draw(screen)

        # // Nous allons donc appliquer l'ensemble des images de mon groupe de comètes //
        self.comet_event.all_comets.draw(screen)

        # Création d'un condition quiu permettra de vérifier si le joueur souhaite aller à gauche ou à droite //
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))

