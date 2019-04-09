import Characters


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

class Ax:

    def __init__(self, character):
        self.name = LB.Tool_names['Ax']
        self.commands = LB.Tool_commands['Ax']
        self.definition = LB.Tool_definitions['Ax']
        self.force = int ((20 * character.stamina) / 100)


class Tube:

    def __init__(self, character):
        self.name = LB.Tool_names['Tube']
        self.commands = LB.Tool_commands['Tube']
        self.definition = LB.Tool_definitions['Tube']
        self.force = int ((15 * character.fairless) / 100)


class Knife:

    def __init__(self, character):
        self.name = LB.Tool_names['Knife']
        self.commands = LB.Tool_commands['Knife']
        self.definition = LB.Tool_definitions['Knife']
        self.force = int ((10 * character.speed) / 100)

Tool_Base = {"Knife": Knife, "Ax": Ax, "Tube": Tube}