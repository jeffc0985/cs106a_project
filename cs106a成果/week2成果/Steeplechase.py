"""
File: Steeplechase.py
Name: Jeff
---------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses 7 hurdles in a 12x12 world
    """
    for i in range(7):
        if front_is_clear():
            """
            2 tiles
            """
            move()
            jump()
        else:
            """
            1 tile 
            """
            jump()

def jump():
    """
    pre-condition:karel is on the left of the wall,facing east
    post-condition:karel is on the right of wall,facing east
    """
    up()
    cross()
    down()


def up():
    """
    pre-condition:karel is on the left of the wall,facing east
    post-condition:karel is at the upper left of the wall,facing north
    """
    turn_left()
    while not right_is_clear():
        move()
    # alternative:
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()


def cross():
    """
    pre-condition:karel is at the upper left of the wall,facing north
    post-condition:karel is at the upper right of the wall,facing south
    """
    turn_right()
    move()
    turn_right()


def down():
    """
    pre-condition:karel is at the upper right of the wall,facing south
    post-condition:karel is at the bottom,facing east
    """
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()





# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
