import pygame
from scenes.scene import Scene, GameObject

# Tampere
class SceneTampere(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-rautatieasema.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_2"

        # create exits
        self.exit_a = "scene_6"
        self.exit_b = "scene_7"
        self.exit_c = "scene_2"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kello on 19.53 ja saavut Tampereen rautatieasemalle. Astut ulos asemalta ja ilta on jo pimeä. "
                        "Sinua haukotuttaa pitkän päivän päätteeksi. Olet kuitenkin innoissasi saapuessasi "
                        "uuteen kaupunkiin, jossa et ole koskaan kunnolla käynyt. "
                        "Mitä teet seuraavaksi? "
                        
                        "<br><br><br><br><br><br><br>"
                        "         A) <b>Hotelli</b>                               B) <b>Yöelämä</b>"
                        )
        return description
