"""
File: PotholeFilling.py
Name: Jeff
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *


def main():
    for i in range(3):
        move()
        go_in()
        put_beepers99()
        go_out()
        turn_right()
        move()


def go_in():
    """
    pre-condition:karel is at the top of Pothhole,facing East
    """
    turn_right()
    move()


def go_out():
    """
    post-condition:karel is in the Pothhole,facing South
    """
    turn_back()
    move()


def turn_back():
    for i in range(2):
        turn_left()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
