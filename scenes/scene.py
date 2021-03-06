import pygame


class GameObject:
    def __init__(self):
        self.name = ""
        self.detailed_description = ""
        self.aliases = []
        self.pick_upable = False
        self.activate_description = ""
        self.change_on_activate_object = None
        self.should_remove_on_activate = False

    def combine(self, object_to_combine_with, scene, inventory):
        description = ""
        description += self.name
        description += ""
        description += object_to_combine_with.name
        return False, scene, inventory, description

    def set_player_flag_on_activate(self, player):
        return player


class Scene:
    def __init__(self):
        self.id = ""
        self.objects = []

        self.text_colour = pygame.Color("#141414")
        self.player_text_colour = pygame.Color("#B41414")
        self.background_colour = pygame.Color("#F0F0F0")
        
        self.is_first_visit = True
        self.fade_timer_acc = 0.0
        self.fade_time = 0.5
        self.type_print_per_letter_timer_acc = 0.0
        self.type_print_per_letter_time = 0.02
        self.type_letter_progress = 0

    def update(self, time_delta):
        pass

    def render_back(self, screen):
        pass
        
    def render_front(self, screen):
        pass

    def get_description(self, player):
        return ""

    def activate_object(self, object_to_activate, player):
        description = ""
        result = (self, description, player)
        return result

    def examine_object(self, object_name):
        pass

    def set_leave_scene(self):
        self.is_first_visit = False
        self.fade_timer_acc = 0.0

    def reset_fade_timer(self):
        self.fade_timer_acc = 0.0

    def reboot_scene(self):
        self.is_first_visit = True
        self.fade_timer_acc = 0.0
        self.type_print_per_letter_timer_acc = 0.0
        self.type_letter_progress = 0
