import pygame
from scenes.scene import Scene, GameObject


class SceneTampereHotelliPyynikkiYo(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-juuri-yo.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_13"

        # create exits
        self.exit_a = "scene_14"
        self.exit_b = "scene_15"
        self.exit_c = "scene_13"

        # propeller fate
        self.b_discovered_propeller_fate = False

    def get_description(self, player):
        description = ("Saavut Pyynikin Näkötornille myöhään illalla lapion kanssa. "
                       "Tornin ympäristö on hiljainen ja autio. Selkäpiitäsi karmii. "
                       "<br><br>"
                       "Ajattelet, että joko piiloudut pusikkoon tarkkailemaan hetkeksi "
                       "tilannetta tai alat heti pimeydessä kaivamaan aarretta. Mitä teet? "
                       "<br><br><br><br><br><br><br>"
                       "        A) <b>Piiloudu</b>                                    B) <b>Kaiva</b>"
                       )
        return description
