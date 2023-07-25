# Игра написана для консоли PyCharm. Для корректной работы необходимо настроить:
# "Run" -> "Edit configurations" -> "Emulate terminal in output console" - включить.

from random import choice
from os import system


class Player:
    def __init__(self, name, mark):  # 'mark' - тип отметки игрока(например: 'x','0','*' и т.д.)
        self.name = name
        self.mark = mark


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.field = [['  ', 1, 2, 3]] + [[i + 1] + ['_'] * 3 for i in range(3)]
        self.winner = None
        self.moves_counter = 0
        self.starter = choice((self.player1, self.player2))
        self.vse_polya = [(i, j) for i in range(1, 4) for j in range(1, 4)]

    def make_move(self):
        self.show_field()
        while (c := tuple(map(int, input(f'''{self.starter.name}, введи "x" и "y" координаты клетки
через пробел, чтобы поставить  "{self.starter.mark}"  ''').split()))) not in self.vse_polya:
            print('\nОшибка! Нет свободной клетки с такими координатами.', end='\n\n')
            continue
        self.field[c[1]][c[0]] = self.starter.mark
        self.vse_polya.remove(c)
        self.moves_counter += 1
        system('clear')

    def show_field(self):
        print('y\\x', end='')
        helpx = 0  # вспомогательный счетчик для красоты игрового поля
        for i in range(len(self.field)):
            if helpx > 0:
                print('    ', end='')
            helpx += 1
            for j in range(len(self.field[i])):
                print(self.field[i][j], end=' ')
            print()
        print()

    def check_winner(self):
        f = self.field
        victory_types = [f[1][1] == f[2][2] == f[3][3] != '_', f[3][1] == f[2][2] == f[1][3] != '_',
                         f[1][1] == f[1][2] == f[1][3] != '_', f[2][1] == f[2][2] == f[2][3] != '_',
                         f[3][1] == f[3][2] == f[3][3] != '_', f[1][1] == f[2][1] == f[3][1] != '_',
                         f[1][2] == f[2][2] == f[3][2] != '_', f[1][3] == f[2][3] == f[3][3] != '_', ]
        if True in victory_types:
            self.winner = self.starter

    def play(self):
        system('clear')
        print(f'В этой игре первый ход сделает {self.starter.name}!', end='\n\n')
        while self.moves_counter < 9:
            self.make_move()
            if self.moves_counter > 4:
                self.check_winner()
            if self.winner is not None:
                self.show_field()
                print(f'{self.winner.name} побеждает в этом раунде!')
                break
            self.starter = self.player1 if self.starter == self.player2 else self.player2
        else:
            self.show_field()
            print('Видимо, ничья :)')


# заготовки для тестов
'''g1 = Player('Петя', '#')
g2 = Player('Вова', '*')
game1 = Game(g1, g2)
game1.play()

g3 = Player('Лена', 'X')
g4 = Player('Аня', '0')
game2 = Game(g3, g4)
game2.play()

g5 = Player('Супермен', 'S')
g6 = Player('Бэтмэн', 'Б')
game3 = Game(g5, g6)
game3.play()'''
