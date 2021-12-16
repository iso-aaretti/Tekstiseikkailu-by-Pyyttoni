import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuHotelli(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/hotelli.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#F0F0F0")
        self.background_colour = pygame.Color("#141414")

        # set id
        self.id = "scene_4"

        # setup exits
        self.exit_a = "scene_23"
        self.exit_b = "scene_24"
        self.exit_c = "scene_4"

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass
        
    def render_front(self, screen):
        pass

    def get_description(self, player):
        description = ("Nukut maukkaat yöunet ja heräät hotellin puhtaista lakanoista. "
                       "Vatsasi kurnii ja päätät mennä hotellin ravintolaan syömään "
                       "aamupalan. "
                       "Vatsa täynnä pohdit mihin lähtisit aarretta etsimään. Turun "
                       "linnaan vai Kakolanmäen vanhaan vankilaa?"
                       "<br><br><br><br><br><br><br><br>"
                       "        A) <b>Turun linna</b>                           B) <b>Vankila</b>"
                       )
        return description