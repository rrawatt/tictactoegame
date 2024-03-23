class Tictactoebot:
    def __init__(self):
        self.board = [0] * 9
        self.p = 1

    def remainingmoves(self):
        return any(cell == 0 for cell in self.board)

    def victory(self):
        for j in range(3):
            if sum(self.board[j*3:(j+1)*3]) in [0, 3]:
                return True
        for i in range(3):
            if sum(self.board[i::3]) in [0, 3]:
                return True
        if sum(self.board[::4]) in [0, 3] or sum(self.board[2:7:2]) in [0, 3]:
            return True
        return False

    def minmaxbot(self, depth, ismax):
        if self.victory():
            return 10 if self.p == 1 else -10
        if not self.remainingmoves():
            return 0

        if ismax:
            best = -1000
            for i in range(9):
                if self.board[i] == 0:
                    self.board[i] = self.p
                    self.p = self.p % 2 + 1
                    best = max(best, self.minmaxbot(depth + 1, not ismax))
                    self.board[i] = 0
                    self.p = self.p % 2 + 1
            return best
        else:
            best = 1000
            for i in range(9):
                if self.board[i] == 0:
                    self.board[i] = self.p
                    self.p = self.p % 2 + 1
                    best = min(best, self.minmaxbot(depth + 1, not ismax))
                    self.board[i] = 0
                    self.p = self.p % 2 + 1
            return best

    def bestmove(self):
        bestval = -1000
        bestmove = -1
        for i in range(9):
            if self.board[i] == 0:
                self.board[i] = self.p
                self.p = self.p % 2 + 1
                moveval = self.minmaxbot(0, False)
                self.board[i] = 0
                if moveval > bestval:
                    bestmove = i
                    bestval = moveval
        return bestmove

def draw_board(board):
    for i in range(3):
        print("|".join(str(cell) if cell != 0 else " " for cell in board[i*3:i*3+3]))
        if i < 2:
            print("-" * 5)

def main():
    ttt = Tictactoebot()
    while ttt.remainingmoves() and not ttt.victory():
        draw_board(ttt.board)
        print("\nIt's Player", ttt.p, "'s turn")
        if ttt.p == 1:
            move = int(input("Enter your move (0-8): "))
            if 0 <= move <= 8 and ttt.board[move] == 0:
                ttt.board[move] = 1
                ttt.p = 2
            else:
                print("Invalid move. Try again.")
        else:
            print("Bot is making a move...")
            move = ttt.bestmove()
            ttt.board[move] = 2
            ttt.p = 1

    draw_board(ttt.board)
    if ttt.victory():
        print("\nPlayer", ttt.p, "wins!")
    else:
        print("\nIt's a draw!")

if __name__ == "__main__":
    main()
