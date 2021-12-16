import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaPihamaaLapioSisaan(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/luola2.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_32"

        # create exits
        self.exit_a = "scene_100"
        self.exit_b = "scene_100"
        self.exit_c = "scene_100"
        
        # propeller fate
        self.b_discovered_propeller_fate = False

    def get_description(self, player):
        description = ("Näyttäisi siltä, että luola on ollu hautautuneena maahan jo pidemmän "
                       "aikaa. Ryömit sisään luolaan ja lähdet astelemaan kapeaa solaa pitkin "
                       "syvemmälle luolaan. Lopulta päädyt perunakellaria muistuttavaan "
                       "huoneeseen, jonka perältä paljastuu hämähäkinseissien peittämä arkku."
                       "<br><br>"
                       "Kokeilet löytämääsi avainta lukkoon ja BINGO! Arkku aukeaa ja aarre on sinun."
                       "<br><br><br>"
                       "<b>VOITIT PELIN</b>"
                       )
        return description
