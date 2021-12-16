import pygame
from scenes.scene import Scene, GameObject

# Tampere yöelämä shotti
class SceneTampereYoelamaOlut(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-baari-juomia-01.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_11"

        # create exits
        self.exit_a = "scene_13"
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
        description = ("Nautiskelet kylmää olutta ja mielialasi nousee "
                       "Päädyt tiskillä keskuteluun vanhan parrakkaan miehen "
                       "kanssa. Hän ei kerro nimeään, mutta yllättäen tietää "
                       "aarteesta kiinnostavia asioita ja kehoittaa suuntaamaan "
                       "Pyynikin Näkötornille. "
                       "Oluesi tyhjenee ja kiität herraa seurasta. "
                       "<br><br>"
                       "<br><br><br><br><br><br>"
                       "        A) <b>Pyynikki</b>"
                       )
        return description
