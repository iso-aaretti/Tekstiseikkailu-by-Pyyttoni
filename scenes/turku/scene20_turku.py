import pygame
from scenes.scene import Scene, GameObject


class SceneTurku(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-rautatieasema.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_3"

        # create exits
        self.exit_a = "scene_4"
        self.exit_b = "scene_5"
        self.exit_c = "scene_3"

    
    def get_description(self, player):
        description = ("Kello on 20.52 ja saavut Turun rautatieasemalle. Astut ulos junasta ja "
                       "syksyinen tuuli ja sade alkavat piiskaamaan kasvojasi. Olet hetkessä litimärkä"
                       "<br><br>"
                       "Ajattelet, että Aarteenetsintä saa jäädä tältä päivältä. Yksinkertaisesti "
                       "sää on niin huono, ettei eteensä näe. Pohdit, menisitkö suoraan hotelliin "
                       "nukkumaan, jotta huomenna olisit pirteä heti aamusta. Toinen vaihtoehto "
                       "on lähteä lähimpään kuppilaan pitelemään sadetta ja tutustumaan Turun yöelämään."
                       "<br><br>"
                       "Mitä teet? "
                       "<br><br><br>"
                       "         A) <b>Hotelli</b>                               B) <b>Yöelämä</b>"
                       )
        return description