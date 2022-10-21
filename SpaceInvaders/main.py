"""
* Taitotalo Python 21.10.2022
* main.py
* Python OOP Space Invaders
* Created by Samu Reinikainen
"""

import pygame as pg
import sys

class SpaceInvaders:
    def __init__(self):
        #initialize pygame
        pg.init()
        self.screen = pg.display.set_mode((1200,800))        
        pg.display.set_caption("Space Invaders")

    def run(self):
        #main loop
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()
    

def main():
    game = SpaceInvaders()
    game.run()


# run blocks of code only if our program is the main program executed
if __name__ == "__main__":
    main()