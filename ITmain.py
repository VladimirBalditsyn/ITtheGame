#It's main game file

import time
import GameLevels
import English
import os
import sys

from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command


def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if system_name().lower() == "windows" else "clear"

    # Action
    system_call(command)




class Game:

    '''The main logic of the game'''

    intro = [
        "IIIIIII  TTTTTTT",
        "   I        T   ",
        "   I        T   ",
        "   I        T   ",
        "   I        T   ",
        "   I        T   ",
        "   I        T   ",
        "   I        T   ",
        "IIIIIII     T   ",
        "\nBased on S.King novel\n"
    ]

    def __init__(self):
        self.languages = ["russian", "english"]
        for i in self.intro:
            print(i)
            time.sleep(0.3)
        time.sleep(0.5)
        s = input("Please, choose suitable language:\n"
                  "Russian or English (it's very fun, cos texts "
                  "translated by Google Translate)\n")
        while True:
            if s.lower() in self.languages:
                game = GameLevels.GameStart(s.lower())
                break
            else:
                print("\nSorry, I don't know this language.\nTry once more")
                s = input()

        game.hello()
        clear_screen()
        game.prologue()
        game.choose_character()
        time.sleep(2)
        clear_screen()
        game.level_one()
        clear_screen()
        game.level_two()


Game()
