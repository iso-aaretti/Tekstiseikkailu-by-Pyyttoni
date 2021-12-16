import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuTurunlinnaSivuoviKerroJatka(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/linnankaytava.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_29"

        # create exits
        self.exit_a = "scene_100"
        self.exit_b = "scene_101"
        self.exit_c = "scene_29"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Jatkat Juhanan osoittamaan suuntaan. Saavut ovelle, jossa lukee "
                       "'Kuninkaansali'. Työnnät raskaan oven varovasti auki ja astut sisään. "
                       "<br><br>"
                       "Salissa on pilkkopimeää. Kaivat taskustasi puhelimen ja laitat taskulampun "
                       "päälle. Valokeila liukuu pitkin seinillä komeilevia taideteoksia. Katseesti "
                       "kiinnittyy erääseen taideteokseen, joka on maalattu vuonna 1523. Mitä ihmettä! "
                       "Taulussa komeilee juuri tapaamasi Juhana! Tilanne alkaa karmimaan "
                       "selkäpiitä oikein kunnolla. "
                       "<br><br>"
                       "Kävelet salin perälle ja huomaat salin perällä puisen arkun. "
                       "<br><br><br>"
                       "        A) <b>Avaa<b>                               B) <b>Poistu<b>"
                       )
        return description
