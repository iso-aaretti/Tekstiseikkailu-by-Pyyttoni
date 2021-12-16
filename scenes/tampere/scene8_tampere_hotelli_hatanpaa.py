import pygame
from scenes.scene import Scene, GameObject

# Tampere hotelli -> Hatanpää
class SceneTampereHotelliHatanpaa(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-hatanpaan-arboretum.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_8"

        # create exits
        self.exit_a = "scene_101"
        self.exit_b = "scene_6"
        self.exit_c = "scene_8"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Nautit syksyn väriloistosta Hatanpään Arboretumissa, ja kulutat koko "
                       "aurinkoisen päivän yrittämällä etsiä puutarhasta vihjeitä aarteenetsintään. "
                       "Valitettavasti etsintäsi ei tuota tulosta. Mitä teet?"
                       "<br><br><br><br><br><br><br><br><br>"
                       "        A) <b>Luovutus</b>                                  B) <b>Hotelli</b>"
                       )
        return description
