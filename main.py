class Game:
    def __init__(self):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.finished = False
        self.turn = 1
        self.play()


    def is_finished(self):
        for i in self.board:
            if sum(i) == 3:
                return [True, 1]
            elif sum(i) == -3:
                return [True, -1]
        
        for i in range(len(self.board)):
            if sum([self.board[0][i], self.board[1][i], self.board[2][i]]) == 3:
                return [True, 1]
            elif sum([self.board[0][i], self.board[1][i], self.board[2][i]]) == -3:
                return [True, -1]

        if sum([self.board[0][0], self.board[1][1], self.board[2][2]]) == 3:
            return [True, 1]
        elif sum([self.board[0][0], self.board[1][1], self.board[2][2]]) == -3:
            return [True, -1]
        elif sum([self.board[2][0], self.board[1][1], self.board[0][2]]) == 3:
            return [True, 1]
        elif sum([self.board[2][0], self.board[1][1], self.board[0][2]]) == -3:
            return [True, -1]

        if 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2]:
            return [True, 0]

        return [False, 0]


    def print_board(self):
        for i in self.board:
            print(['-' if j == 0 else ('X' if j == 1  else 'O') for j in i])

        print()
        print('-----------------')
        print()


    def take_turn(self, pos):
        if self.board[pos[1]][pos[0]] == 0:
           self.board[pos[1]][pos[0]] = self.turn
           self.turn = self.turn * -1 


    def play(self):
        while self.finished != True:
            if self.turn == 1:
                print()
                print('Enter the coordinate in x, y form')
                print()
                pos = [int(i) for i in input().split(',')]

                self.take_turn(pos)
            else:
                result = self.minimize()

                self.board[result[1]][result[2]] = -1
                self.turn = self.turn * -1

            if self.is_finished()[0]:
                self.finished = True

            self.print_board()

    
    def maximize(self):
        max_value = -2
        max_x = None
        max_y = None

        done = self.is_finished()

        if done[0]:
            if done[1] == 1:
                return [1, 0, 0]
            elif done[1] == -1:
                return [-1, 0, 0]
            elif done[1] == 0:
                return [0, 0, 0]

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.board[i][j] = 1

                    state = self.minimize()

                    if state[0] > max_value:
                        max_value = state[0]
                        max_x = i
                        max_y = j

                    self.board[i][j] = 0

        return [max_value, max_x, max_y]


    def minimize(self):
        min_value = 2
        min_x = None
        min_y = None

        done = self.is_finished()

        if done[0]:
            if done[1] == 1:
                return [1, 0, 0]
            elif done[1] == -1:
                return [-1, 0, 0]
            elif done[1] == 0:
                return [0, 0, 0]

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    self.board[i][j] = -1

                    state = self.maximize()

                    if state[0] < min_value:
                        min_value = state[0]
                        min_x = i
                        min_y = j

                    self.board[i][j] = 0

        return [min_value, min_x, min_y]


if __name__ == '__main__':
    g = Game()
