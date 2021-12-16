import pygame
from scenes.scene import Scene, GameObject

# Tampere pyynikki
class SceneTampereHotelliPyynikki(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-juuri-yo.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_9"

        # create exits
        self.exit_a = "scene_100"
        self.exit_b = "scene_101"
        self.exit_c = "scene_9"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kierrät Pyynikin tornia metallinpaljastimen kanssa. "
                       "Pienen tutkiskelun jälkeen paljastin alkaa piipittää. "
                       "Aikasi kaivettua lapiosi kalahtaa johonkin kovaan tornin "
                       "juurella. "
                       "Kaivat esiin puisen pienen arkun. Avaat arkun jännityksissäsi "
                       "ja sisältä paljastuu käärö, jossa on seitsemän numeroa välillä "
                       "<br><br>"
                       "Päätät täyttää löytämilläsi numeroilla lottokupongin."
                       "<br><br><br><br><br><br>"
                       "        A) <b>Tämä viikko</b>                        B) <b>Ensi viikko</b>"
                       )
        return description
