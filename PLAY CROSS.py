import time


def make_field(field: list):
    """Создаёт поле и выводит его в консоль"""
    print("-------------")
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-------------")


def check_input(position: str):
    """Проверяет ввод на корректность"""
    if position.isdigit():
        position = int(position)
        if 1 <= position <= 9:
            return True
        return False


def user_input(char: str, field: list, tries: int):
    """Принимает данные и проверяет позицию"""
    k = 0
    while tries > 0:
        position = input("Куда поставим " + char + "? ")
        if check_input(position):
            position = int(position)
            if str(field[position - 1]) not in "XO":
                field[position - 1] = char
                break
            else:
                print("Эта позиция уже занята.\n")
        else:
            print("\nНекорректный ввод!!! Что бы походить нужно ввести ЧИСЛО от 1 до 9.")
        tries -= 1
        k += 1
        if tries != 0:
            print(f"У вас осталось {tries} попыток."
                  f"\nПо истечению попыток вы будете заблокированы за попытку поломать игру!!!\n")
        else:
            print(f"У вас осталось {tries} попыток.")
    return k


def check_win(field: list):
    """Проверяет выигрыш"""
    win_combinations = ((0, 1, 2), (0, 3, 6), (3, 4, 5), (1, 4, 7), (2, 4, 6), (6, 7, 8), (0, 4, 8), (2, 5, 8))
    for x in win_combinations:
        if field[x[0]] == field[x[1]] == field[x[2]]:
            if field[x[0]] == 'X':
                return "\nВыиграл первый игрок!!!"
            else:
                return "\nВыиграл второй игрок!!!"
    return False


def secundomer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время: {round(end - start, 1)} сек длилась партия.')

    return wrapper


@secundomer
def main():
    """Головная функция, объединяет все функции; описывает весь процесс игры"""
    print("*" * 1, "Игра Крестики-нолики(размер поля 3х3,стандартное)", "*" * 1)
    field = list(range(1, 10))
    tries, move = 10, 0
    while True:
        make_field(field)
        char = 'X' if move % 2 == 0 else 'O'
        s = user_input(char, field, tries)
        tries -= s
        move += 1
        if tries == 0:
            print("Вы были заблокированы.")
            break
        elif move == 9:
            res = check_win(field)
            if not res:
                print("\nНичья!")
            elif isinstance(res, str):
                print(res)
            break
        elif 4 < move:
            res = check_win(field)
            if isinstance(res, str):
                print(res)
                break
    make_field(field)


if __name__ == '__main__':
    main()
