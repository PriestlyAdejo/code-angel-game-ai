#!/usr/bin/python
# Shadowstone
# Code Angel

import sys
import os
import pygame
from pygame.locals import *
import random

import people_items

# Define the colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (22, 68, 152)
GREEN = (40, 180, 40)

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

PRINT_LINE_SIZE = 20
PRINT_BOX_MARGIN = 48

CARD_PADDING = 10
LEFT_MARGIN = 20
CARD_X = 220
DICE_X = 270
DICE_Y = 210
ITEM_X = [406, 482, 555]
CHOOSE_CARD_BOTTOM = 200

TURN_X = 258
PLAYER_TURN_Y = 165
OPPONENT_TURN_Y = 454

PAUSE_TIME = 2000
DICE_ROLL_TIME = 300

STRENGTH_ATTACK_MULTIPLIER = 2
DEXTERITY_ATTACK_MULTIPLIER = 1
WEAPON_ATTACK_MULTIPLIER = 3

STRENGTH_DEFENCE_MULTIPLIER = 0.5
DEXTERITY_DEFENCE_MULTIPLIER = 1
ARMOUR_DEFENCE_MULTIPLIER = 3

# Setup
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Shadowstone')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Helvetica', 16)
small_font = pygame.font.SysFont('Helvetica', 10)
large_font = pygame.font.SysFont('Helvetica', 32)

# Load images
background_image = people_items.load_image('general', 'background')
stats_box_image = people_items.load_image('general', 'stats_box')
message_box_image = people_items.load_image('general', 'message_box')
lge_message_box_image = people_items.load_image('general', 'lge_message_box')
player_box_image = people_items.load_image('general', 'player_box')

turn_image = people_items.load_image('general', 'turn')


def main():

    # Initialise variables
    level = 1
    opponent_weapon = ''
    player_weapon = ''

