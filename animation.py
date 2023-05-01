import pygame

# // Création d'une classe qui va s'occuper des animations //
class AnimateSprite(pygame.sprite.Sprite):

    # // Définition des choses à faire à la création de l'entité //
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 # // Pour dire que l'on souhaite commencer l'animation à l'image 0, rendre ça plus dynamique et cohérent //
        self.images = animations.get(sprite_name)
        self.animation = False

    # // Définition d'une méthode pour démarrer l'animation //
    def start_animation(self):
        self.animation = True

    # // Défiiniton d'une méthode qui va animer le sprite //
    def animate(self, loop=False):

        # // Vérification de si l'animation est active //
        if self.animation :

            # // Passer d'une image à une autre //
            self.current_image += 1
            #// Vérification si on a atteint la fin de l'animation //
            if self.current_image >= len(self.images):
                # // Remettre l'animation au départ //
                self.current_image = 0

                # // Vérification de si l'animation n'est pas en mode loop //
                if loop is False:

                 # // Désactivation de l'animation //
                 self.animation = False

            # // Modification de l'image précédente par la suivante //
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# // Définition d'une fonction pour charger les images d'un sprite //
def load_animation_images(sprite_name):
    # // Chargement des 24 images de ce sprite dans le dossier correspondant //
    images = []
    # // Récupération du chemin du dossier pour ce sprite //
    path = f"assets/{sprite_name}/{sprite_name}"

    # // Bouclage sur chaque image de ce dossier //
    for num in range(1, 24):
       image_path = path + str(num) + '.png'
       images.append(pygame.image.load(image_path))

    # // Renvoyer le contenu de la liste d'images //
    return images

# // Définition d'un dictionnaire qui va contenir les images chargées de chaque sprite //
# // mummy - > [....mummy1.png, ....mummy2.png, ....]
animations = {
    'mummy' : load_animation_images('mummy'),
    'player' : load_animation_images('player'),
    'alien' : load_animation_images('alien')
}