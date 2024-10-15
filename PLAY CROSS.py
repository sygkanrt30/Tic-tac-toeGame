import time


def make_field(field):
    """Создаёт поле и выводит его в консоль"""
    print("*************")
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("*************")


def start_game(char, field):
    """Принимает данные, которые ввёл игроки"""
    while True:
        position = int(input("Куда поставим " + char + "? "))
        if 1 <= position <= 9:
            if str(field[position - 1]) not in "XO":
                field[position - 1] = char
                break
            else:
                print("Эта позиция уже занята.")
        else:
            print("Некорректный ввод!!! Что бы походить нужно ввести число от 1 до 9.")


def check_win(field):
    """Проверяет выигрыш"""
    win_combinations = ((0, 1, 2), (0, 3, 6), (3, 4, 5), (1, 4, 7), (2, 4, 6), (6, 7, 8), (0, 4, 8), (2, 5, 8))
    for x in win_combinations:
        if field[x[0]] == field[x[1]] == field[x[2]]:
            return field[x[0]]
    return False


def secundomer(f):
    def wrapper():
        start = time.time()
        f()
        end = time.time()
        print(f'Время: {round(end - start, 1)} сек длилась партия')

    return wrapper


@secundomer
def main():
    """Процесс игры"""
    print("*" * 1, "Игра Крестики-нолики(размер поля 3х3,стандартное)", "*" * 1)
    field = list(range(1, 10))
    cnt = 0
    while True:
        make_field(field)
        if cnt % 2 == 0:
            start_game("X", field)
        else:
            start_game("O", field)
        cnt += 1
        if cnt == 9:
            print("Ничья!")
            break
        elif 4 < cnt < 9:
            char = check_win(field)
            if char == 'X':
                print("Выиграл первый игрок!!!")
                break
            elif char == 'O':
                print("Выиграл второй игрок!!!")
                break
    make_field(field)


if __name__ == '__main__':
    main()
