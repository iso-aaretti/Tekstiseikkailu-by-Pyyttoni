import pygame
from scenes.scene import Scene, GameObject

# Tampere pyynikki Yö
class SceneTampereHotelliPyynikkiYoPiiloudu(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-juuri-yo.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_14"

        # create exits
        self.exit_a = "scene_9"
        self.exit_b = "scene_14"
        self.exit_c = "scene_14"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Piiloudut lähimpään pusikkoon ja odotat hetken. Seuraat tilannetta "
                       "piiloutuneena ja huomaat pian, että tornin ympäristöä saapuu "
                       "kiertämään vartija. Odotat, että hän kävelee pois päin."
                       "Kun olet varma hänen poistumisestaan uskaltaudut kaivamaan. "
                       "<br><br><br><br><br><br><br><br>"
                       "        A) <b>Kaiva</b>"
                       )
        return description
