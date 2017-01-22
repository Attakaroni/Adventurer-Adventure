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

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ADVENTURER_IMAGE_FORWARD = pygame.image.load("adventurer_forward.png")
ADVENTURER_IMAGE_LEFT = pygame.image.load("adventurer_left.png")
ADVENTURER_IMAGE_BACK = pygame.image.load("adventurer_back_0.png")
ADVENTURER_IMAGE_RIGHT = pygame.image.load("adventurer_right.png")

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

def display(screen, image, hitbox):
    screen.blit(image, hitbox)

def render(screen, game):
<<<<<<< HEAD
    screen.fill(game['background']['color'])
    rect = pygame.Rect(game['adventurer']['x'] - game['adventurer']['x_size'] / 2, game['adventurer']['x_size'], game['adventurer']['y'] - game['adventurer']['y_size'] / 2, game['adventurer'])
    display(screen, game['adventurer']['image']['back'], rect)
    pygame.display.flip 

def reset():
    game = {'mode': "Run", 'background': {'color': BLACK},
            'adventurer': {'x_size': 32, 'y_size': 32, 'x': 0, 'y': 0,
                           'image': {'forward': ADVENTURER_IMAGE_FORWARD, 'left': ADVENTURER_IMAGE_FORWARD, 'back': ADVENTURER_IMAGE_BACK, 'right': ADVENTURER_IMAGE_RIGHT}}}
=======
    screen.fill(game['background']['background_color'])
    #pygame.display.flip()

    tilesize = 10
    roomsize = len(game['room'])
    for y, row in enumerate(game['room']):
        for x, cell in enumerate(game['room'][y]):
            if cell or True:
                pygame.draw.rect(screen, (abs(x-roomsize)/roomsize*255, abs(y-roomsize)/roomsize*255, abs(x-y)/roomsize*255), (tilesize * x, tilesize * y, tilesize, tilesize))
    pygame.display.flip()
                

def reset():
    game = {'mode': "Run", 'background': {'background_color': BLACK}, 'room': generate_room(30)}
>>>>>>> origin/master
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

def generate_room(dim):# dim: dimensions of room
    room = [0] * dim
    for y in range(0,dim):
        room[y] = [0] * dim
        for x in range(0,dim):
            room[y][x] = 0
    for i in range(0,dim):
        room[0][i] = 1
        room[-1][i] = 1
        room[i][0] = 1
        room[i][-1] = 1
        
    for i in range(0,dim):
        print(room[i])
    return room

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
