import pygame
from scenes.scene import Scene, GameObject

# Tampere pyynikki Yö
class SceneTampereHotelliPyynikkiYoKaivaAarre(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-juuri-yo.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_17"

        # create exits
        self.exit_a = "scene_9"
        self.exit_b = "scene_17"
        self.exit_c = "scene_17"

        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kerrot vartijalle aarteesta. Hän kuitenkin katsoo sinua kuin hullu puuroa."
                       "Vartija toteaa, ettei hän ole taikauskoinen ja lähtee kävelemään pois. "
                       "Voit jatkaa kaivamista rauhassa."
                       "<br><br><br><br><br><br>"
                       "        A) <b>Kaiva</b>"
                       )
        return description
