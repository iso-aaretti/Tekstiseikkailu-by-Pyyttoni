import pygame
from scenes.scene import Scene, GameObject


class SceneVoitto(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/aarre.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_100"

        # create exits
        self.exit_a = "scene_1"
        self.exit_b = "scene_1"
        self.exit_c = "scene_1"

    def get_description(self, player):
        description = ("<b>ONNEKSI OLKOON"
                       "<br><br><br>"
                       "VOITIT PELIN</b>!"
                       "<br><br><br><br><br><br>"
                       "Paina A, B tai C aloittaaksesi alusta.")

        return description
