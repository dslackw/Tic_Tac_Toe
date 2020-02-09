#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random


class TicTacToe:

    def __init__(self, x=[1, 2, 3], y=['A', 'B', 'C']):
        self.x = x
        self.y = y
        self.tags = ['X', 'O']
        self.player = 1
        self.human = []
        self.pc = []
        self.board = []
        self.green = '\x1b[32m'
        self.red = '\x1b[31m'
        self.yellow = '\x1b[33m'
        self.endc = '\x1b[0m'
        self.color = ''
        self.wining_board()
        self.build_board()
        self.init()
        self.refresh()

    def init(self):
        '''Initilazation the Headers'''
        print('+---------------------+')
        print(f'| {self.green}*** Tic Tac Toe ***{self.endc} |')
        print('+---------------------+')
        print(f' Write {self.yellow}\help{self.endc} for Help!')
        print(f' Press {self.red}\quit{self.endc} for Quit\n')

    def build_board(self):
        '''Building board method'''
        for x in self.x:
            for y in self.y:
                self.board.append(f'{y}{x}')

    def wining_board(self):
        '''All winning possibilities'''
        self.win_board = (
            ['A1', 'B1', 'C1'],
            ['A2', 'B2', 'C2'],
            ['A3', 'B3', 'C3'],
            ['A1', 'A2', 'A3'],
            ['B1', 'B2', 'B3'],
            ['C1', 'C2', 'C3'],
            ['A1', 'B2', 'C3'],
            ['C1', 'B2', 'A3']
        )

    def refresh(self):
        '''Refreshing board method'''
        mark, n = ' ', 0
        print(' ' * 4, f'{" " * 5}'.join(self.y))
        for i, pos in enumerate(self.board):
            if i in (0, 3, 6):
                print(' ', self.x[n], end='')
                n += 1
            if pos in self.tags:
                mark = pos
            if mark == self.tags[0]:
                self.color = self.green
            else:
                self.color = self.red
            print(f' [{self.color}{mark}{self.endc}] ', end=' ')
            mark = ' '
            if i in (2, 5, 8):
                print('\n')

    def is_winner(self):
        '''Winner checking method algorithm'''
        # check if human won
        for win in self.win_board:
            n = 0
            for hum in self.human:
                for w in win:
                    if hum == w:
                        n += 1
                        if n == 3:
                            print(f'{self.yellow}  Human Won!{self.endc}')
                            raise SystemExit()
        # check if pc won
        for win in self.win_board:
            n = 0
            for com in self.pc:
                for w in win:
                    if com == w:
                        n += 1
                        if n == 3:
                            print(f'{self.yellow}  Computer Won!{self.endc}')
                            raise SystemExit()

    def computer(self):
        '''Computer method playing'''
        left = []
        time.sleep(1)
        for pos in self.board:
            if pos not in self.tags:
                left.append(pos)
                # set the B2 position if is available
                if 'B2' in left:
                    return 'B2'
        # compare the lists and get the
        # possibilities to win
        com = ''
        for win in self.win_board:
            com = set(win) - set(self.pc)
            if len(com) == 1 and ''.join(com) in left:
                return ''.join(com)
        # compare the lists and get the
        # possibilities to defend
        ply = ''
        for win in self.win_board:
            ply = set(win) - set(self.human)
            if len(ply) == 1 and ''.join(ply) in left:
                return ''.join(ply)

        return ''.join(random.sample(left, 1))

    def play(self):
        '''Control playing method'''
        while True:
            tag, hum, com = '', '', ''
            if (self.player % 2) == 1:
                raw = str(input('  Human playing: '))
                raw = raw.upper()
                raw = self.keybinds(raw)
                hum = raw
                tag = self.tags[0]
                print()
            else:
                print('  Computer playing ...\n')
                raw = self.computer()
                com = raw
                raw = raw.upper()
                tag = self.tags[1]

            if raw == '\QUIT':
                print(f"{self.green}  Bye, Please don't forget me :({self.endc}\n")
                break

            if raw in self.board:
                i = self.board.index(raw)
                self.board[i] = tag
                if hum:
                    self.human.append(hum)
                if com:
                    self.pc.append(com)

            elif raw == '\HELP':
                self.help()
                self.player -= 1
            else:
                print(f'{self.red}*** Play again ***{self.endc}\n')
                self.player -= 1

            self.refresh()
            self.is_winner()
            self.player += 1

            if self.player == 10:
                print(f'{self.yellow}  Draw!{self.endc}')
                break

    def keybinds(self, key):
        '''Keyboard keys filter'''
        k = key.lower()
        keys = {
            'q': 'A1',
            'w': 'B1',
            'e': 'C1',
            'a': 'A2',
            's': 'B2',
            'd': 'C2',
            'z': 'A3',
            'x': 'B3',
            'c': 'C3'
        }
        if k in keys.keys():
            return keys[k]
        else:
            return key

    def help(self):
        print(f"{self.yellow}     RULES FOR TIC-TAC-TOE\n"
              "     ---------------------\n"
              "  1. The game is played on a grid that's 3 squares by 3 squares.\n"
              "  2. You are X, and the computer in this case is O. \n"
              "     Players take turns putting their marks in empty squares.\n"
              "     You mark na empty square just write a char from A, B, C and\n"
              "     a number from 1, 2 or 3, like 'B2 or use the keys:\n"
              "     q, w, e, a, s, d, z, x and c.\n"
              "  3. The first player to get 3 of her marks in a row (up, down,\n"
              "     across, or diagonally) is the winner.\n"
              "  4. When all 9 squares are full, the game is over. If no player \n"
              f"     has 3 marks in a row, the game ends in a tie.{self.endc}\n")


if __name__ == '__main__':
    t = TicTacToe()
    t.play()