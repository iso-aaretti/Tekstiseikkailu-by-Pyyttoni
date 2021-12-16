import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuYoelamaShottiLisaaJahti(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-baari-juomia-03.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#F0F0F0")
        self.background_colour = pygame.Color("#141414")

        # set id
        self.id = "scene_44"

        # setup exits
        self.exit_a = "scene_23"
        self.exit_b = "scene_44"
        self.exit_c = "scene_44"

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass
        
    def render_front(self, screen):
        pass

    def get_description(self, player):
        description = ("Hygge ottaa teille taksin joelle, vaikka kävelymatka on lähes mitätön. "
                       "Astutte hulppeaan jahtiin ja bailaatte koko yön. Olet korviasi myöten "
                       "ihastunut Hyggeen.."
                       "<br><br>"
                       "Bailaatte Hyggen kanssa seuraavat päivät toistaen aina samaa kaavaa. Ensin "
                       "yökerhossa ja sitten jatkot jahdilla."
                       "<br><br>"
                       "Neljäntenä aamuna heräät Turun linnan pihamaalta huonovointisena. Hyggeä "
                       "ei näyt missään. Katselet hetken ympärillesi ja kävelet kohti linnaa."
                       "<br><br><br>"
                       "        A) <b>Turun linna</b>")
        return description