import time
import random
import Characters
from threading import Timer
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


def import_eng():
    import EngLanguageBase
    return EngLanguageBase


def import_rus():
    import RusLanguageBase
    return RusLanguageBase


languages = {"russian": import_rus, "english": import_eng}

LB = None

def right_import(language):
    Characters.right_import(language)
    global LB
    LB = languages[language]()


class GameStart:

    def __init__(self, language):

        right_import(language)
        self.commands = LB.Level_one_commands
        self.answers = LB.Level_one_answers
        self.character = Characters.Null()
        self.character_variants = {
            LB.Choose_character_commands[0]: self.learn_bill,
            LB.Choose_character_commands[1]: self.learn_ben,
            LB.Choose_character_commands[2]: self.learn_beverly,
            LB.Choose_character_commands[3]: self.set_bill,
            LB.Choose_character_commands[4]: self.set_ben,
            LB.Choose_character_commands[5]: self.set_beverly
        }

    def hello(self):
        print(LB.Hello)
        time.sleep(1)

    def prologue(self):
        for i in LB.Prologue:
            print(i)
            time.sleep(1.5)
        time.sleep(1)

    # I can't pack next functions into something more compact
    # without increasing code in another place.
    # If you need to add character,
    # you should just add learn_ function and set_ function and add
    # character "set" and "learn" commands in "character_variants"
    def learn_bill(self):
        print('\n')
        Characters.show_definition('Bill')
        s = input(LB.What_else)
        return s

    def learn_ben(self):
        print('\n')
        Characters.show_definition('Ben')
        s = input(LB.What_else)
        return s

    def learn_beverly(self):
        print('\n')
        Characters.show_definition('Beverly')
        s = input(LB.What_else)
        return s

    def set_bill(self):
        print('\n')
        print(LB.Bill_set)
        self.character = Characters.Bill()
        return True

    def set_ben(self):
        print('\n')
        print(LB.Ben_set)
        self.character = Characters.Ben()
        return True

    def set_beverly(self):
        print('\n')
        print(LB.Beverly_set)
        self.character = Characters.Beverly()
        return True

    def choose_character(self):
        for i in LB.Choose_character_instruction:
            print(i)
            time.sleep(0.7)
        s = input()

        while True:
            if s.lower() in self.character_variants.keys():
                s = self.character_variants[s.lower()]()
                if isinstance(s, bool):
                    break
            else:
                print(LB.Wrong_command)
                s = input()

    def time_end(self, flag):
        print(LB.Too_slow)
        self.character.stamina -= 5
        flag[0] = True

    def run(self, count, timeover):
        while self.character.stamina > 0 and count > 0:
            timeout = timeover * self.character.speed / 100
            flag = [False]
            t = Timer(timeout, self.time_end, [flag])
            t.start()
            i = random.randint(0, 4)
            prompt = "{}!\n".format(self.commands[i])
            answer = input(prompt)

            t.cancel()

            if flag[0]:
                t.cancel()
                pass

            elif answer.lower() != self.answers[i]:
                if i in [0, 3, 4]:
                    print(LB.Wrong_step)
                    self.character.stamina -= 5
                elif i in [1, 2]:
                    print(LB.Wrong_turn)
                    self.character.stamina -= 5
            else:
                count -= 1

    def level_one(self):
        time.sleep(1)
        print(LB.Level_one)

        time.sleep(1)
        self.character.level_one_intro()

        time.sleep(3)

        clear_screen()

        print(LB.Level_one_rules[0])

        for i in range(len(self.commands)):
            print("{}    --->    {}".format(self.commands[i], self.answers[i]))
        time.sleep(2)

        print(LB.Level_one_rules[1])
        time.sleep(0.5)

        print(LB.Your_speed.format(self.character.speed))
        print(LB.Your_health.format(self.character.stamina))
        time.sleep(1)
        print(LB.Level_one_rules[2])
        input(LB.Level_one_rules[3])
        clear_screen()

        start_stamina = self.character.stamina

        while True:
            self.run(10, 4)

            if self.character.stamina > 0:
                print(LB.Level_one_congrats[0])
                print(LB.Your_health.format(self.character.stamina))
                time.sleep(2)
                clear_screen()
                break
            else:
                print(LB.Level_one_restarts[0])
                time.sleep(3)
                clear_screen()
                self.character.stamina = start_stamina
                pass

        while True:
            self.run(10, 3)

            if self.character.stamina > 0:
                print(LB.Level_one_congrats[1])
                print(LB.Your_health.format(self.character.stamina))
                time.sleep(2)
                clear_screen()
                break
            else:
                print(LB.Level_one_restarts[1])
                time.sleep(4)
                clear_screen()
                self.character.stamina = start_stamina
                pass

        while True:

            self.run(6, 2)

            if self.character.stamina > 0:

                print(LB.Level_one_congrats[2])
                time.sleep(3)
                clear_screen()
                break
            else:
                print(LB.Level_one_restarts[2])
                time.sleep(4)
                clear_screen()
                self.character.stamina = start_stamina
                pass
