
from tttlib import *



n_moves = 0

T = genBoard()
while True:
   printBoard(T)
   moveX = input("X move? ")

   # check moveX for valid input
   while not((0<=int(moveX)) and (int(moveX)<9) and (T[int(moveX)]==0)):
      moveX = input("Invalid. X move? ")
   print(n_moves)
   # if valid :and if T is unoccupied at moveX, set the appropriate
   # position of T via: T[int(moveX)] = 1
   T[int(moveX)]=1

   state = analyzeBoard(T)
   # check if state says X won and act accordingly and break
   # check if state says draw and act accordingly and break
   if(state == 1):
      printBoard(T)
      print("X wins")
      break
   elif(state == 3):
      printBoard(T)
      print("Draw")
      break
   n_moves+=1


   printBoard(T)
   # HUMAN INPUT CODE  moveO = input("O move? ")
   moveO = -1
   print("O Move ")
   # check moveO for valid input
   # if valid and if T is unoccupied at moveO, set the appropriate
   # while not((0<=int(moveO)) and (int(moveO)<9) and (T[int(moveO)]==0)):
   if n_moves< 2:
       moveO = genRandomMove(T,2)
   #elif n_moves < 4:
    #   moveO = genRandomMove(T,2)
   else:
      if genWinningMove(T,2)!=-1:
         moveO = genWinningMove(T,2)
      elif genNonLoser(T,2)!=-1:
         moveO = genNonLoser(T,2)
      else:
         moveO = genOpenMove(T,2)
   print(n_moves)      
   # Old HUMAN input Code:  moveO = input("Invalid. O move? ")

   # position of T via: T[int(moveO)] = 2
   T[moveO]=2

   state = analyzeBoard(T)
   # check if state says O won and act accordingly and break
   # check if state says draw and act accordingly and break
   if(state == 2):
      printBoard(T)
      print(state)
      break
   elif(state == 3):
      printBoard(T)
      print(state)
      break

   n_moves += 1

