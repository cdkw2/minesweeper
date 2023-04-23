import random

class Minesweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = []
        self.revealed = []
        self.mines = []
        self.flags = []
        self.game_over = False

        # Create the board
        for i in range(self.width):
            self.board.append([' '] * self.height)
            self.revealed.append([False] * self.height)

        # Place the mines randomly on the board
        num_placed_mines = 0
        while num_placed_mines < self.num_mines:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            if self.board[x][y] != '*':
                self.board[x][y] = '*'
                self.mines.append((x, y))
                num_placed_mines += 1

    def print_board(self):
        # Print the header row
        header = '   '
        for i in range(self.width):
            header += str(i) + ' '
        print(header)

        # Print the board
        for i in range(self.height):
            row = str(i) + ' |'
            for j in range(self.width):
                if (j, i) in self.flags:
                    row += '⚐|'
                elif not self.revealed[j][i]:
                    row += ' |'
                else:
                    row += self.board[j][i] + '|'
            print(row)

    def reveal(self, x, y):
        if self.revealed[x][y] or (x, y) in self.flags:
            return

        self.revealed[x][y] = True

        if self.board[x][y] == '*':
            self.game_over = True
            return

        num_adjacent_mines = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                    continue
                if self.board[nx][ny] == '*':
                    num_adjacent_mines += 1

        if num_adjacent_mines > 0:
            self.board[x][y] = str(num_adjacent_mines)
        else:
            self.board[x][y] = ' '
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx = x + dx
                    ny = y + dy
                    if nx < 0 or nx >= self.width or ny < 0 or ny >= self.height:
                        continue
                    self.reveal(nx, ny)

    def flag(self, x, y):
        if self.revealed[x][y]:
            return

        if (x, y) in self.flags:
            self.flags.remove((x, y))
        else:
            self.flags.append((x, y))

    def play(self):
        while not self.game_over:
            self.print_board()
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            action = input("Enter 'r' to reveal, 'f' to flag/unflag: ")

            if action == 'r':
                self.reveal(x, y)
            elif action == 'f':
                self.flag(x, y)

        self.print_board()
        if len(self.mines) == 0:
            print("Congratulations, you win!")
        else:
            print("Game over, you lose!")

if __name__ == '__main__':
    width = 10
    height = 10
    num_mines = 10
    game = Minesweeper(width, height, num_mines)
    game.play()
