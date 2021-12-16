import pygame
from scenes.scene import Scene, GameObject

# Tampere hotelli
class SceneTampereHotelli(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/hotelli.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_6"

        # create exits
        self.exit_a = "scene_8"
        self.exit_b = "scene_12"
        self.exit_c = "scene_6"
        
        # propeller fate
        self.b_discovered_propeller_fate = False

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass

    def render_front(self, screen):
        pass

    def get_description(self, player):
        description = ("Heräät hotellin mukavasta sängystä aikaisin aamulla. "
                       "Avaat verhot ja hymyilet nähdessäsi kirkkaan auringonvalon "
                       "valtaavan huoneen. Mielialasi on korkealla ja olet valmis "
                       "aarrejahtiin."
                       "<br><br>"
                       "Pohdit, minne lähtisit etsimään aarretta ensimmäisenä. Mielessäsi "
                       "on kaksi erityistä kohdetta. Hatanpään Arboretum ja Pyynikin Näkörotni. "
                       "<br><br><br><br><br><br>"
                       "        A) <b>Hatanpää</b>                              B) <b>Pyynikki</b>"
                       )
        return description
