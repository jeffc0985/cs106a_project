"""
File: StoneMasonKarel.py
Name: jeff
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    karel will fill two columns of a building with beepers.
    pre:karel is at the left bottom of the building,facing east.
    post:karel is at the right bottom of the building, facing east.
    """
    while front_is_clear():
        turn_left()
        fill_the_column()
        detect()
        turn_right()
        move4()
        turn_right()
        fill_the_column()
        detect()
        turn_left()


def fill_the_column():
    """
    karel will fill a column with beepers.
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()


def detect():
    """
    karel will detect if it's on the beeper
    """
    if not on_beeper():
        put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def move4():
    for i in range(4):
        move()











# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
