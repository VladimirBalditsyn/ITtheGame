import time
import CharactersEng
import random
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


class GameStart:

    def __init__ (self):
        self.commands = ["Run", "Turn left", "Turn right", "Knock down", "Jump up"]
        self.answers = ["run", "left", "right", "down", "up"]
        self.character = CharactersEng.Null()

    def hello(self):
        print("\nCool, let's get started! \n")
        time.sleep(1)

    def prologue(self):
        print("Welcome to Derry! \n \n")
        time.sleep(2)
        print("Dear town, whose anthem could begin with the words:")
        time.sleep(1.5)
        print("\" Simple people live here, my friends live here ... \"")
        time.sleep(1.5)
        print("If the city did not live ... \n")
        time.sleep(2)
        print("IT. \n")
        time.sleep(2)
        print("Every 28 years it comes out of hell and settles in the sewers of this city ...")
        time.sleep(1.5)
        print("And today IT again woke up and kidnapped baby Georgie. \n")
        time.sleep(1.5)
        print("But George's brother - Bill - is not ready to put up with it.")
        time.sleep(1.5)
        print("He wants to stop the monster.")
        time.sleep(1.5)
        print("Only he, Zaika Bill, the beautiful Beverly, the fat Ben and their friends are able to stop Penny ...")
        time.sleep(1.5)
        print("But can they? \n")
        time.sleep(3)

    def choose_character(self):
        print("\n Now it’s time to choose a character. \n Who do you want to be, a desperate hero? Mike, Ben or"
              "maybe Beverly?)")
        time.sleep(1)
        print("\n \n Enter \" learn about \" and the name of the character( for example, learn out about Bill)"
              " to get information about him \n "
              "or  \" I \" and the name of the character ( for example, I am Bill) to be in his shoes \n")
        s = input()
        while True:
            if s.lower() == 'learn about bil':
                CharactersEng.showDefinition('Bill')
                s = input("\nWhat else do you want? \n")
            elif s.lower() == 'learn about beverly':
                CharactersEng.showDefinition('Beverly')
                s = input("\nWhat else do you want? \n")
            elif s.lower() == 'learn about ben':
                CharactersEng.showDefinition('Ben')
                s = input("\nWhat else do you want? \n")
            elif s.lower() == 'i am bill':
                print("Penny will beg for mercy! \n")
                self.character = CharactersEng.Bill()
                break
            elif s.lower() == 'i am beverly':
                print("Fire-girl !!! \n")
                self.character = CharactersEng.Beverly()
                break
            elif s.lower() == 'i am ben':
                print("A good choice. Ben is cool, though not \n")
                self.character = CharactersEng.Ben()
                break
            else:
                print("Hmm ... You want something I don’t know. \nGet up and try again \n")
                s = input()

    def time_end(self, flag):
        print('\nToo slow! Press Enter to continue')
        self.character.stamina -= 5
        flag[0] = True

    def run(self, count, timeout):
        while self.character.stamina > 0 and count > 0:
            timeout = timeout * self.character.speed / 100
            flag = [False]
            t = Timer(timeout, self.time_end, [flag])
            t.start()
            i = random.randint(0, 4)
            prompt = "{}! \n" .format(self.commands [i])
            answer = input(prompt)
            if flag[0]:
                t.cancel()
                pass
            elif answer.lower() != self.answers[i]:
                if i in [0, 3, 4]:
                    print('You stumbled, -5XP \n')
                    self.character.stamina -= 5
                elif i in [1, 2]:
                    print('You turned the wrong way, -5XP \n')
                    self.character.stamina -= 5
            else:
                count -= 1

            t.cancel()

    def level_one(self):
        time.sleep(1)
        print("Level 1. Chase")

        time.sleep(1)
        self.character.level_one_intro()

        time.sleep(3)

        clear_screen()

        print("The rules are simple: \n"
              "Commands will appear on the screen, according to which you will need to enter the word \n"
              "to escape Penny. Here they are:")
        for i in range(5):
            print("{} ---> {}". format(self.commands[i], self.answers[i]))
        time.sleep(1.5)
        print("\nBe careful, my friend. \n"
              "Any mistake will bring Pennvayze close to you and take 5XP of precious health \n"
              "It’s also important to enter teams quickly, otherwise Penny will be able to reach you \n"
              "And you will lose 5XP again \ n \ n"
              "The time allotted for the answer depends on the speed of your character:")
        time.sleep(0.5)
        print("Your speed: {}". format(self.character.speed))
        print("Your Health: {}". format(self.character.stamina))
        time.sleep(1)
        print("Do not forget to press ENTER  after entering the answer")
        input("If you feel the strength to start, my friend, press ENTER and good luck! \n")
        clear_screen()

        while True:
            self.run(10, 8)

            if self.character.stamina > 0:
                print("You're doing great! It's time to speed up!")
                print("Your Health: {}".format(self.character.stamina))
                time.sleep(2)
                clear_screen()
            else:
                print("Oooh nooo !!! \n"
                      "Pennyzvez delicious lunch. And you try again.")
                time.sleep(2)
                clear_screen()
                pass

            self.run(8, 6)

            if self.character.stamina > 0:
                print("Well, you are well done! Now you are close to the exit like never before!")
                print("Your Health: {}".format(self.character.stamina))
                time.sleep(2)
                clear_screen()
            else:
                print("Oooh nooo !!! \n"
                      "Life is cruel, like Penny Pipes today. And you try again.")
                time.sleep(2)
                clear_screen()
                pass

            self.run(6, 4)

            if self.character.stamina > 0:
                print("You're an athlete, it turns out!")
                print("You successfully hid from this monster!")
                print("Let's see what's waiting for you next!")
                time.sleep(3)
                clear_screen()
                break

            else:
                print("Oooh nooo !!! \n"
                      "Victory was so close ... Let's do it one more time.")
                time.sleep(2)
                clear_screen()
                pass
