import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaPihamaaMuualta(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/kultakalat.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_34"

        # create exits
        self.exit_a = "scene_101"
        self.exit_b = "scene_101"
        self.exit_c = "scene_101"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Jatkat etsintöjä välittämättä kiveen maalatusta nuolesta. Saavut "
                       "koristelammen luo ja huomaat, että vedessä ui kultakaloja. Päätät "
                       "heittää lampeen kolikon ja samalla esittää toiveen aarteen löytämisestä. "
                       "<br><br>"
                       "Suunnitelma menee kuitenkin pahasti mönkään ja molskahdat itse vahingossa "
                       "lampeen liukastuessasi. Kylmissäsi räpiköit kuivalle maalle kalojen "
                       "mulkoillessa sinua hämillään. Olet aivan jäässä ja päätät palata kotiin. "
                       "<br><br><br>"
                       "<b>HÄVISIT PELIN</b>"
                       )
        return description
