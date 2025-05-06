"""
File: CollectNewspaperKarel.py
Name: jeff
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    karel will walk to the door of its house,
    picking up the beeper,
    and go back to its initial position,
    put the beeper down.
    """
    """
    pre:karel is in its house
    post:karel is out of its house,on the beeper
    """
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()
    pick_beeper()
    """
    pre:karel is on the beeper
    post:karel move back to his initial position,facing east
    """
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
     for i in range(3):
         turn_left()





# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
