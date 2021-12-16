import pygame
from scenes.scene import Scene, GameObject

# Alkukohtaus
class SceneOne(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/hki-rautatieasema.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_1"

        # create exits
        self.exit_a = "scene_2"
        self.exit_b = "scene_3"
        self.exit_c = "scene_1"


    def get_description(self, player):
        description = ("Olet saanut luotettavalta lähteeltä vihiä salaisesta aarteesta. "
                       "Et voi vastustaa kiusausta lähteä etsimään sitä, voihan se olla arvokaskin. "
                       "<br><br>"
                       "Kuulit tarinan vanhalta höperöityneeltä rouvalta. Hän ei osannut kertoa "
                       "siitä paljoakaan. "
                       "Hän muisti vain sen, että aarre sijaitsee joko Turussa tai Tampereella "
                       "<br><br>"
                       "Olet saapunut Helsingin päärautatieasemalle. Kumpaan kaupunkiin suuntaat? "
                       "<br><br>")

        description += ("<br><br><br>"
                        "       <b>A) Tampere</b>                               <b>B) Turku</b>"
                        )
        return description
