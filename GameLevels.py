import time
import random
import Characters
import Tools
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
    Tools.right_import(language)
    global LB
    LB = languages[language]()


class GameStart:

    def __init__(self, language):

        right_import(language)
        self.tool = None
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
        s = input(LB.Skip_level_one)

        if s == LB.Yes:
            return

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
            self.run(10, 3.5)

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

            self.run(6, 2.5)

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

    def penny_attac(self, flag):
        i = random.randint(0, len(LB.Penny_attac_phrases) - 1)
        print(LB.Level_two_too_slow)
        print(LB.Penny_attac_phrases[i])
        print(LB.Press_enter)
        self.character.stamina -= 5
        flag[0] = True

    def kill(self, penny_health, limit):
        flag = [True]
        while penny_health > limit and self.character.stamina > 0:
            timeout = 4 * self.character.speed / 100
            flag = [False]
            t = Timer(timeout, self.penny_attac, [flag])
            t.start()
            i = random.randint(0, len(self.tool.commands) - 1)
            prompt = "{}!\n".format(self.tool.commands[i])
            answer = input(prompt)

            t.cancel()

            if flag[0]:
                t.cancel()
                pass
            elif answer.lower() != self.tool.commands[i].lower():
                print(LB.Penny_attac_phrases[i % len(LB.Penny_attac_phrases)])
                self.character.stamina -= 5
                print(LB.Your_health.format(self.character.stamina))
            else:
                penny_health -= self.tool.force
                print(LB.Penny_hurt_phrases[i % len(
                    LB.Penny_hurt_phrases)].format(self.tool.force))

        return penny_health

    def level_two(self):
        print(LB.Level_two)
        time.sleep(1)
        flag = False

        tool_base = {k: v(self.character) for k, v in Tools.Tool_Base.items()}

        for i in LB.Level_two_intro:
            print(i)
            time.sleep(1.5)

        time.sleep(2)
        clear_screen()

        for i in LB.Level_two_choose_tool:
            print(i)
            time.sleep(1)

        time.sleep(1)
        for i in tool_base.values():
            print(i.name)
            time.sleep(0.5)
            print(i.definition)
            time.sleep(2)
            print('\n')

        print(LB.Your_tool_choice)

        while True:
            s = input()
            for k, v in LB.Tool_names.items():
                if v.lower() == s.lower():
                    self.tool = tool_base[k]
                    print('\n')
                    print(LB.Tool_choice_congrats[k])
                    time.sleep(1)
                    flag = True
                    break

            if flag:
                break

            print(LB.Tool_wrong_input)

        clear_screen()

        for i in LB.Level_two_rules:
            print(i)
            time.sleep(1.5)

        input()

        clear_screen()

        your_start_health = self.character.stamina
        penny_health = 100
        while True:
            penny_health = self.kill(penny_health, 50)

            if self.character.stamina > 0:
                print(LB.Level_two_congrats[0])
                break
            else:
                print(LB.Level_two_fail[0])
                self.character.stamina = your_start_health
                time.sleep(3)
                clear_screen()

        print(LB.Broken_tool.format(self.tool.name.lower()))
        for i in tool_base.values():
            if i.name != self.tool.name:
                print(i.name)
                time.sleep(0.5)

        while True:
            timeout = 10 * self.character.speed / 100
            flag = [False]
            t = Timer(timeout, self.penny_attac, [flag])
            t.start()

            i = random.randint(0, len(LB.Penny_attac_phrases) - 1)
            answer = input()

            t.cancel()

            if flag[0]:
                t.cancel()
                pass
            else:
                flag[0] = True
                for k, v in LB.Tool_names.items():
                    if v.lower() == answer.lower() and answer.lower() != \
                            self.tool.name.lower():
                        self.tool = tool_base[k]
                        print('\n')
                        print(LB.Tool_choice_congrats[k])
                        flag[0] = False
                        break

                if flag[0]:
                    print(LB.Tool_wrong_input)
                    print(LB.Penny_attac_phrases[i])
                    self.character.stamina -= 5
                    print(LB.Your_health.format(self.character.stamina))
                else:
                    break

        your_start_health = self.character.stamina

        while True:
            penny_health = self.kill(penny_health, 0)

            if self.character.stamina > 0:
                print(LB.Level_two_congrats[1])
                break
            else:
                print(LB.Level_two_fail[1])
                self.character.stamina = your_start_health
                time.sleep(3)
                clear_screen()

        time.sleep(1)

        clear_screen()

        for i in LB.You_win:
            print(i)
            time.sleep(1)
        time.sleep(2)
