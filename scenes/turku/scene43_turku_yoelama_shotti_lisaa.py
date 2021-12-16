import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuYoelamaShottiLisaa(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-baari-01.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#F0F0F0")
        self.background_colour = pygame.Color("#141414")

        # set id
        self.id = "scene_43"

        # setup exits
        self.exit_a = "scene_44"
        self.exit_b = "scene_4"
        self.exit_c = "scene_43"

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass
        
    def render_front(self, screen):
        pass

    def get_description(self, player):
        description = ("Hygge menee tiskille. Istut hetken kulmapöydässä kun Hygge tuleekin jo takaisin. "
                       "Mukana hänellä on tarjottimen yäteltä juotavaa ja päädytte laulamaan yhdessä "
                       "Kaija Koota karaokeen. Nautitte illasta täysin siemauksin aina pikkutunneille "
                       "asti."
                       "<br><br>"
                       "Hyggen ystävällä on kuulemma jatkot joen rannassa sijaitsevalla jahdilla ja "
                       "hän kysyy sinua mukaansa. Olet jo aivan loppu. Mitä teet?"
                       "<br><br><br>"
                       "        A) <b>Jahti</b>                                 B) <b>Hotelli</b>")
        return description