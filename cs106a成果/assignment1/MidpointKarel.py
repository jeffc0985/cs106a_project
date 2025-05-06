"""
File: MidpointKarel.py
Name: jeff
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    karel will find the mid point of first row in a square world.
    """
    if not front_is_clear() and not left_is_clear():
        pass#如果世界是1*1
    else:
        while front_is_clear():
            if not on_beeper():
                move()
        put_beeper()
        turn_back_and_move()

        while front_is_clear():
            if not on_beeper():
                move()
        put_beeper()
        turn_back_and_move()#放左下右下兩個角


        while not on_beeper():
            cycle()

        pick_beeper()
        turn_back_and_move()#剩相鄰兩個，回收一個

def cycle():
    #先右邊內縮，再左邊內縮
    while front_is_clear() and not on_beeper():
        move()
    pick_beeper()
    turn_back_and_move()
    put_beeper()
    move()
    #post-cond1:not on beeper---繼續縮
    #post-cond2:on beeper---break


def turn_back_and_move():
    turn_left()
    turn_left()
    move()








# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
