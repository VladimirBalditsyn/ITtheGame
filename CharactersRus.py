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
        self.name = "Бен"
        self.definition = "Парень, у которого большая не только душа, но и одежда." \
                     "\nЕсли поделить часы, проведенные им за занятиями спортом, на те, что он провел за книгами \n" \
                     "- получится бесконечно малое число." \
                     "\nЗато крайне сообразителен и никогда не предаст друзей"
        self.stamina = 70
        self.speed = 50
        self.fairless = 80
        self.superSection = "ум"

    def show_definition(self):
        print(self.definition)
        time.sleep(1)
        print("Супреспособность - {}".format(self.superSection))

    def level_one_intro(self):
        print("Бен как обычно проводил время в библитеке.")
        time.sleep(1)
        print("Читал \"Историю Дерри\"")
        time.sleep(1)
        print("Вдруг из хранилища вылетел красный воздушный шар...")
        time.sleep(1)
        print("Он манил Бена за собой...")
        time.sleep(1)
        print("И Бен пошел за ним.")
        time.sleep(1.5)
        print("Шар вел его между лабиринтами стеллажей...")
        time.sleep(1)
        print("Бен еле успевал...")
        time.sleep(1)
        print("Неожиданно, шар исчез.")
        time.sleep(1)
        print("Бен огляделся. Он заблудился в лабиринте. Ему стало страшно.")
        time.sleep(1)
        print("Вдруг из-за одного шкафа выглянул... Клоун...")
        time.sleep(1)
        print("Пенннивайз.")
        time.sleep(1)
        print("И Бен понял, что пора сматываться")
        time.sleep(1)


class Beverly:

    def __init__(self):
        self.name = "Беверли"
        self.definition = "Девушка с огненными волосами, сводящая с ума Билла и Бена.\nВолевая, с сильным характером - " \
                     "вот уж точно кто не боится опасностей"
        self.stamina = 80
        self.speed = 70
        self.fairless = 100
        self.superSection = "воля"

    def show_definition(self):
        print(self.definition)
        time.sleep(1)
        print("Супреспособность - {}".format(self.superSection))

    def level_one_intro(self):
        print("Беверли зашла в ванную, чтобы умыться после тяжелого дня...")
        time.sleep(1)
        print("Она наклонилась над раковиной и вдруг...")
        time.sleep(1)
        print("Из неё послышались голоса...")
        time.sleep(1)
        print("Детские голоса...")
        time.sleep(1)
        print("\"Беверли, мы все здесь летаем... Идем к нам... Ты тоже будешь летать\"")
        time.sleep(1)
        print("\"ТЫ ТОЖЕ БУДЕШЬ ЛЕТАТЬ!")
        time.sleep(1)
        print("И из раковины мгновенно хлынул поток крови.")
        time.sleep(1)
        print("Она залила всё: ванная стала равномерно бордового цвета и наполинлась запахом сталию")
        time.sleep(1)
        print("Когда Беверли на секунду отошла от шока и обернулась...")
        time.sleep(1)
        print("Она увидела за шторкой душевой...")
        time.sleep(1)
        print("ПЕННИВАЙЗА")
        time.sleep(1)
        print("и поняла, что пора бежать!")

class Bill:

    def __init__(self):
        self.name = "Билл"
        self.definition = "Вот точно кто хочет свести счеты с чудовищем - так это Билл." \
                     "\nДа, он прекрасен во всем, но есть нюанс: его решимость и " \
                     "бесстрашие могут подкосить воспоминания о Джодже...\n" \
                     "Есть велосипед, поэтому Усейн Болт видит лишь его спину"
        self.stamina = 100
        self.speed = 100
        self.fairless = 100
        self.superSection = "скорость"

    def show_definition(self):
        print(self.definition)
        time.sleep(1)
        print("Супреспособность - {}".format(self.superSection))

    def level_one_intro(self):
        print("Билл поздно вечером возвращался на велосипеде домой.")
        time.sleep(1)
        print("Его велосипед, Сильвер, как его называл сам Билл, летел по дорогам Дерри.")
        time.sleep(1)
        print("Хоть Сильвер был слишком большой для парня, Билл прекрасно управлялся с ним.")
        time.sleep(1)
        print("Некоторые машины ездили медленнее...\n")
        time.sleep(1.5)
        print("Вдруг краем глаза Билл замечает, что над водой канала имени Дерри...")
        time.sleep(1)
        print("Летает множество разноцветных шаров.")
        time.sleep(1)
        print("Точнее, они стоят. Даже ветер не колышет их.")
        time.sleep(1)
        print("И из воды канала поялвяется мерзкий клоун, и противным голосом предлагает:")
        time.sleep(1)
        print("\"Билл, возьми шарик. Ты будешь летать. Джорджи летает, и вместе с ним БУДЕШЬ ЛЕТАТЬ!\"")
        time.sleep(1)
        print("Но Билл не потерял самообладание и понял,")
        time.sleep(1)
        print("Нужно бежать!")
        time.sleep(1)


bill = Bill()
beverly = Beverly()
ben = Ben()


def show_definition(name):

    if name == "Bill":
        bill.show_definition()
    if name == "Beverly":
        beverly.show_definition()
    if name == "Ben":
        ben.show_definition()
