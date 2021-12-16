import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuYoelama(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-baari-01.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#F0F0F0")
        self.background_colour = pygame.Color("#141414")

        # set id
        self.id = "scene_5"

        # setup exits
        self.exit_a = "scene_41"
        self.exit_b = "scene_42"
        self.exit_c = "scene_41"

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass
        
    def render_front(self, screen):
        pass

    def get_description(self, player):
        description = ("Tallustat hetken katua pitkin ja päätät jäädä ensimmäiseen vastaan "
                       "tulleeseen kuppilaan. Sisällä näyttäisi olevan paljon porukkaa. "
                       "Karaokessa keski-ikäinen mies laulaa Dingoa ja edessä ihmiset tanssivat "
                       "villisti. Päätät suunnata suoraan baaritiskille. "
                       "<br><br>"
                       "Baarimikko tervehtii ja kysyy 'Mitä saisi olla?'"
                       "<br><br><br><br><br><br>"
                       "        A) <b>Kalja</b>                                   B) <b>Shotti</b>                              C) <b>Limu</b> ")
        return description