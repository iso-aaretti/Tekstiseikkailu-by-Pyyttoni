import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuYoelamaShotti(Scene):
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-baari-juomia-02.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#F0F0F0")
        self.background_colour = pygame.Color("#141414")

        # set id
        self.id = "scene_42"

        # setup exits
        self.exit_a = "scene_43"
        self.exit_b = "scene_4"
        self.exit_c = "scene_42"

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass
        
    def render_front(self, screen):
        pass

    def get_description(self, player):
        description = ("Pitkän päivän jälkeen kiskaiset shotin kurkusta alas käden käänteessä. Otat vielä "
                       "pari lisää ja tunnet pian olevasi juopunut. Tepastelet viskikola kädessäsi tanssi- "
                       "lattialle. Jatkat juomista ja tanssimista ja karaokekin kuulostaa yllättävän hyvältä. "
                       "<br><br>"
                       "Törmään tanssilattialla henkilöön nimeltä Hygge hänen horjuttua paikalle jostain "
                       "takavasemmalta. Hyggellä on hyvä meno päällä ja hän kysyy tahdotko lisää juotavaa. "
                       "Humala painaa jo päälle ja kello on aika paljon.. Pohdit mitä tekisit."
                       "<br><br><br>"
                       "        A) <b>Lisää</b>                                 B) <b>Hotelli</b>")
        return description