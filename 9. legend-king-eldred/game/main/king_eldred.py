#!/usr/bin/python
# The Legend of King Eldred
# Code Angel

import map
import game_items

# Define constants
MAP_MAX_ROW = 7
MAX_MAP_COLUMN = 7
START_ROOM = '01'
END_ROOM = '24'


def main():

    # Initialise variables
    map_row = 0
    map_column = 0

    new_row = 0
    new_column = 0

    game_over = False
    alive = True

    room = ''

    gold = 0


