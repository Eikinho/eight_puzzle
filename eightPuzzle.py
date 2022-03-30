from SearchAlgorithims import AEstrela
from Graph import State
from random import randrange
import numpy as np
import time

class EightPuzzle(State):

    def __init__(self, board, size, op):
        self.board = board
        self.size = size
        self.operator = op
        
        # Acessar goal seguindo formatacao: goal[row][column]
        self.goal = np.array([[1, 2, 3],
                              [8, 0, 4],
                              [7, 6, 5]])

        self.dict_goal = {
            0: (1,1),
            1: (0,0),
            2: (0,1),
            3: (0,2),
            4: (1,2),
            5: (2,2),
            6: (2,1),
            7: (2,0),
            8: (1,0)
        }

    def get_empty(self):
        for row in range(0, self.size):
            for column in range(0, self.size):
                if self.board[row][column] == 0:
                    return (row, column)

    def env(self):
        return str(self.board)

    def sucessors(self):
        sucessores = []
        i, j = self.get_empty()
    
        if i > 0:
            tmp = self.board.copy()
            tmp_value = tmp[i-1][j]
            tmp[i-1][j] = tmp[i][j]
            tmp[i][j] = tmp_value
            sucessores.append(EightPuzzle(tmp, tmp.shape[0], "up"))
            
        if i < self.board.shape[0] - 1:
            tmp = self.board.copy()
            tmp_value = tmp[i+1][j]
            tmp[i+1][j] = tmp[i][j]
            tmp[i][j] = tmp_value
            sucessores.append(EightPuzzle(tmp, tmp.shape[0], "down"))
            
        if j > 0:
            tmp = self.board.copy()
            tmp_value = tmp[i][j-1]
            tmp[i][j-1] = tmp[i][j]
            tmp[i][j] = tmp_value
            sucessores.append(EightPuzzle(tmp, tmp.shape[0], "left"))
            
        if j < self.board.shape[0] - 1:
            tmp = self.board.copy()
            tmp_value = tmp[i][j+1]
            tmp[i][j+1] = tmp[i][j]
            tmp[i][j] = tmp_value
            sucessores.append(EightPuzzle(tmp, tmp.shape[0], "right"))

        return sucessores

    def is_goal(self):
        return str(self.board) == str(self.goal)
    
    def description(self):
        return "8-Puzzle Problem"
    
    def cost(self):
        return 1

    def h(self):
        d = 0

        for i in range(0, self.size):

            for j in range(0, self.size):

                i_goal, j_goal = self.dict_goal[self.board[i][j]]

                d += abs(i-i_goal) + abs(j-j_goal)

        return d

    def print(self):
        pass

    def isNotSolvable(self):
        l = list(self.board.flatten())
        for i in range(len(l)):
            l[i] = int(l[i])
        self.puzzle = l
        count=0
        for i in range(8):
            for j in range(i,9):
                if (self.puzzle[i] > self.puzzle[j] and              
                    self.puzzle[j]!=0):
                    count+=1
        if count%2==0:
            return True
        else:
            return False

def main():
    print('8-Puzzle Solver')
    board = np.array([[3,4,8],[1,2,5],[7,0,6]])
    state = EightPuzzle(board, board.shape[0], " ")
    if (state.isNotSolvable()):
        print("Not Solvable")
    else:
        print("Solvable")
        algorithm = AEstrela()
        print("Initial state with h = "+str(state.h()))
        start = time.time()
        result = algorithm.search(state)
        end = time.time()
        if result != None:
            print(result.show_path())
            print('Final state with h = '+str(result.h()))
            print('Duration in seconds = '+str(end-start))
        else:
            print('Nao achou solucao')

if __name__ == '__main__':
    main()