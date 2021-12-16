import pygame
from scenes.scene import Scene, GameObject

# Tampere pyynikki Yö
class SceneTampereHotelliPyynikkiYoKaiva(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-juuri-yo.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_15"

        # create exits
        self.exit_a = "scene_16"
        self.exit_b = "scene_17"
        self.exit_c = "scene_15"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Aloitat kierroksen tornin ympäri metallinpaljastimen kanssa. "
                       "Metallinpaljastin piippailee aika-ajoin ja pian kuulet takaasi "
                       "askelten ääniä. <br><br>Paikalle on saapunut äkäisen näköinen vartija! "
                       "Hän kysyy kipakasti 'Mitäs täällä melutaan?'. Sanot nopeasti "
                       "etsiväsi: "
                       "<br><br><br><br><br><br>"
                       "        A) <b>Avaimet</b>                               B) <b>Aarre</b>"
                       )
        return description
