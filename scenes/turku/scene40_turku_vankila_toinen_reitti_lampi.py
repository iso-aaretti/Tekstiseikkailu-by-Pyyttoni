import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaToinenReittiLampi(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/kultakalat.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_40"

        # create exits
        self.exit_a = "scene_100"
        self.exit_b = "scene_100"
        self.exit_c = "scene_100"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Tallustat lammen reunalle vilkaisten hölmistyneen näköisiä kaloja. <br>"
                       "Asetut takaperin heittäen kolikon olkasi yli sulkien samalla silmäsi. "
                       "Et ole taikauskoinen, mutta esität nyt ajatuksissasi yhden toiveen. "
                       "Toivot hartaasti löytäväsi aarteen...."
                       "<br><br>"
                       "Avaat silmäsi ja kuin ihmeen kaupalla jalkojesi juuressa komeilee ihka "
                       "oikea aarre! Ihmeitä ilmeisesti tapahtuu.."
                       "<br><br><br>"
                       "<b>VOITIT PELIN</b>"
                       )
        return description
