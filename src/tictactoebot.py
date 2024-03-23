class Tictactoebot:
    
    def __init__(self, board, p):
        self.board = board
        self.p = p
    
    def remainingmoves(self):
        for i in range(9):
            if self.board[i] not in [0, 1]:
                return True
        return False
    
    def victory(self):
        Lis=[]
        for j in range(3):
            sum=0
            for i in range(3):
                sum+=self.board[j*3+i]
            Lis.append(sum)  #vertical
        for i in range(3):
            sum=0
            for j in range(3):
                sum+=self.board[j*3+i]
            Lis.append(sum) #horizontal
        sum1=0
        sum2=0
        for i in range(3):
            sum1+=self.board[i*3+i]
            sum2+=self.board[(2-i)*3+i]
        Lis.append(sum1) #diag1
        Lis.append(sum2) #diag2
        if 0 in Lis:
            return 10
        elif 3 in Lis:
            return -10
        return 0

    def minmaxbot(self, depth, ismax):
        vic = self.victory()
        if vic == 10:
            return vic
        if vic == -10:
            return vic
        if not self.remainingmoves(): 
            return 0
        if ismax:
            best = -1000
            for i in range(9):
                if self.board[i] not in [0, 1]: 
                    x = self.board[:]
                    self.board[i] = self.p
                    self.p = self.p % 2 + 1  # Switch player
                    best = max(best, self.minmaxbot(depth + 1, not ismax))
                    self.board = x[:]
            return best
        else:
            best = 1000
            for i in range(9):
                if self.board[i] not in [0, 1]:
                    x = self.board[:]
                    self.board[i] = self.p
                    self.p = self.p % 2 + 1  # Switch player
                    best = min(best, self.minmaxbot(depth + 1, not ismax))
                    self.board = x[:]
            return best
    
    def bestmove(self):
        bestval = -1000
        bestmove = -1
        for i in range(9):
            if self.board[i] not in [0, 1]:
                x = self.board[:]
                self.board[i] = self.p
                self.p = self.p % 2 + 1  # Switch player
                moveval = self.minmaxbot(0, False)
                self.board = x[:]
                if moveval > bestval:
                    bestmove = i 
                    bestval = moveval
        return bestmove

'''sumboard=[10 for x in range(9)]
p=1
board=[2 for x in range(3) for y in range(3)]
for i in range(9):
    n=int(input())
    sumboard[i]=p%2
    print(sumboard)
'''