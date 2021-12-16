import os

import pygame
from pygame.locals import *
import pygame_gui
import sys

from core.functions import try_scene_change
from core.functions import activate_object

# Tampere scenet
import scenes.scene1_alku as s1
import scenes.tampere.scene2_tampere as s2
import scenes.tampere.scene6_tampere_hotelli as s6
import scenes.tampere.scene7_tampere_yoelama as s7
import scenes.tampere.scene8_tampere_hotelli_hatanpaa as s8
import scenes.tampere.scene9_tampere_hotelli_pyynikki as s9
import scenes.tampere.scene10_tampere_yoelama_shotti as s10
import scenes.tampere.scene11_tampere_yoelama_olut as s11
import scenes.tampere.scene12_tampere_hotelli_pyynikki_aamu as s12
import scenes.tampere.scene13_tampere_hotelli_pyynikki_yo as s13
import scenes.tampere.scene14_tampere_hotelli_pyynikki_yo_piiloudu as s14
import scenes.tampere.scene15_tampere_hotelli_pyynikki_yo_kaiva as s15
import scenes.tampere.scene16_tampere_hotelli_pyynikki_yo_kaiva_avaimet as s16
import scenes.tampere.scene17_tampere_hotelli_pyynikki_yo_kaiva_aarre as s17
import scenes.tampere.scene18_tampere_hotelli_pyynikki_aamu_huippu as s18
import scenes.tampere.scene19_tampere_hotelli_pyynikki_aamu_juuri as s19

#Turku scenet
import scenes.turku.scene20_turku as s20
import scenes.turku.scene21_turku_hotelli as s21
import scenes.turku.scene22_turku_yoelama as s22
import scenes.turku.scene23_turku_turunlinna as s23
import scenes.turku.scene24_turku_vankila as s24
import scenes.turku.scene25_turku_turunlinna_sivuovi as s25
import scenes.turku.scene26_turku_turunlinna_sivuovi_juokse as s26
import scenes.turku.scene27_turku_turunlinna_sivuovi_kerro as s27
import scenes.turku.scene28_turku_turunlinna_sivuovi_kerro_kurkista as s28
import scenes.turku.scene29_turku_turunlinna_sivuovi_kerro_jatka as s29
import scenes.turku.scene30_turku_vankila_pihamaa as s30
import scenes.turku.scene31_turku_vankila_pihamaa_lapio as s31
import scenes.turku.scene32_turku_vankila_pihamaa_lapio_sisaan as s32
import scenes.turku.scene33_turku_vankila_pihamaa_lapio_pois as s33
import scenes.turku.scene34_turku_vankila_pihamaa_muualta as s34
import scenes.turku.scene35_turku_vankila_rakennus as s35
import scenes.turku.scene36_turku_vankila_rakennus_tikkaat as s36
import scenes.turku.scene37_turku_vankila_rakennus_tikkaat_uudestaan as s37
import scenes.turku.scene38_turku_vankila_rakennus_tikkaat_uudestaan_tutki as s38
import scenes.turku.scene39_turku_vankila_toinen_reitti as s39
import scenes.turku.scene40_turku_vankila_toinen_reitti_lampi as s40
import scenes.turku.scene41_turku_yoelama_kalja as s41
import scenes.turku.scene42_turku_yoelama_shotti as s42
import scenes.turku.scene43_turku_yoelama_shotti_lisaa as s43
import scenes.turku.scene44_turku_yoelama_shotti_lisaa_jahti as s44

import scenes.scene100_voitto as s100
import scenes.scene101_havio as s101


class Player:
    def __init__(self):
        self.game_over = False


# Lisätään musiikki
file = 'Aarteenetsintä.wav'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

# Määritetään peliruutu
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption('Aarteenetsintä')
screen = pygame.display.set_mode((640, 480))
width = screen.get_width()
height = screen.get_height()

# Määritetään buttonin värit
color = (255,255,255)
color_light = (170,170,240)
color_dark = (100,100,100)

# Määritetään buttonin teksti
smallfont = pygame.font.SysFont('Corbel', 40)
text = smallfont.render('A', True, color)
text2 = smallfont.render('B', True, color)
text3 = smallfont.render('C', True, color)

# Otetaan tyyli käyttöön
ui_manager = pygame_gui.UIManager((640, 480), "data/ui_theme.json")
ui_manager.add_font_paths('agency', "data/AGENCYB.TTF")
ui_manager.preload_fonts([{'name': 'agency', 'point_size': 18, 'style': 'regular'},
                          {'name': 'gabriola', 'point_size': 18, 'style': 'bold'},
                          {'name': 'gabriola', 'point_size': 18, 'style': 'italic'}])

# Määritetään logo
programIcon = pygame.image.load('treasure.png')
pygame.display.set_icon(programIcon)

have_started = False
scenes = []

# Helsinki
scene_1 = s1.SceneOne()
scenes.append(scene_1)

# Tampere
scenes.append(s2.SceneTampere())
scenes.append(s6.SceneTampereHotelli())
scenes.append(s7.SceneTampereYoelama())
scenes.append(s8.SceneTampereHotelliHatanpaa())
scenes.append(s9.SceneTampereHotelliPyynikki())
scenes.append(s10.SceneTampereYoelamaShotti())
scenes.append(s11.SceneTampereYoelamaOlut())
scenes.append(s12.SceneTampereHotelliPyynikkiAamu())
scenes.append(s13.SceneTampereHotelliPyynikkiYo())
scenes.append(s14.SceneTampereHotelliPyynikkiYoPiiloudu())
scenes.append(s15.SceneTampereHotelliPyynikkiYoKaiva())
scenes.append(s16.SceneTampereHotelliPyynikkiYoKaivaAvaimet())
scenes.append(s17.SceneTampereHotelliPyynikkiYoKaivaAarre())
scenes.append(s18.SceneTampereHotelliPyynikkiAamuHuippu())
scenes.append(s19.SceneTampereHotelliPyynikkiAamuJuuri())

# Turku
scenes.append(s20.SceneTurku())
scenes.append(s21.SceneTurkuHotelli())
scenes.append(s22.SceneTurkuYoelama())
scenes.append(s23.SceneTurkuTurunlinna())
scenes.append(s24.SceneTurkuVankila())
scenes.append(s25.SceneTurkuTurunlinnaSivuovi())
scenes.append(s26.SceneTurkuTurunlinnaSivuoviJuokse())
scenes.append(s27.SceneTurkuTurunlinnaSivuoviKerro())
scenes.append(s28.SceneTurkuTurunlinnaSivuoviKerroKurkista())
scenes.append(s29.SceneTurkuTurunlinnaSivuoviKerroJatka())
scenes.append(s30.SceneTurkuVankilaPihamaa())
scenes.append(s31.SceneTurkuVankilaPihamaaLapio())
scenes.append(s32.SceneTurkuVankilaPihamaaLapioSisaan())
scenes.append(s33.SceneTurkuVankilaPihamaaLapioPois())
scenes.append(s34.SceneTurkuVankilaPihamaaMuualta())
scenes.append(s35.SceneTurkuVankilaRakennus())
scenes.append(s36.SceneTurkuVankilaRakennusTikkaat())
scenes.append(s37.SceneTurkuVankilaRakennusTikkaatUudestaan())
scenes.append(s38.SceneTurkuVankilaRakennusTikkaatUudestaanTutki())
scenes.append(s39.SceneTurkuVankilaToinenReitti())
scenes.append(s40.SceneTurkuVankilaToinenReittiLampi())
scenes.append(s41.SceneTurkuYoelamaKalja())
scenes.append(s42.SceneTurkuYoelamaShotti())
scenes.append(s43.SceneTurkuYoelamaShottiLisaa())
scenes.append(s44.SceneTurkuYoelamaShottiLisaaJahti())

# Häviö/Voitto
scenes.append(s100.SceneVoitto())
scenes.append(s101.SceneHavio())


active_scene = scene_1

player = Player()

# Vastaanotetaan input
def parse(input_text):
    command = input_text.lower()
    object1 = None
    object2 = None

    return command, object1, object2


# Ohjataan input funktion käyttöön
def process_command(command, object1, object2):
    global have_started
    global active_scene
    global player

    output = "Paina enter-näppäintä aloittaaksesi"
    if have_started:
        output = "Virheellinen komento, yritä uudestaan painamalla 'enter'"

    if command == "":
        active_scene.reset_fade_timer()
        output = active_scene.get_description(player)
        if not have_started:
            active_scene.reboot_scene()
            have_started = True
        else:
            active_scene.is_first_visit = False

    elif have_started:
        if command == "a":
            result = try_scene_change(active_scene, scenes, command, player)
            active_scene = result[0]
            output = result[1]
        elif command == "b":
            result = try_scene_change(active_scene, scenes, command, player)
            active_scene = result[0]
            output = result[1]
        elif command == "c":
            result = try_scene_change(active_scene, scenes, command, player)
            active_scene = result[0]
            output = result[1]


    return output


# Ekan ikkunan sisältö
adventure_output = ("<font face='agency' size=5>Tervetuloa Aarteenmetsästykseen!</font>"
                    "<br><br>"
                    "Seuraa oikeaa polkua ja löydä palkinto. Onnea matkaan!"
                    "<br><br>"
                    "Paina enteriä jatkaaksesi")
entered_keys = ""

# Input-kenttä
ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                              pygame.Rect((10, 10), (620, 300)),
                                              manager=ui_manager,
                                              object_id="#scene_text")
ui_scene_text.set_active_effect("typing_appear")
player_text_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((1, 480), (640, 480)),
                                                        manager=ui_manager,
                                                        object_id="#player_input")

ui_manager.select_focus_element(player_text_entry)


# Peli pyörii
running = True
clock = pygame.time.Clock()

while running:
    frameTime = clock.tick(60)
    time_delta = frameTime / 1000.0

    # Peli pysähtyy
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        # Events
        ui_manager.process_events(event)

        # Komennot tekstillä
        if event.type == USEREVENT:
            if event.user_type == "ui_text_entry_finished":
                entered_keys = event.text
                parsed_command = parse(entered_keys)
                adventure_output = process_command(parsed_command[0], parsed_command[1], parsed_command[2])
                ui_scene_text.kill()
                ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                                              pygame.Rect((10, 10), (620, 300)),
                                                              manager=ui_manager,
                                                              object_id="#scene_text")
                if active_scene.is_first_visit and entered_keys != 'apua':
                    ui_scene_text.set_active_effect("typing_appear")
                player_text_entry.set_text("")

        # Komennot buttoneilla
        if event.type == pygame.MOUSEBUTTONDOWN:
            # A
            if 45 <= mouse[0] <= 185 and 347 <= mouse[1] <= 387:

                adventure_output = process_command("a", parsed_command[1], parsed_command[2])
                ui_scene_text.kill()
                ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                                              pygame.Rect((10, 10), (620, 300)),
                                                              manager=ui_manager,
                                                              object_id="#scene_text")
                if active_scene.is_first_visit:
                    ui_scene_text.set_active_effect("typing_appear")
                player_text_entry.set_text("")

            # B
            elif 245 <= mouse[0] <= 385 and 347 <= mouse[1] <= 387:

                adventure_output = process_command("b", parsed_command[1], parsed_command[2])
                ui_scene_text.kill()
                ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                                              pygame.Rect((10, 10), (620, 300)),
                                                              manager=ui_manager,
                                                              object_id="#scene_text")
                if active_scene.is_first_visit:
                    ui_scene_text.set_active_effect("typing_appear")
                player_text_entry.set_text("")

            # C
            elif 445 <= mouse[0] <= 585 and 347 <= mouse[1] <= 387:

                adventure_output = process_command("c", parsed_command[1], parsed_command[2])
                ui_scene_text.kill()
                ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                                              pygame.Rect((10, 10), (620, 300)),
                                                              manager=ui_manager,
                                                              object_id="#scene_text")
                if active_scene.is_first_visit:
                    ui_scene_text.set_active_effect("typing_appear")
                player_text_entry.set_text("")


    # Tallentaa hiiren sijainnin mouse-muuttujaan
    mouse = pygame.mouse.get_pos()

    if ui_manager.select_focused_element != player_text_entry:
        ui_manager.unselect_focus_element()
        ui_manager.select_focus_element(player_text_entry)

    # Tämänhetkisen scenen background
    screen.blit(active_scene.background, (0, 0))

    # Button muuttuu tummasta vaaleaksi kun siinä hoveraa
    # A
    if 45 <= mouse[0] <= 185 and 347 <= mouse[1] <= 387:
        pygame.draw.rect(screen, color_light, [45, 347, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [45, 347, 140, 40])
    # B
    if 245 <= mouse[0] <= 385 and 347 <= mouse[1] <= 387:
        pygame.draw.rect(screen, color_light, [245, 347, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [245, 347, 140, 40])
    # C
    if 445 <= mouse[0] <= 585 and 347 <= mouse[1] <= 387:
        pygame.draw.rect(screen, color_light, [445, 347, 140, 40])
    else:
        pygame.draw.rect(screen, color_dark, [445, 347, 140, 40])

    # Width + 140, Height + 40

    # Lisätään teksti buttoniin
    screen.blit(text, (100, 350))
    screen.blit(text2, (300, 350))
    screen.blit(text3, (500, 350))

    # Päivittää framet
    pygame.display.update()

    active_scene.update(time_delta)
    ui_manager.update(time_delta)

    active_scene.render_back(screen)
    ui_manager.draw_ui(screen)
    active_scene.render_front(screen)

    # piirtää sisällön ruudulle
    pygame.display.flip()

# Lopettaa pelin suorittamisen
pygame.quit()
