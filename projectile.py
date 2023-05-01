import pygame

# // Désormais, nous allons définir la classe qui va gérer les animations/déplacements des projectiles de notre joueur //

class Projectile(pygame.sprite.Sprite):

    # Nous allons ici construire le constructeur de cette classe, tout ce que nous mettrons dans le constructeur va se charger lorsque le joueur va générer un prokectile //

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self): # // Ce constructeur permet de définir la vitesse de rotation du projectile //
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self): # // Ce constructeur permet de définir la suppression du projectile à la sortie de l'écran //
        self.player.all_projectiles.remove(self)

    def move(self): # // Ce constructeur permet de définir les paramètres de mouvement du projectile sur l'ave des abscisse //
        self.rect.x += self.velocity
        self.rotate()

        # // Vérification de si le projectile entre en collision avec un monstre //
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # Supprimer le projectile lors de la collision avec le monstre //
             self.remove()
            # Variable qui va pouvoir infliger des dégats aux ennemis //
             monster.damage(self.player.attack)


        # Dans le fichier "main.py", nous avons pu paramétrer le déplacement des projectiles. Cette fois-ci, nous essayerons de déterminer si le projectile est présent à l'écran ou non//
        if self.rect.x > 1080:
        # Si les coordonnées en x du projectile sont supérieur à la résolution de l'écran, alors on décide de le supprimer //
           self.remove()
           print("Projectile supprimé")
