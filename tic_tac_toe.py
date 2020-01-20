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
        self.refresh()

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
        print(' ' * 2, f'{" " * 5}'.join(self.y))
        for i, pos in enumerate(self.board):
            if i in (0, 3, 6):
                print(self.x[n], end='')
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
                        n += 2
                        if n == 6:
                            print(f'{self.yellow}Human Won!{self.endc}')
                            raise SystemExit()
        # check if pc won
        for win in self.win_board:
            n = 0
            for com in self.pc:
                for w in win:
                    if com == w:
                        n += 2
                        if n == 6:
                            print(f'{self.yellow}Computer Won!{self.endc}')
                            raise SystemExit()

    def computer(self):
        '''Computer method playing'''
        left = []
        time.sleep(1)
        for pos in self.board:
            if pos not in self.tags:
                left.append(pos)
                if 'B2' in left:
                    return 'B2'
        found = ''
        for win in self.win_board:
            found = set(win) - set(self.human)
            if len(found) == 1 and ''.join(found) in left:
                return ''.join(found)
        return ''.join(random.sample(left, 1))

    def play(self):
        '''Control playing method'''
        while True:
            tag, hum, com = '', '', ''
            if (self.player % 2) == 1:
                raw = str(input('Human playing (Q/quit): '))
                raw = raw.upper()
                hum = raw
                tag = self.tags[0]
                print()
            else:
                print('Computer playing...\n')
                raw = self.computer()
                com = raw
                raw = raw.upper()
                tag = self.tags[1]

            if raw in ['Q', 'q']:
                break

            if raw in self.board:
                i = self.board.index(raw)
                self.board[i] = tag
                if hum:
                    self.human.append(hum)
                if com:
                    self.pc.append(com)
            else:
                print(f'{self.red}*** Play again ***{self.endc}\n')
                self.player -= 1

            self.refresh()
            self.is_winner()
            self.player += 1

            if self.player == 10:
                print(f'{self.yellow}Draw!{self.endc}')
                break


if __name__ == '__main__':
    t = TicTacToe()
    t.play()