import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuTurunlinnaSivuovi(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-linna-2.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_25"

        # create exits
        self.exit_a = "scene_26"
        self.exit_b = "scene_27"
        self.exit_c = "scene_25"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Odotat sopivaa hetkeä kun vartija katsoo muualle. Hetkesi on "
                       "koittanut. "
                       "Livahdat sivuovesta vaivihkaa sisään ja onnistut pääsemään sisään. "
                       "<br><br>"
                       "Sisällä tuoksuu terva, on hämärää ja hiljaista. Ainoastaan tuuli "
                       "vinkuu vaimeasti vasten linnan vanhoja rakenteita. Hiippailet pitkin "
                       "käytävää eteenpäin, kunnes kuulet aivan takanasi oven aukeavan. "
                       "<br><br>"
                       "Oven suussa seisoo mies, joka esittäytyy Juhanaksi. Hän kertoo asuneensa "
                       "linnassa jo satoja vuosia ja kysyy millä asioilla linnassa olet. Juoksetko "
                       "karkuun vai kerrotko Juhanalle aarteesta?"
                       "<br><br>"
                       "        A) <b>Juokse</b>                                B) <b>Kerro</b>"
                       )
        return description
