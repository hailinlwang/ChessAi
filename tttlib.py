import random

def genBoard():
   return [0,0,0,0,0,0,0,0,0]

def printBoard(T):
   if len(T) != 9:
      return False
   for i in T:
      if (i != 0) and (i != 1) and (i != 2):
         return False

   msg=[]
   pos=0
   for i in T:
      if (i==1):
         msg += ["X"]
      elif (i==2):
         msg += ["O"]
      else:
         msg += list(str(pos))
      pos+=1
     
   s = " " + msg[0] + " | " + msg[1] + " | " + msg[2]
   print(s)
   print("---|---|---")
   s = " " + msg[3] + " | " + msg[4] + " | " + msg[5]
   print(s)
   print("---|---|---")
   s = " " + msg[6] + " | " + msg[7] + " | " + msg[8]
   print(s)
   return True


def analyzeBoard(t):
    if t[0] == t[1] == t[2] != 0:
        return t[0]
    if t[3] == t[4] == t[5] != 0:
        return t[3]
    if t[6] == t[7] == t[8] != 0:
        return t[6]
    if t[0] == t[3] == t[6] != 0:
        return t[0]
    if t[1] == t[4] == t[7] != 0:
        return t[1]
    if t[2] == t[5] == t[8] != 0:
        return t[2]
    if t[0] == t[4] == t[8] != 0:
        return t[0]
    if t[2] == t[4] == t[6] != 0:
        return t[2]

    n_opens=0
    for i in t:
       if i==0:
          n_opens+=1
    if n_opens == 0:
        return 3
    else:
        return 0


def genNonLoser(T, player):
    boardNonLoser = list(T)
    p1 = player
    p2 = -1
    pos = -1

    move = False

    if p1 == 1:
        p2 = 2
    elif p1 == 2:
        p2 = 1
    else:
        return -1

    for x in range(0,9):
        if boardNonLoser[x] == 0:
            boardNonLoser[x] = p2
            if (analyzeBoard(boardNonLoser)) == p2:
                boardNonLoser[x] = p1
                pos = x
                move = True
            else:
                boardNonLoser[x] = 0
                move = False
    return pos



def genWinningMove(T, player):
    boardWinner = list(T)
    p1 = player
    p2 = -1
    pos = -1

    if p1 == 1:
        p2 = 2
    elif p1 == 2:
        p2 = 1
    else:
        return -1

    for x in range(0,9):
        if boardWinner[x] == 0:
            boardWinner[x] = p1
            if analyzeBoard(boardWinner) == p1:
                pos = x
                break
            else:
                boardWinner[x] = 0
    return pos





def genRandomMove(T,player):
    boardRandom = list(T)
    p1 = player
    p2 = -1
    pos = -1

    n_opens = 9

    if p1 == 1:
        p2 = 2
    elif p1 == 2:
        p2 = 1
    else:
        return -1

    for x in range(0,9):
        if boardRandom[x]!= 0:
            n_opens -= 1

    if n_opens > 0:
        while True:
            pos=random.randint(0,8)
            if boardRandom[pos] == 0:
                boardRandom[pos] = p1
                break
    elif n_opens <=0:
        return -1

    return pos

# What is the qualitative diff between using the
# random move generator and the open move generator?

def genOpenMove(T,player):
    boardOpen = list(T)
    p1 = player
    p2 = -1
    pos = -1
    n_opens = 9

    if p1 == 1:
        p2 = 2
    elif p1 == 2:
        p2 = 1
    else:
        return -1

    for x in range(0, 9):
        if boardOpen[x] != 0:
            n_opens -= 1

    if n_opens > 0:
        for x in range(0,9 ):
            if boardOpen[x] == 0:
                boardOpen[x] = p1
                pos = x
                break

    elif n_opens <= 0:
        return -1

    return x


Y = [2, 2, 0, 0, 2, 2, 0, 0, 0]
z = 2 

# print(genOpenMove(Y,z))
# print(genRandomMove(Y,z))
# print(genWinningMove(Y,z))
# print(genNonLoser(Y, z))
