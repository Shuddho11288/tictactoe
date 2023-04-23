import random

class UserInput:

    def __init__(self, row, column):

        self. row = row

        self.column = column

    def get_row(self):

        return self.row
    
    def get_column(self):

        return self.column
    

class AIChoice:

    def __init__(self, board:list, userSymbol='X'):

        self.userSymbol = userSymbol

        self.isFinalAttackReady = False

        self.isDefendNeeded = False

        self.choices = []

        self.ultimatechoice = []

        self.board = board

        self.check_columnwise()

        self.check_rowwise()

        self.check_diagonals()

        rowi = -1

        for row in self.board:

            rowi += 1

            if '-' in row:

                self.choices.append([rowi,row.index('-')])

        print(self.ultimatechoice)
        

    def getChoices(self):

        if self.ultimatechoice:

            return self.ultimatechoice
        
        else:

            return self.choices

    def check_rowwise(self):

        rowi = -1

        for row in self.board:

            rowi += 1

            if row.count('-') == 1:

                print('row check')
            
                if row.count(self.userSymbol)  == 2:

                    self.isDefendNeeded == True

                    self.ultimatechoice = [[rowi, row.index('-')]]

                elif row.count(self.userSymbol) == 1:

                    pass

                else:

                    self.isFinalAttackReady == True

                    self.ultimatechoice = [[rowi, row.index('-')]]

            

    def check_columnwise(self):

        for coli in [0,1,2]:
                
            choices = [self.board[0][coli], self.board[1][coli], self.board[2][coli]]

            if choices.count('-') == 1:

                print('col check')

                print(coli)

                print(choices)
            
                if choices.count(self.userSymbol)  == 2:

                    self.isDefendNeeded == True

                    self.ultimatechoice = [[choices.index('-'), coli]]

                elif choices.count(self.userSymbol) == 1:

                    pass

                else:

                    self.isFinalAttackReady == True

                    self.ultimatechoice = [[choices.index('-'), coli]]


    def check_diagonals(self):

        allChoices = [

            [self.board[0][0], self.board[1][1], self.board[2][2]],

            [self.board[0][2], self.board[1][1], self.board[2][0]]

        ]

        choices = allChoices[0]

        if choices.count('-') == 1:

            print('diag check')
        
            if choices.count(self.userSymbol)  == 2:

                print('diag check')

                self.isDefendNeeded == True

                self.ultimatechoice = [[choices.index('-'), choices.index('-')]]

            elif choices.count(self.userSymbol) == 1:

                pass

            else:

                print('diag check')

                self.isFinalAttackReady == True

                self.ultimatechoice = [[choices.index('-'), choices.index('-')]]



        choices = allChoices[1]

        if choices.count('-') == 1:

            print('diag check')
        
            if choices.count(self.userSymbol)  == 2:

                self.isDefendNeeded == True

                self.ultimatechoice = [[choices.index('-'), 2-choices.index('-')]]

            elif choices.count(self.userSymbol) == 1:

                pass

            else:

                self.isFinalAttackReady == True

                self.ultimatechoice = [[choices.index('-'), 2-choices.index('-')]]

    def getEnd(self):

        return len(self.getChoices())-1

class AIInput:

    def __init__(self, aiChoice:AIChoice):

        choice = aiChoice.getChoices()[random.randint(0,aiChoice.getEnd())]

        self.row = choice[0]
        
        self.column = choice[1]

    def get_row(self):

        return self.row
    
    def get_column(self):

        return self.column


class Board:

    def __init__(self, tosswin= True):

        self.createBoard()

        self.USER_SYMBOL = 'X' if tosswin is True else 'O'

        self.AI_SYMBOL = 'X' if tosswin is False else 'O'

    def createBoard(self):

        self.board = [
                        ['-', '-', '-'],
                        ['-', '-', '-'],
                        ['-', '-', '-']
                    ]
        
    def setUserInput(self, userInput: UserInput):

        self.board[userInput.get_row()][userInput.get_column()] = self.USER_SYMBOL


    def setAIInput(self):

        print(self.board)

        aiInput  = AIInput(AIChoice(self.board, self.USER_SYMBOL))

        self.board[aiInput.get_row()][aiInput.get_column()] = self.AI_SYMBOL

    def checkWin(self):

        board = self.board

        for row in board:

            if row.count(self.USER_SYMBOL) == 3:

                return 1
            
            elif row.count(self.AI_SYMBOL) == 3:

                return 2

        for col in range(3):

            if board[0][col] == board[1][col] == board[2][col]:

                if board[0][col] == self.USER_SYMBOL:

                    return 1
                
                elif board[0][col] == self.AI_SYMBOL:

                    return 2
  
        if board[0][0] == board[1][1] == board[2][2]:

            if board[0][0] == self.USER_SYMBOL:

                return 1
            
            elif board[0][0] == self.AI_SYMBOL:

                return 2
            
        elif board[0][2] == board[1][1] == board[2][0]:

            if board[0][2] == self.USER_SYMBOL:

                return 1
            
            elif board[0][2] == self.AI_SYMBOL:

                return 2
    
        return None

    def show(self):

        for x in self.board:

            print(' '.join(x))



if __name__ == '__main__':

    b = Board()

    while True:

        b.show()

        w = b.checkWin()

        if w == 1:

            print('USER WINS')

            break

        elif w == 2:

            print('AI WINS')

            break

        i = input('Enter your input:').split(' ')

        b.setUserInput(UserInput(int(i[0]), int(i[1])))    

        b.setAIInput()

    
