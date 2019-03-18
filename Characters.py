import time


def import_eng():
    import EngLanguageBase
    return EngLanguageBase


def import_rus():
    import RusLanguageBase
    return RusLanguageBase


languages = {"russian": import_rus, "english": import_eng}


LB = None


def right_import(language):
    global LB
    LB = languages[language]()


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
        self.definition = LB.Ben_definition
        self.stamina = 70
        self.speed = 50
        self.fairless = 80

    def show_definition(self):
        print(self.definition)
        time.sleep(1)

    def level_one_intro(self):
        for i in LB.Ben_intro_level_one:
            print(i)
            time.sleep(1)


class Beverly:
    def __init__(self):
        self.definition = LB.Beverly_definition
        self.stamina = 80
        self.speed = 70
        self.fairless = 100

    def show_definition(self):
        print(self.definition)
        time.sleep(1)

    def level_one_intro(self):
        for i in LB.Beverly_intro_level_one:
            print(i)
            time.sleep(1)

class Bill:

    def __init__(self):
        self.definition = LB.Bill_definition
        self.stamina = 100
        self.speed = 100
        self.fairless = 100

    def show_definition(self):
        print(self.definition)
        time.sleep(1)

    def level_one_intro(self):
        for i in LB.Bill_intro_level_one:
            print(i)
            time.sleep(1)


characters = {"Bill": Bill, "Ben": Ben, "Beverly": Beverly}


def show_definition(name):
    characters[name]().show_definition()
