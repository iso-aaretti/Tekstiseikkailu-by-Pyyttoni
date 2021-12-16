import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuTurunlinnaSivuoviKerroKurkista(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/Linnankaytava.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_28"

        # create exits
        self.exit_a = "scene_101"
        self.exit_b = "scene_101"
        self.exit_c = "scene_101"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Jännittyneenä työnnät oven auki ja astut sisään. RÄKS!! "
                       "Jalkojesi alla ollut lattiaparrun palanen luiskahtaa pois paikaltaan ja vatsassasi "
                       "muljahtaa. Liu'ut jonkunlaista liukuluiskaa pitkin kovaa vauhtia alaviistossa. "
                       "<br><br>"
                       "Tiput ainakin viisi metriä ja lopulta molskahdat veteen. Tajuat, että se oli ansa "
                       "ja räpiköit nyt linnan vallihaudan pohjalla mudan ja veden seassa. Satutit rytäkässä "
                       "polvesi. Suuntaat lähimpään terveyskeskukseen häpeissäsi selittämään tilannetta."
                       "<br><b>HÄVISIT PELIN</b>"
                       "<br><br><br>"

                       )
        return description
