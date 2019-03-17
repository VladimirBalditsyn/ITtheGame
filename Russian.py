import time
import CharactersRus
import random
from threading import Timer
from platform import system as system_name # Returns the system/OS name
from os import system as system_call       # Execute a shell command


def clear_screen():
    """
    Clears the terminal screen.
    """

    # Clear command as function of OS
    command = "cls" if system_name().lower()=="windows" else "clear"

    # Action
    system_call(command)


class GameStart:

    def __init__(self):
        self.commands = ["Беги", "Поверни налево", "Поверни направо", "Пригнись", "Подпрыгни"]
        self.answers = ["беги", "налево", "направо", "вниз", "вверх"]
        self.character = CharactersRus.Null()

    def hello(self):
        print("\nКруто, давай начнем!\n")
        time.sleep(1)

    def prologue(self):
        print("Добро пожаловать в Дерри!\n\n")
        time.sleep(2)
        print("Милый городок, гимн которого мог бы начинаться со слов:")
        time.sleep(1.5)
        print("\"Здесь живут простые люди, здесь живут мои друзья...\"")
        time.sleep(1.5)
        print("Если бы в городе не поселилось...\n")
        time.sleep(2)
        print("ОНО.\n")
        time.sleep(2)
        print("Каждые 28 лет оно выходит из ада и поселяется в канализации этого города...")
        time.sleep(1.5)
        print("И сегодня ОНО снова проснулось  и похитило малыша Джорджи.\n")
        time.sleep(1.5)
        print("Но брат Джорджи - Билл - не готов мириться с этим.")
        time.sleep(1.5)
        print("Он хочет остановить чудовище.")
        time.sleep(1.5)
        print("Только он, Заика Билл, красавица Беверли,толстячок Бен и их друзья способны остановить Пеннивайза...")
        time.sleep(1.5)
        print("Но смогут ли они?\n")
        time.sleep(3)

    def choose_character(self):
        print("\nСейчас настало самое время выбрать пресонажа.\nКем ты хочешь быть, отчаянный герой? Майком, Беном или,"\
              "быть может, Беверли?)")
        time.sleep(1)
        print("\n\nВведи \"узнать о \" и имя пресонажа(например, узнать о Билле), чтобы получить информацию о нем\n"\
              "или \"я \" и имя персонажа(например, я Билл), чтобы оказаться в его шкуре\n")
        s = input()
        while True:
            if s.lower() == 'узнать о билле':
                print('\n')
                CharactersRus.show_definition('Bill')
                s = input("\nЧто ещё угодно?\n")
            elif s.lower() == 'узнать о беверли':
                print('\n')
                CharactersRus.show_definition('Beverly')
                s = input("\nЧто ещё угодно?\n")
            elif s.lower() == 'узнать о бене':
                print('\n')
                CharactersRus.show_definition('Ben')
                s = input("\nЧто ещё угодно?\n")
            elif s.lower() == 'я билл':
                print('\n')
                print("Пеннивайз будет молить о пощаде!\n")
                self.character =  CharactersRus.Bill()
                break
            elif s.lower() == 'я беверли':
                print('\n')
                print("Огонь-девушка!!!\n")
                self.character = CharactersRus.Beverly()
                break
            elif s.lower() == 'я бен':
                print('\n')
                print("Хороший выбор. Бен крут, хоть и нескладен\n")
                self.character = CharactersRus.Ben()
                break
            else:
                print("\nХмм... Ты хочешь того, что я не знаю.\nСоберись и попробуй еще\n")
                s = input()

    def time_end(self, flag):
        print('\nСлишком медленно! Нажми Enter, чтобы продолжить')
        self.character.stamina -= 5
        flag[0] = True

    def run(self, count, timeout):
        while self.character.stamina > 0 and count > 0:
            timeout = timeout * self.character.speed / 100
            flag = [False]
            t = Timer(timeout, self.time_end, [flag])
            t.start()
            i = random.randint(0, 4)
            prompt = "{}!\n".format(self.commands[i])
            answer = input(prompt)
            if flag[0]:
                t.cancel()
                pass
            elif answer.lower() != self.answers[i]:
                if i in [0, 3, 4]:
                    print('Ты споткнулся, -5ХР\n')
                    self.character.stamina -= 5
                elif i in [1, 2]:
                    print('Ты повернул не туда, -5ХР\n')
                    self.character.stamina -= 5
            else:
                count -= 1

            t.cancel()

    def level_one(self):
        time.sleep(1)
        print("Уровень 1. Погоня")

        time.sleep(1)
        self.character.level_one_intro()

        time.sleep(3)

        clear_screen()

        print("Правила просты:\n"
              "На экране будут появляться команды, в соответсвии с которыми нужно будет ввести слово\n"
              "чтобы скрыться от Пеннивайза. Вот они:")
        for i in range(5):
            print("{}       --->        {}".format(self.commands[i], self.answers[i]))
        time.sleep(1.5)
        print("\nБудь внимателен, друг мой.\n"
              "Любая ошибка приблизит к тебе Пеннивайза и отнимет 5ХР драгоценного здоровья\n"
              "Так же важно вводить команды быстро, иначе Пеннивайз сможет дотянуться до тебя\n"
              "И ты снова потеряешь 5ХР\n\n"
              "Время, отведенное на ответ, зависит от скорости твоего персонажа:")
        time.sleep(0.5)
        print("Твоя скорость: {}".format(self.character.speed))
        print("Твое здоровье: {}".format(self.character.stamina))
        time.sleep(1)
        print("Не забывай после ввода ответа нажимать ENTER\n")
        input("Если ты чувствуешь в себе силы начать, мой друг, нажми ENTER и удачи!\n")
        clear_screen()

        while True:
            self.run(10, 3)

            if self.character.stamina > 0:
                print("Да ты молодец! Пришло время ускориться!")
                print("Твоё здоровье: {}".format(self.character.stamina))
                time.sleep(2)
                clear_screen()
            else:
                print("Оооо нееет!!!\n"
                      "Пеннивайз вкусно пообедал. А ты попробуй ещё.")
                time.sleep(2)
                clear_screen()
                pass

            self.run(10, 2.5)

            if self.character.stamina > 0:
                print("Да ты молодец! Сейчас ты близок к выходу как никода!")
                print("Твоё здоровье: {}".format(self.character.stamina))
                time.sleep(2)
                clear_screen()
            else:
                print("Оооо нееет!!!\n"
                      "Жизнь бывает жестока, как Пенивайз сегодня. А ты попробуй ещё.")
                time.sleep(2)
                clear_screen()
                pass

            self.run(6, 2)

            if self.character.stamina > 0:
                print("Да ты спортсмен, оказывается!")
                print("Ты успешно скрыл{} от этого монстра!".format('ся' if self.character.name != "Беверли" else 'ась'))
                print("Посмотрим, что ждёт тебя дальше!")
                time.sleep(3)
                clear_screen()
                break

            else:
                print("Оооо нееет!!!\n"
                      "Победа была так близко... Давай ещё разок.")
                time.sleep(2)
                clear_screen()
                pass

    def level_two(self):
        print("Уровень 2. Путь к логову зверя")
