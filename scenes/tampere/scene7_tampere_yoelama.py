import pygame
from scenes.scene import Scene, GameObject

# Tampere yöelämä
class SceneTampereYoelama(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-baari.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_7"

        # create exits
        self.exit_a = "scene_10"
        self.exit_b = "scene_11"
        self.exit_c = "scene_11"
        
        # propeller fate
        self.b_discovered_propeller_fate = False

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass

    def render_front(self, screen):
        pass

    def get_description(self, player):
        description = ("Tervetuloa Tampereen yöelämään! "
                       "<br><br>"
                       "Saavut viehättävään pieneen "
                       "kulmakuppilaan ja kävelet suorin päin baaritiskille. Nuori baarimikko "
                       "toivottaa hyvät illat ja kysyy tilaustasi. <br>"
                       "Tilaatko shotin vai oluen?"
                       "<br><br><br><br><br><br><br>"
                       "        A) <b>Shotti</b>                                  B) <b>Olut</b>"
                       )
        return description
