"""
File: CheckerboardKarel.py
Name: jeff
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    put_beeper()
    go_east()
    while front_is_clear():
        #如果大於一列
        #pre-cond:在該列最東向北
        if on_beeper():#該列奇數格
            move()
            go_west()
        else:#偶數格
            move()
            put_beeper()
            go_west()
        #post-cond:停在(2，1)向北，沒beeper

        if front_is_clear():
            if on_beeper():
                move()
                go_east()
            else:#去東，回到pre-cond
                move()
                put_beeper()
                go_east()


def go_east():
    #從西到東填一列，到牆壁後停下，轉向北

    while not facing_east():
        turn_right()
    fill_one_row_beeper()
    turn_left()


def go_west():
    #從東到西填一列，到牆壁後停下，轉向北

    while not facing_west():
        turn_left()
    fill_one_row_beeper()
    turn_right()


def fill_one_row_beeper():#填一列
    while front_is_clear():
        if on_beeper():
            move()
        else:
            move()
            put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
