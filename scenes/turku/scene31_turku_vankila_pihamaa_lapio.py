import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaPihamaaLapio(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/avain.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_31"

        # create exits
        self.exit_a = "scene_32"
        self.exit_b = "scene_33"
        self.exit_c = "scene_31"

        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Poimit rautalapion seinän vierestä ja alat hommiin. Kaivat vimmatusti "
                       "nuolen osoittamasta kohdasta ja lapiosi lopulta kolahtaakin johonkin. "
                       "Maan alta paljastuu metallinen rasia, jonka sisältä löytyy avain. "
                       "<br>"
                       "Mihinköhän avain sopii oikein, ajattelet. Hortoilet hetken ympäriinsä "
                       "hämmentyneenä, kunnes huomaat rakennuksen sivustalla sateiden aiheuttaman "
                       "pienen maanvajoaman. Kurkkaat lähempää ja huomaat, että vajoaman pohjalla "
                       "on luolan suuaukko!"
                       "<br><br>"
                       "Uskaltaudutko tutkimaan luolaa? Siellähän voi olla vaikka lepakoita."
                       "<br><br><br><br>"
                       "        A) <b>Sisään</b>                                  B) <b>Pois</b>"
                       )
        return description
