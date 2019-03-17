import time


class Null:
    def __init__(self):
        self.name = ""
        self.definition = ""
        self.stamina = 0
        self.speed = 0
        self.fairless = 0
        self.superSection = ""

    def show_definition(self):
        pass

    def level_one_intro(self):
        pass

class Ben:

    def __init__(self):
        self.name = "Ben"
        self.definition = "A guy who has a big not only soul, but also clothes." \
                     " \nIf you divide the hours he spent playing sports, the ones he spent on books \n "\
                      "- you get an infinitely small number." \
                     "\nBut extremely smart and never betray friends"
        self.stamina = 70
        self.speed = 50
        self.fairless = 80
        self.superSection = "brain"

    def show_definition(self):
        print(self.definition)
        time.sleep(1)
        print("Supersability - {}".format(self.superSection))

    def level_one_intro(self):
        print("Ben as usual spent time in the library.")
        time.sleep(1)
        print("Read \"History Derry \"")
        time.sleep(1)
        print("Suddenly a red balloon flew out of the vault ...")
        time.sleep(1)
        print("He beckoned Ben behind him ...")
        time.sleep(1)
        print("And Ben followed him.")
        time.sleep(1.5)
        print("The ball led him between the maze of shelving ...")
        time.sleep(1)
        print("Ben barely had time ...")
        time.sleep(1)
        print("Suddenly, the ball disappeared.")
        time.sleep(1)
        print("Ben looked around. He got lost in a maze. He was scared.")
        time.sleep(1)
        print("Suddenly, out of one closet looked out ... Clown ...")
        time.sleep(1)
        print("Pennnivais.")
        time.sleep(1)
        print("And Ben realized that it was time to wind up")
        time.sleep(1)


class Beverly:

    def __init__(self):
        self.name = "Beverly"
        self.definition = "A girl with fiery hair, maddening Bill and Ben. \nVolnoe, with a strong character -" \
                          "that's for sure who is not afraid of dangers"
        self.stamina = 80
        self.speed = 70
        self.fairless = 100
        self.superSection = "will"

    def show_definition(self):
        print(self.definition)
        time.sleep(1)
        print("Supersability - {}".format(self.superSection))

    def level_one_intro(self):
        print("Beverly went to the bathroom to wash after a hard day ...")
        time.sleep(1)
        print("She leaned over the sink and suddenly ...")
        time.sleep(1)
        print("Voices were heard from it ...")
        time.sleep(1)
        print("Children's voices ...")
        time.sleep(1)
        print("\" Beverly, we all fly here ... Come to us ... You will fly too \"")
        time.sleep(1)
        print("\" YOU WILL BE FLYING ALSO! ")
        time.sleep(1)
        print("And from the shell instantly there was a rush of blood.")
        time.sleep(1)
        print("She flooded everything: the bathroom became evenly burgundy in color and filled with the smell of steel")
        time.sleep(1)
        print("When Beverly departed from the shock for a second and turned around ...")
        time.sleep(1)
        print("She saw behind the curtain of the shower ...")
        time.sleep(1)
        print("PENNIVAISE")
        time.sleep(1)
        print("and realized that it was time to run!")


class Bill:

    def __init__(self):
        self.name = "Bill"
        self.definition = "That's exactly who wants to settle scores with the monster - so this is Bill." \
                          "\nYes, he is beautiful in everything, but there is a nuance: his determination and" \
                          "fearlessness can shatter memories of George ... \n" \
                          "There is a bike, so Usain Bolt sees only his back"
        self.stamina = 100
        self.speed = 100
        self.fairless = 100
        self.superSection = "speed"

    def show_definition(self):
        print(self.definition)
        time.sleep(1)
        print("Supersability - {}".format(self.superSection))

    def level_one_intro(self):
        print("Bill returned home on the bike late at night.")
        time.sleep(1)
        print("His bike, Silver, as Bill himself called him, was flying along the roads of Derry.")
        time.sleep(1)
        print("Although Silver was too big for a guy, Bill handled him well.")
        time.sleep(1)
        print("Some cars drove slower ... \n")
        time.sleep(1.5)
        print("Suddenly, out of the corner of his eye, Bill notices that above the water channel named Derry ...")
        time.sleep(1)
        print("A lot of colorful balloons fly.")
        time.sleep(1)
        print("More precisely, they stand. Even the wind does not wave them.")
        time.sleep(1)
        print("And a nasty clown pokes out of the water of the canal, and in a nasty voice suggests:")
        time.sleep(1)
        print("\" Bill, take the ball. You will fly. Georgie flies, and together you will FLY! \"")
        time.sleep(1)
        print("But Bill has not lost his composure and understood,")
        time.sleep(1)
        print("Need to run!")
        time.sleep(1)


bill = Bill()
beverly = Beverly()
ben = Ben()


def showDefinition(name):

    if name == "Bill":
        bill.show_definition()
    if name == "Beverly":
        beverly.show_definition()
    if name == "Ben":
        ben.show_definition()
