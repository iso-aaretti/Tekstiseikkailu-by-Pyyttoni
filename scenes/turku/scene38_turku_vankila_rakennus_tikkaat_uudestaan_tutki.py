import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaRakennusTikkaatUudestaanTutki(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-kakola.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_38"

        # create exits
        self.exit_a = "scene_30"
        self.exit_b = "scene_38"
        self.exit_c = "scene_38"


    def get_description(self, player):
        description = ("Nouset maasta ja karistelet mudan sekä syksyn lehdet päältäsi. Paikka "
                       "näyttää siltä, että siellä ei ole vierailtu vuosiin. Silmäilet ympärillesi "
                       "ja jostain nurkasta lentää lepakko aivan pääsi ohi. Huomaat aivan huoneen "
                       "perällä hämähäkinseitteihin vuorautuneen arkun, joka on kuitenkin lukossa. "
                       "<br><br>"
                       "Arkun päällä on kuitenkin valokuva vankilan pihalta löytyvästä suuresta "
                       "kivestä, johon on maalattu nuoli alaspäin. Olisi sittenkin pitänyt etsiä "
                       "pihamaalta! "
                       "<br><br><br><br><br>"
                       "        A) <b>Pihamaa</b>"
                       )
        return description
