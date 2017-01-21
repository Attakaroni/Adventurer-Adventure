# adventurer_adventure.py
# Attakaroni
# Vitridax
# Wyzat

import pygame
import sys
import traceback
import random

pygame.init()

WINDOW_SIZE = 768
FPS = 64

def play_music(track):
    pygame.mixer.music.load(track)
    pygame.mixer.play(-1)

def stop_music():
    pygame.mixer.music.stop()

def update(game):
    pass

def handle_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game['mode'] = "Quit"

    pressed = pygame.key.get_pressed()

def render(screen, game):
    pass

def reset():
    game = {'mode': "Run"}
    return game

def setup():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Adventurer Adventure")
    clock = pygame.time.Clock()
    game = reset()
    #play_music(game['music'])
    return screen, clock, game

def unsetup():
    stop_music()

def main():
    screen, clock, game = setup()
    while game['mode'] == "Run":
        handle_events(game)
        update(game)
        render(screen, game)
        clock.tick(FPS)
    unsetup()

try:
    main()
except Exception as e:
    for frame in traceback.extract_tb(sys.exc_info()[2]):
        fname, lineno, fn, text = frame
        print("You screwed up in %s on line %d" % (fname, lineno))
    print(sys.exc_info())
finally:
    pygame.quit()
    sys.exit
