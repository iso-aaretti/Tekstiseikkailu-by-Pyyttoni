import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuTurunlinnaSivuoviJuokse(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/Linnankaytava2.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_26"

        # create exits
        self.exit_a = "scene_101"
        self.exit_b = "scene_101"
        self.exit_c = "scene_101"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Juokset niin kovaa kuin pystyt. Juokset ohi ovien ja ikkunoiden.. AUTS!! "
                       "Tätä et osannut odottaa. Kulman takana oli portaikko ja lennähdit suoraan "
                       "täydessä vauhdissa portaat alas. "
                       "<br><br>"
                       "Loukkaat polvesi etkä pysty enää kävelemään. Vartijat soittavat ambulanssin "
                       "ja reissusi päättyy sairaalaan. "
                       "<br><b>HÄVISIT PELIN</b>"
                       "<br><br>"
                       )
        return description
