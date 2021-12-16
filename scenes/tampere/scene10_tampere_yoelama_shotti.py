import pygame
from scenes.scene import Scene, GameObject

# Tampere yöelämä shotti
class SceneTampereYoelamaShotti(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-baari-juomia-02.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_10"

        # create exits
        self.exit_a = "scene_6"
        self.exit_b = "scene_3"
        self.exit_c = "scene_1"
        
        # propeller fate
        self.b_discovered_propeller_fate = False

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass

    def render_front(self, screen):
        pass

    def get_description(self, player):
        description = ("Kaadat shotin kurkustasi alas yhdellä kädenheilautuksella. "
                       "Tilaat vielä toisen ja kolmannenkin ja päässä alkaa pyöriä. "
                       "Päädy selittämään aartenmetsätysaikeistasi jokaiselle vastaantulijalle, "
                       "joka suostuu kuuntelemaan. Lähdet lopulta baarista. "
                       "<br><br>"
                       "Suuntaatko hotelliin nukkumaan, yöjunaan kohti Turkua vai "
                       "lähdetkö kotiin Helsinkiin? "
                       "<br><br><br><br><br><br>"
                       "        A) <b>Hotelli</b>                               B) <b>Turku</b>                               C) <b>Helsinki</b>"
                       )
        return description
