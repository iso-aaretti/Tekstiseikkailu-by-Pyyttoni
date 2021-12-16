import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaRakennusTikkaatUudestaan(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-kakola.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_37"

        # create exits
        self.exit_a = "scene_38"
        self.exit_b = "scene_30"
        self.exit_c = "scene_37"

        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kipuat uudestaan tikkaita ja onnistut tällä kertaa pääsemään avoimen "
                       "ikkunan kohdalle. Juuri kiivetessäsi ikkunasta sisään sisältä ilmestyy "
                       "isokokoinen koira hampaat esillä haukkuen ja syöksyy sinua kohti. Pelästys "
                       "ja yrität räpiköidä otetta tikkaista. Saat kuin saatkin tikkaista kiinni ja "
                       "liu'ut niitä alaspäin kuin palomies konsanaan. Tekniikkasi kuitenkin pettää.. "
                       "<br><br>"
                       "Otteesi lipeää tikkaista ja tiput selkä edellä kohti maata. Yllätykseksesi "
                       "osuma on pehmeä! Maa pettää altasi ja rojahdat maaperän läpi huoneeseen ,jonka "
                       "toteat olevan jonkinlainen perunakellari. Kannattaisiko sitä tutkia enemmän vai "
                       "jatkaa etsintöjä pihamaalta?"
                       "<br><br>"
                       "        A) <b>Tutki</b>                                  B) <b>Pihamaa</b>"
                       )
        return description
