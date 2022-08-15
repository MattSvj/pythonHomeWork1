# Задача 1: Крестики нолики

def ShowBoard():
    for i in range(0, len(pole)):
        print(pole[i])
    print("Ходит игрок " + players[move] + '(' + signs[move] + ').')


def Finish():
    if pole[0][0] == pole[0][1] == pole[0][2] == 'x' or pole[0][0] == pole[1][1] == pole[2][2] == 'x' or pole[0][0] == \
            pole[1][0] == pole[2][0] == 'x' or pole[0][0] == pole[1][0] == pole[2][0] == 'x' or pole[0][2] == pole[1][
        2] == pole[2][2] == 'x' or pole[0][0] == pole[1][1] == pole[2][2] == 'x' or pole[0][2] == pole[1][1] == pole[2][
        0] == 'x' or pole[2][0] == pole[2][1] == pole[2][2] == 'x':
        return True
    elif pole[0][0] == pole[0][1] == pole[0][2] == '0' or pole[0][0] == pole[1][1] == pole[2][2] == '0' or pole[0][0] == \
            pole[1][0] == pole[2][0] == '0' or pole[0][0] == pole[1][0] == pole[2][0] == '0' or pole[0][2] == pole[1][
        2] == pole[2][2] == '0' or pole[0][0] == pole[1][1] == pole[2][2] == '0' or pole[0][2] == pole[1][1] == pole[2][
        0] == '0' or pole[2][0] == pole[2][1] == pole[2][2] == '0':
        return True
    return False


def check_move(x, y):
    if pole[x][y] == "":
        return True


user1 = input('Игрок №1 (ходит x), введите имя: ')
user2 = input('Игрок №2 (ходит 0), введите имя: ')
pole = [['', '', ''], ['', '', ''], ['', '', '']]
move = 0
players = [user1, user2]
signs = ['x', '0']
while not Finish():
    ShowBoard()
    a, b = map(int, input('Введите координаты: ').split())
    if check_move(a - 1, b - 1):
        pole[a - 1][b - 1] = signs[move]
        move = (move + 1) % 2
print('Победил ' + players[(move + 1) % 2] + '!')