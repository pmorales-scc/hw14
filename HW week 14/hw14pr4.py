# CSCI1550
# homework 14 problem 4
# file: hw14pr4.py
# Name: Peter Morales

import random
import os

class TTT:
    def __init__(self,strData):
        self.data_string = ''
        N = len(strData)
        for k in range(9):
            if k >= N:
                break
            else:
                self.data_string = self.data_string + strData[k]
        self.board = TTT.boardFromDataString(self.data_string)
        
    def boardFromDataString(dataString):
        tttBoard = [ [' ',' ',' '], [' ', ' ',' '], [' ',' ',' ']]
        N = len(dataString)
        for k in range(N):
            r = k // 3
            c = k % 3
            tttBoard[r][c] = dataString[k]
        return tttBoard

    def __repr__(self):
       s = ''
       for k in range(30):
           r = k // 6
           c = k % 6
           if (r % 2 == 0) and (c % 2 == 1):
               if c < 5:
                   s = s + '|'
               else:
                    s = s + '\n'
           elif (r % 2 == 1) and (c % 2 == 1):
                if c < 5:
                    s = s + '+'
                else:
                    s = s + '\n'
           elif (r % 2 == 1) and (c % 2 == 0):
                s = s + '-'
           else:
                s = s + self.board[r//2][c//2]
       return s    

    def dataStringFromBoard(board):
        dsOut = ''
        for r in range(3):
            for c in range(3):
                dsOut = dsOut + board[r][c]
        return dsOut

    def addMove(self, row, col, ox):
        self.board[row][col] = ox
        self.data_string = TTT.dataStringFromBoard(self.board)

    def checkMove(self, row, col):
        if row not in range(3) or col not in range(3):
            return False
        elif self.board[row][col] != ' ':
            return False
        else:
            return True

    def deleteMove(self, row, col):
        self.addMove(row, col, ' ')
            
    def clearBoard(self):
        for row in range(3):
            for col in range(3):
                self.deleteMove(row,col)

    def winsFor(self, ox):
        for i in range(3):
            if inarow_Neast(ox,i,0,self.board,3):
                return True
            if inarow_Nsouth(ox,0,i,self.board,3):
                return True
        if inarow_Nsoutheast(ox,0,0,self.board,3):
            return True
        if inarow_Nnortheast(ox,2,0,self.board,3):
            return True
        return False


    def hostGame(self):
        filename = self.fileNamer5000()
        gameState = True
        print("Player 1, you are 'X's, you will go first!")
        print("Player 2, you are 'O's, you will go second.")
        print("You will enter your moves in row, column pairs.")
        print("Be sure to separate rows and column values by a comma!")
        print("Since this is a CS class, values for rows and columns start at ZERO!")
        print("Let the best primate win!")
        
        while gameState:
            print("Player 1, what is your move? ", end = '')
            tmp = input()
            x = tmp.split(',')
            m = []
            for rc in x:
                m.append(int(rc))
            while not self.checkMove(m[0],m[1]):
                print("Player 1, please supply a valid move! ", end = '')
                tmp = input()
                x = tmp.split(',')
                m = []
                for rc in x:
                    m.append(int(rc))
            self.addMove(m[0],m[1],'X')
            
            print(self)    
            if self.winsFor('X'):
                print("Congratulations player 1, you (the X's) won!")
                myF = open(filename, "a")
                myF.write(self.data_string + ",x" + "\n")
                myF.close()
                gameState = False
            elif not (" " in self.data_string):
                print("The game ends in a tie!")
                myF = open(filename, "a")
                myF.write(self.data_string + ",t" + "\n")
                myF.close()
                gameState = False
            else:
                print("Player 2, what is your move? ", end = '')
                tmp = input()
                x = tmp.split(',')
                m = []
                for rc in x:
                    m.append(int(rc))
                while not self.checkMove(m[0],m[1]):
                    print("Player 2, please supply a valid move! ", end = '')
                    tmp = input()
                    x = tmp.split(',')
                    m = []
                    for rc in x:
                        m.append(int(rc))
                self.addMove(m[0],m[1],'O')
                myF = open(filename, "a")
                myF.write(self.data_string + ",n" + "\n")
                myF.close()
                print(self)    
                if self.winsFor('O'):
                    print("Congratulations player 2, you (the O's) won!")
                    myF = open(filename, "a")
                    myF.write(self.data_string + ",o" + "\n")
                    myF.close()
                    gameState = False
        print("Do you want to play again? (Y)es or (N)o? ", end = '')
        tmp = input()
        if (tmp == "Y") or (tmp == "yes") or (tmp == "Yes"):
            print()
            print()
            self.clearBoard()
            self.hostGame()
        else:
            print("Good Bye!") 

    def hostGameYouVAi(self):
        filename = self.fileNamer5000()
        gameState = True
        print("You are 'X's, you will go first!")
        print("You will enter your moves in row, column pairs.")
        print("Be sure to separate rows and column values by a comma!")
        print("Since this is a CS class, values for rows and columns start at ZERO!")
        while gameState:
            print("Player 1, what is your move? ", end = '')
            tmp = input()
            x = tmp.split(',')
            m = []
            for rc in x:
                m.append(int(rc))  
            while not self.checkMove(m[0],m[1]):
                print("Player 1, please supply a valid move! ", end = '')
                tmp = input()
                x = tmp.split(',')
                m = []
                for rc in x:
                    m.append(int(rc))
            self.addMove(m[0],m[1],'X')
            print(self)    
            if self.winsFor('X'):
                print("Congratulations player 1, you (the X's) won!")
                myF = open(filename, "a")
                myF.write(self.data_string + ",x" + "\n")
                myF.close()
                gameState = False
            elif not (" " in self.data_string):
                print("The game ends in a tie!")
                myF = open(filename, "a")
                myF.write(self.data_string + ",t" + "\n")
                myF.close()
                gameState = False
            
            else:
                print("AI played its move\n")
                x = self.aiMove()
                m = []
                for rc in x:
                    m.append(rc)
                while not self.checkMove(m[0],m[1]):
                    x = self.aiMove()
                    m = []
                    for rc in x:
                        m.append(rc)
                self.addMove(m[0],m[1],'O')
                myF = open(filename, "a")
                myF.write(self.data_string + ",n" + "\n")
                myF.close()
                print(self)    
                if self.winsFor('O'):
                    print("The AI (the O's) won!")
                    myF = open(filename, "a")
                    myF.write(self.data_string + ",o" + "\n")
                    myF.close()
                    gameState = False
        print("Do you want to play again? (Y)es or (N)o? ", end = '')
        tmp = input()
        if (tmp == "Y") or (tmp == "yes") or (tmp == "Yes"):
            print()
            print()
            self.clearBoard()
            self.hostGameYouVAi()
        else:
            print("Good Bye!")

    def hostGameAiVAi(self):
        filename = self.fileNamer5000()
        gameState = True
        print("AI vs AI!")
        while gameState:
            x = self.aiMove()
            m = []
            for rc in x:
                m.append(rc)
            while not self.checkMove(m[0],m[1]):
                x = self.aiMove()
                m = []
                for rc in x:
                    m.append(rc)
            self.addMove(m[0],m[1],'X')
            print(self)      
            if self.winsFor('X'):
                print("The X's won!")
                myF = open(filename, "a")
                myF.write(self.data_string + ",x" + "\n")
                myF.close()
                gameState = False
            elif not (" " in self.data_string):
                print("The game ends in a tie!")
                myF = open(filename, "a")
                myF.write(self.data_string + ",t" + "\n")
                myF.close()
                gameState = False
            
            else:
                x = self.aiMove()
                m = []
                for rc in x:
                    m.append(rc)
                while not self.checkMove(m[0],m[1]):
                    x = self.aiMove()
                    m = []
                    for rc in x:
                        m.append(rc)
                self.addMove(m[0],m[1],'O')

                myF = open(filename, "a")
                myF.write(self.data_string + ",n" + "\n")
                myF.close()

                print(self)    
                if self.winsFor('O'):
                    myF = open(filename, "a")
                    myF.write(self.data_string + ",o" + "\n")
                    myF.close()
                    print("The O's won!")
                    gameState = False

        print()
        print()
        self.clearBoard()


    def hostGameAiVAiVERBOSE(self):
        filename = self.fileNamer5000()
        gameState = True
        print("AI vs AI!")
        while gameState:
            x = self.aiMove()
            m = []
            for rc in x:
                m.append(rc)
            while not self.checkMove(m[0],m[1]):
                x = self.aiMove()
                m = []
                for rc in x:
                    m.append(rc)
            self.addMove(m[0],m[1],'X')
            print(self)
            print("View next move? (y/n) ", end = '')
            yOrN= input()
            if yOrN == "y":
                None
            else:
                print("Game Over")
                break 
            if self.winsFor('X'):
                print("The X's won!")
                myF = open(filename, "a")
                myF.write(self.data_string + ",x" + "\n")
                myF.close()
                gameState = False
            elif not (" " in self.data_string):
                print("The game ends in a tie!")
                myF = open(filename, "a")
                myF.write(self.data_string + ",t" + "\n")
                myF.close()
                gameState = False
            
            else:
                x = self.aiMove()
                m = []
                for rc in x:
                    m.append(rc)
                while not self.checkMove(m[0],m[1]):
                    x = self.aiMove()
                    m = []
                    for rc in x:
                        m.append(rc)
                self.addMove(m[0],m[1],'O')
                myF = open(filename, "a")
                myF.write(self.data_string + ",n" + "\n")
                myF.close()
                print(self)
                print("View next move? (y/n) ", end = '')
                yOrN= input()
                if yOrN == "y":
                    None
                else:
                    print("Game Over")
                    break    
                if self.winsFor('O'):
                    print("The O's won!")
                    myF = open(filename, "a")
                    myF.write(self.data_string + ",o" + "\n")
                    myF.close()
                    gameState = False
       
        print()
        print()
        self.clearBoard()

    def movesAvailable(self):
        spaceAv = []
        for i in range(len(self.data_string)):
            if self.data_string[i] == ' ':
                spaceAv.append(i)
        return spaceAv

    """
    Note: Self is an instance of the class. So you call methods by having self "call" them.
    self.movesAvailable() is cleaner then TTT.movesAvailable(self)

    You only need to use the class to call a method IF the method is a static method.
    """
    def scoreAvailable(self):
        scores = []
        score3 = [0,2,6,8]
        score2 = [1,3,4,5,7]
        Lol = []
        scoreIndex = []
        j = 0
        moves = self.movesAvailable()
        for i in moves:
            if i in score3:
                scores.append(3)
            elif i in score2:
                scores.append(2)

        while scores != []:
            Lol = [scores[j], moves[j]]
            scoreIndex.append(Lol)
            scores = scores[1:]
            moves = moves[1:]
        return scoreIndex


    """
    Dr. Reynolds tip:
    for x in num:
        if x[0] == maxS:
        bestMovePos.append(x[1])
    """
    def bestMoves(self):
        maxS = 0
        bestMovePos = []
        num = self.scoreAvailable()
        scores = []
        for i in range(len(num)):
            scores.append(num[i][0])
        maxS = max(scores)
        while num != []:
            if maxS > num[0][0]:
                num = num[1:]
            elif maxS == num[0][0]:
                bestMovePos.append(num[0][1])
                num = num[1:]  
        return bestMovePos

    def aiMove(self):
        bMoves = self.bestMoves()
        loc = random.choice(bMoves)
        c = loc%3
        r = loc//3 
        return [r,c]

    def hostGame_v2(self):
        count = 0
        print("Please input how many players. 0 (AI v AI), 1 (You v AI) or 2 (You v Another You): ", end = '')
        gameChoice = input()
        if gameChoice == "0":
            print("If you want the AI to play fast, enter 1. If you want the Ai to play VERBOSE, enter 2: ", end = '')
            gameType = input()
            print("How many games should be played? ", end = '')
            numGames = input()
            numGames = int(numGames)
            if gameType == "1":
                while count != numGames:
                    self.hostGameAiVAi()
                    count+=1
            elif gameType == "2":
                while count != numGames:
                    self.hostGameAiVAiVERBOSE()
                    count+=1
            else:
                print("Didnt enter a valid selection.")
                self.hostGame_v2()
        elif gameChoice == "1":
            self.hostGameYouVAi()
        elif gameChoice == "2":
            self.hostGame()
    
    def fileNamer5000(self):
        ListOfFiles = os.listdir()
        if "dataFile00000.ttt" in ListOfFiles:
            ttt_files = []
            for i in range(len(ListOfFiles)):
                if "ttt" in ListOfFiles[i]:
                    ttt_files.append(ListOfFiles[i])

            maxS = max(ttt_files)
            num = maxS[8:13]
            if num == "00000":
                newNum = "00001"
            elif num != "99999":
                num2 = int(num)
                num2+=1
                num2 = list(str(num2))
                num = list(num)
                for i in range(len(num)):
                    if num[i] != "0":
                        num[i] = num2[0]
                        num2 = num2[1:]
                    newNum = ''.join(num)
            else:
                newNum = "00000"
            filename = maxS[0:8]+newNum+maxS[13:17]
        else:
            filename = "dataFile00000.ttt"
        return filename

    

def inarow_Neast(ox, rs, cs, board, N):
    NR = len(board)
    NC = len(board[0])

    if (rs < 0) or (rs >= NR):
        return False
    if (cs < 0) or (cs > NC - N):
        return False
    for i in range(N):
        if board[rs][cs + i] != ox:
            return False 
    return True

def inarow_Nsouth(ox, rs, cs, board, N):
    NR = len(board)
    NC = len(board[0])

    if (cs < 0) or (cs >= NC):
        return False
    if (rs < 0) or (rs > NR - N):
        return False
    for i in range(N):
        if board[rs + i][cs] != ox:
            return False 
    return True

def inarow_Nsoutheast(ox, rs, cs, board, N):
    NR = len(board)
    NC = len(board[0])

    if (rs < 0) or (rs > NR - N):
        return False
    if (cs < 0) or (cs > NC - N):
        return False
    for i in range(N):
        if board[rs + i][cs + i] != ox:
            return False 
    return True

def inarow_Nnortheast(ox, rs, cs, board, N):
    NR = len(board)
    NC = len(board[0])

    if (rs < N-1) or (rs >= NR):
        return False
    if (cs < 0) or (cs > NC - N):
        return False
    for i in range(N):
        if board[rs - i][cs + i] != ox:
            return False 
    return True


