import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuTurunlinna(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-linna-2.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_23"

        # create exits
        self.exit_a = "scene_25"
        self.exit_b = "scene_24"
        self.exit_c = "scene_23"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Lähdet kävelemään kohti Turun linnaa. Ilma "
                       "on hieno. "
                       "<br><br>"
                       "Saavuttuasi pihalle huomaat, että linna on tänään suljettu. Voi räkä! "
                       "Katselet hetken ympärillesi ja huomaat linnan seinässä raollaan "
                       "olevan sivuoven. Virkaintoisen näköinen vartija seisoo kuitenkin linnan "
                       "pääsisäänkäynnillä. "
                       "<br><br>"
                       "Yritätkö sivuovesta sisään vai lähdetkö sittenkin Kakolanmäen vanhaan "
                       "vankilaan? "
                       "<br><br><br><br>"
                       "        A) <b>Sivuovi</b>                                    B) <b>Vankila</b>"
                       )
        return description
