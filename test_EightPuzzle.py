import time
from SearchAlgorithims import AEstrela
from eightPuzzle import EightPuzzle
import numpy as np

goal = np.array([[1,2,3],
                 [8,0,4],
                 [7,6,5]])

def testFacil():
  board = np.array([[8,1,3],[0,7,2],[6,5,4]])
  state = EightPuzzle(board, 3, "")
  algorithm = AEstrela()
  ts = time.time()
  result = algorithm.search(state)
  tf = time.time()
  print("")
  print("=======================================")
  print("Teste Facil 1")
  print(f"Tempo de resolucao: {tf - ts}")
  assert result.show_path() == " ; right ; right ; down ; left ; left ; up ; up ; right ; down"
  
def testdificil1():
  board = np.array([[7,8,6],[2,3,5],[1,4,0]]) 
  state = EightPuzzle(board, 3, "")
  algorithm = AEstrela()
  ts = time.time()
  result = algorithm.search(state)
  tf = time.time()
  print("")
  print("=======================================")
  print("Teste Dificil 1")
  print(f"Tempo de resolucao: {tf - ts}")
  assert result.show_path() == " ; up ; left ; left ; up ; right ; down ; down ; left ; up ; up ; right ; right ; down ; left ; down ; left ; up ; right ; up ; left ; down ; down ; right ; up"

def testdificil2():
  board = np.array([[7,8,6],[2,3,5],[0,1,4]]) 
  state = EightPuzzle(board, 3, "")
  algorithm = AEstrela()
  ts = time.time()
  result = algorithm.search(state)
  tf = time.time()
  print("")
  print("=======================================")
  print("Teste Dificil 2")
  print(f"Tempo de resolucao: {tf - ts}")
  assert result.show_path() == " ; up ; up ; right ; down ; left ; down ; right ; up ; right ; up ; left ; left ; down ; down ; right ; up ; up ; left ; down ; right ; right ; down ; left ; up"
  
def testdificil3():
  board = np.array([[8,3,6],[7,5,4],[2,1,0]])
  state = EightPuzzle(board, 3, "")
  algorithm = AEstrela()
  ts = time.time()
  result = algorithm.search(state)
  tf = time.time()
  print("")
  print("=======================================")
  print("Teste Dificil 3")
  print(f"Tempo de resolucao: {tf - ts}")
  assert result.show_path() == " ; up ; up ; left ; left ; down ; right ; down ; left ; up ; up ; right ; down ; down ; left ; up ; up ; right ; down ; right ; down ; left ; up"
