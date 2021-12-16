import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankila(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-kakola.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_24"

        # create exits
        self.exit_a = "scene_30"
        self.exit_b = "scene_35"
        self.exit_c = "scene_24"
        
        # propeller fate
        self.b_discovered_propeller_fate = False



    def get_description(self, player):
        description = ("Matkustat Kakolanmäelle bussilla ja matkalla juttelet mukavia "
                       "viereesi istahtaneen vanhan rouvan kanssa. Kerrot rouvalle "
                       "olevasi menossa etsimään aarretta Kakolanmäeltä ja hän kertookin "
                       "sinulle kuulleensa huhun, jonka mukaan eräs vanki olisi piilottanut "
                       "alueelle jotakin arvokasta aikoja sitten. "
                       "<br><br>"
                       "Pysäkkisi tulee ja on aika nousta kyydistä. Hyvästelet rouvan ja kiität "
                       "neuvoista. Kipuat pitkin rinnettä kohti Kakolanmäkeä ja edessäsi kohoaakin "
                       "pian jykevä vankilarakennus. Löytyyköhän aarre pihamaalta vai rakennuksesta? "
                       "<br><br><br>"
                       "        A) <b>Pihamaa</b>                               B) <b>Rakennus</b>"
                       )
        return description
