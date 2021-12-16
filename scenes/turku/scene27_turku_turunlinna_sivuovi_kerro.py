import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuTurunlinnaSivuoviKerro(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/Linnankaytava2.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_27"

        # create exits
        self.exit_a = "scene_29"
        self.exit_b = "scene_28"
        self.exit_c = "scene_27"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kerrot Juhanalle aarteesta ja epäilyistäsi, että se voisi olla Turun linnassa. "
                       "Juhana hörähtää äänekkääseen nauruun. Hän hipoo partaansa ja kertoo, että "
                       "kuninkaansalista voisi mahdollisesti löytyä jotain kiinnostavaa. "
                       "<br><br>"
                       "Juhana viittoo kädellään käytävän perälle ja käskee kääntymään sieltä oikealle. "
                       "Vilkaiset Juhanan käden osoittamaan suuntaan ja kääntäessäsi katseesi takaisin "
                       "Juhana on jo kadonnut. Huomaat samalla vieressäsi oven, jossa lukee 'Älä avaa!'."
                       "<br><br>"
                       "Jatkaakko Juhanan osoittamaan suuntaan vai kurkata mitä oven takana on? <br>"
                       "Mitä teet seuraavaksi? "
                       "<br><br>"
                       "        A) <b>Jatka</b>                                     B) <b>Kurkista</b>"
                       )
        return description
