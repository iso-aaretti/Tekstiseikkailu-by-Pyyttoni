import pygame
from scenes.scene import Scene, GameObject


class SceneHavio(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/loppu.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_101"

        # create exits
        self.exit_a = "scene_1"
        self.exit_b = "scene_1"
        self.exit_c = "scene_1"

    def get_description(self, player):
        description = ("<br><br>"
                       "<b>HÄVISIT PELIN!</b>"
                       "<br><br><br>"
                       "Paina A,B tai C aloittaaksesi alusta.")

        return description
