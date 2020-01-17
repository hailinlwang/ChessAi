from chessPlayer_tree import *
from chessPlayer_minimax import *

def genBoard():
   board = [13,11,12,15,14,12,11,13,
           10,10,10,10,10,10,10,10,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           0,0,0,0,0,0,0,0,
           20,20,20,20,20,20,20,20,
           23,21,22,25,24,22,21,23]

   return board

def printBoard(board):
   if len(board) != 64:
      return False
   b = []
   index = 0
   for i in board:
      if i == 10:
         b = b + ['wp']
      elif i == 11:
         b = b + ['wk']
      elif i == 12:
         b = b + ['wb']
      elif i == 13:
         b = b + ['wr']
      elif i == 14:
         b = b + ['wq']
      elif i == 15:
         b = b + ['wK']
      elif i == 20:
         b = b + ['bp']
      elif i == 21:
         b = b + ['bk']
      elif i == 22:
         b = b + ['bb']
      elif i == 23:
         b = b + ['br']
      elif i == 24:
         b = b + ['bq']
      elif i == 25:
         b = b + ['bK']
      else:
         if index%2 == 0 and (-1<index<8 or 15<index<24 or 31<index<40 or 47<index<56):
            b = b + ['_']
         elif index%2 == 0 and (7<index<16 or 23<index<32 or 39<index<48 or 55<index):
            b = b + ['#']
         elif index%2 != 0 and (-1<index<8 or 15<index<24 or 31<index<40 or 47<index<56):
            b = b + ['#']
         elif index%2 != 0 and (7<index<16 or 23<index<32 or 39<index<48 or 55<index):
            b = b + ['_']
      index += 1

   r = ''
   for i in range(56,64,1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' +  r + '  '
      else:
         r = b[i] + ' ' +  r + ' '
   print(r)

   r = ''
   for i in range(48,56,1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' +  r + '  '
      else:
         r = b[i] + ' ' +  r + ' '
   print(r)

   r = ''
   for i in range(40,48,1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' +  r + '  '
      else:
         r = b[i] + ' ' +  r + ' '
   print(r)

   r = ''
   for i in range(32,40,1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' +  r + '  '
      else:
         r = b[i] + ' ' +  r + ' '
   print(r)
   
   r = ''
   for i in range(24,32,1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' +  r + '  '
      else:
         r = b[i] + ' ' +  r + ' '
   print(r)

   r = ''
   for i in range(16,24,1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' +  r + '  '
      else:
         r = b[i] + ' ' +  r + ' '
   print(r)

   r = ''
   for i in range(8,16,1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' +  r + '  '
      else:
         r = b[i] + ' ' +  r + ' '
   print(r)

   r = ''
   for i in range(0,8,1):
      if b[i] == '#' or b[i] == '_':
         r = b[i] + '  ' +  r + '  '
      else:
         r = b[i] + ' ' +  r + ' '
   print(r)

def GetPlayerPositions(board,player):
   if(player!=10) and (player!=20):
      return [False]   

   pos = []
   for i in range(0, len(board),1):
      if(type(board[i])==int):
         if(((board[i]-player)>=0)and((board[i]-player)<10)):
            pos = pos + [i]
   return pos      
   
def GetPieceLegalMoves(board,position):
   moves = []
   
   h = (position%8)
   v = (position - h)/8
   

   if(position>(len(board))-1):
      return False
   i = board[position]
   if (i == 10)and(v<7):

      if (board[position + 8]==0):
         moves = moves + [position+8]
      if ((board[position+7]-20>=0)and(position%8!=0)):    
         moves = moves + [position+7]
      if ((board[position+9]-20>=0)and(position%8!=7)):
         moves = moves + [position+9]

   elif (i == 20)and(v>0):
      if (board[position-8]==0):
         moves = moves + [position-8]
      if ((board[position-7]-10>=0)and(position%8!=0)and(board[position-7]-10<10)):    
         moves = moves + [position-7]
      if ((board[position-9]-10>=0)and(position%8!=0)and(board[position-9]-10<10)):    
         moves = moves + [position-9]

   elif (i == 11) or (i == 21):
      if ((position%8<7)):    
          if(position<48)and((board[position+17]==0)or((board[position+17]-i<-1 )or(board[position+17]-i>4))):
             moves = moves + [position+17] ##Upside down L -||.
          if(position>15)and((board[position-15]==0)or((board[position-15]-i<-1 )or(board[position-15]-i>4))):
             moves = moves + [position-15] ##Mirrored L -||^
      if ((position%8>0)):    
          if(position<48)and((board[position+15]==0)or((board[position+15]-i<-1 )or(board[position+15]-i>4))):
             moves = moves + [position+15] ##Upside down and mirrored L .-||
          if(position>15)and((board[position-17]==0)or((board[position-17]-i<-1 )or(board[position-17]-i>4))):
             moves = moves + [position-17] ##L ^||-
      if ((position%8<6)):    
          if(position<56)and((board[position+10]==0)or((board[position+10]-i<-1 )or(board[position+10]-i>4))):
             moves = moves + [position+10] ##--|.
          if(position>7)and((board[position-6]==0)or((board[position-6]-i<-1 )or(board[position-6]-i>4))):
             moves = moves + [position-6] ## -||^
      if ((position%8)>1):
          if(position<56)and((board[position+6]==0)or((board[position+6]-i<-1 )or(board[position+6]-i>4))):
             moves = moves + [position+6] ## .|--
          if(position>7)and((board[position-10]==0)or((board[position-10]-i<-1 )or(board[position-10]-i>4))):
             moves = moves + [position-10] ## ^|--
      
   elif (i == 12) or (i == 22):


      temppos = position
      while(temppos%8>0) and (temppos>7):
         temppos = temppos - 9
         if(board[temppos]==0):
            moves = moves + [temppos]      
         elif (board[temppos]-i<-2)or(board[temppos]-i>3):
            moves = moves + [temppos]
            break
         else:      
            break


      temppos = position
      while(temppos%8<7) and (temppos>7):
         temppos = temppos - 7
         if(board[temppos]==0):
            moves = moves + [temppos]      
         elif (board[temppos]-i<-2)or(board[temppos]-i>3):
            moves = moves + [temppos]
            break
         else:      
            break

      temppos = position
      while(temppos%8>0) and (temppos<56):
         temppos = temppos + 7
         if(board[temppos]==0):
            moves = moves + [temppos]      
         elif (board[temppos]-i<-2)or(board[temppos]-i>3):
            moves = moves + [temppos]
            break
         else:      
            break

      temppos = position
      while(temppos%8<7) and (temppos<56):
         temppos = temppos + 9
         if(board[temppos]==0):
            moves = moves + [temppos]      
         elif (board[temppos]-i<-2)or(board[temppos]-i>3):
            moves = moves + [temppos]
            break
         else:      
            break

   elif (i == 13) or (i == 23):

      h_dis = position%8
      v_dis = int((position-(position%8)) ) #could add / sign here 
              
      for x in range(int(v_dis/8)+1,8,1):
         if(board[8*x+h_dis]==0): #instead of here
            moves = moves + [8*x+h_dis]
         elif (board[8*x+h_dis]-i<-3)or(board[8*x+h_dis]-i>2):
            moves = moves + [8*x+h_dis]
            break
         else:      
            break

      for x in range(int(v_dis/8)-1,-1,-1):
         if(board[8*x+h_dis]==0): #instead of here
            moves = moves + [8*x+h_dis]
         elif (board[8*x+h_dis]-i<-3)or(board[8*x+h_dis]-i>2):
            moves = moves + [8*x+h_dis]
            break
         else:      
            break

      for x in range(h_dis+1,8,1):
         if(board[x+v_dis]==0): #instead of here
            moves = moves + [x+v_dis]
         elif (board[x+v_dis]-i<-3)or(board[x+v_dis]-i>2):
            moves = moves + [x+v_dis]
            break
         else:      
            break

      for x in range(h_dis-1,-1,-1):
         if(board[x+v_dis]==0): #instead of here
            moves = moves + [x+v_dis]
         elif (board[x+v_dis]-i<-3)or(board[x+v_dis]-i>2):
            moves = moves + [x+v_dis]
            break
         else:      
            break


   elif (i == 14) or (i == 24):

      h_dis = position%8
      v_dis = int((position-(position%8)) ) #could add / sign here 
              
      for x in range(int(v_dis/8)+1,8,1):
         if(board[8*x+h_dis]==0): #instead of here
            moves = moves + [8*x+h_dis]
         elif (board[8*x+h_dis]-i<-4)or(board[8*x+h_dis]-i>1):
            moves = moves + [8*x+h_dis]
            break
         else:      
            break

      for x in range(int(v_dis/8)-1,-1,-1):
         if(board[8*x+h_dis]==0): #instead of here
            moves = moves + [8*x+h_dis]
         elif (board[8*x+h_dis]-i<-4)or(board[8*x+h_dis]-i>1):
            moves = moves + [8*x+h_dis]
            break
         else:      
            break

      for x in range(h_dis+1,8,1):
         if(board[x+v_dis]==0): #instead of here
            moves = moves + [x+v_dis]
         elif (board[x+v_dis]-i<-4)or(board[x+v_dis]-i>1):
            moves = moves + [x+v_dis]
            break
         else:      
            break

      for x in range(h_dis-1,-1,-1):
         if(board[x+v_dis]==0): #instead of here
            moves = moves + [x+v_dis]
         elif (board[x+v_dis]-i<-4)or(board[x+v_dis]-i>1):
            moves = moves + [x+v_dis]
            break
         else:      
            break

      temppos = position
      while(temppos%8>0) and (temppos>7):
         temppos = temppos - 9
         if(board[temppos]==0):
            moves = moves + [temppos]      
         elif (board[temppos]-i<-4)or(board[temppos]-i>1):
            moves = moves + [temppos]
            break
         else:      
            break


      temppos = position
      while(temppos%8<7) and (temppos>7):
         temppos = temppos - 7
         if(board[temppos]==0):
            moves = moves + [temppos]      
         elif (board[temppos]-i<-4)or(board[temppos]-i>1):
            moves = moves + [temppos]
            break
         else:      
            break

      temppos = position
      while(temppos%8>0) and (temppos<56):
         temppos = temppos + 7
         if(board[temppos]==0):
            moves = moves + [temppos]      
         elif (board[temppos]-i<-4)or(board[temppos]-i>1):
            moves = moves + [temppos]
            break
         else:      
            break

      temppos = position
      while(temppos%8<7) and (temppos<56):
         temppos = temppos + 9
         if(board[temppos]==0):
            moves = moves + [temppos]      
         elif (board[temppos]-i<-4)or(board[temppos]-i>1):
            moves = moves + [temppos]
            break
         else:      
            break

   elif (i == 15) or (i == 25):   #KING#
      if (i==15):
         opp = 25
      else:
         opp = 15
    
      temppos = position - 8
      if(temppos>7)and((board[temppos]==0) or(board[temppos]-i<-5)or(board[temppos]-i>1)):
         moves = moves + [temppos]

      temppos = position + 1
      if(temppos%8<7)and((board[temppos]==0) or(board[temppos]-i<-5)or(board[temppos]-i>1)and(KingMoves(board,temppos,i-5))):
         moves = moves + [temppos]

      temppos = position - 1 
      if(temppos%8>0)and((board[temppos]==0) or(board[temppos]-i<-5)or(board[temppos]-i>1)):
         moves = moves + [temppos]
            
      temppos = position + 8
      if(temppos<56)and((board[temppos]==0) or(board[temppos]-i<-5)or(board[temppos]-i>1)):
         moves = moves + [temppos]

      temppos = position - 9
      if(temppos%8>0)and(temppos>7)and((board[temppos]==0) or(board[temppos]-i<-5)or(board[temppos]-i>1)):
         moves = moves + [temppos]

      temppos = position - 7
      if(temppos%8<7)and(temppos>7)and((board[temppos]==0) or(board[temppos]-i<-5)or(board[temppos]-i>1)):
         moves = moves + [temppos]

      temppos = position + 7 
      if(temppos%8>0)and(temppos<56)and((board[temppos]==0) or(board[temppos]-i<-5)or(board[temppos]-i>1)):
         moves = moves + [temppos]
            
      temppos = position + 9
      if(temppos%8<7)and(temppos<56)and((board[temppos]==0) or(board[temppos]-i<-5)or(board[temppos]-i>1)):
         moves = moves + [temppos]

   else:
     return []

   return moves

def IsPositionUnderThreat(board,position,player):
   opp = []
   oppmove = []
   if (player==10):
      opp = GetPlayerPositions(board,20)
   else:
      opp = GetPlayerPositions(board,10)  
   
   for i in range(0,len(opp),1):
      oppmove = GetPieceLegalMoves(board,opp[i])
      for j in range(0,len(oppmove),1):
         if position == oppmove[j]:
            return True
   return False   
  
def check(board,player):
   king = 0
   for i in range(0,len(board),1):
      if board[i] == player + 5:
         king = i
   return IsPositionUnderThreat(board, king, player)
 
def KingMoves(board,position,player):   
   if(board[position]!=15) and (board[position]!=25):
      return False
   threat = []
   safe = []
   possible = GetPieceLegalMoves(board,position)
   #possible = [position-9,position-8,position-7,position-1,position+1,position+7,position+8,position+9]
   for i in range(0,len(possible),1):
      threat = threat + [IsPositionUnderThreat(board,possible[i],player)]
   for x in range(0,len(threat),1):
      if(threat[x]==False):
         safe = safe + [possible[x]] 
   return safe 

def safe(board,position,player):
   accum = []
   moves = GetPieceLegalMoves(board,position)
   for i in moves:    
      if not(IsPositionUnderThreat(board,i,player)):
         accum = accum + [i]
   return accum

def capture(board,newpos,player):
   opp = board[newpos]
   points = 0
   if(opp-player>-1)and(opp-player<6):
      points = 0
   elif(opp==15)or(opp==25):
      points = 900  #check
   elif(opp==14)or(opp==24):
      points = 90
   elif(opp==13)or(opp==23):
      points = 50
   elif(opp==12)or(opp==22):
      points = 30
   elif(opp==11)or(opp==21):
      points = 30
   elif(opp==10)or(opp==20):
      points = 10
   return points

def pieceVal(piece):
   if (piece==10) or (piece==20):
      return 10
   elif (piece==11) or (piece==21):
      return 30
   elif (piece==12) or (piece==22):
      return 30
   elif (piece==13) or (piece==23):
      return 50
   elif (piece==14) or (piece==24):
      return 90
   elif (piece==15) or (piece==25):
      return 900
   else:
      return False
 
def positionWeight(board,position,newpos,player):
   i = board[position]
   points = 0
   if(i==10)or(i==20):
      points = pawnPos(board,newpos,position)
   elif(i==11)or(i==21):
      points = knightPos(board,newpos)
   elif(i==12)or(i==22):
      points = bishopPos(board,newpos,position)
   elif(i==13)or(i==23):
      points = rookPos(board,newpos,position)
   elif(i==14)or(i==24):
      points = queenPos(board,newpos)
   elif(i==15)or(i==25):
      points = kingPos(board,newpos,position)
   if(IsPositionUnderThreat(board,newpos,player)==True):
      #print("$$$$$$$")
      #print(points)
      
      points = points - (pieceVal(i))

      #print("$$$$$$$")
      #print(points)
   return points   

def pawnPos(board,newpos,position):
   i = board[position]
   if(i==20):
      evalBoard = [
         0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
         5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
         1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
         0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
         0.0,  2.0,  1.5,  1.5,  1.5,  1.5,  2.0,  0.0,
         0.5,  1.5,  1.2,  1.2,  1.2,  1.2,  1.5,  0.5,
         0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5,
         0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
      return evalBoard[newpos]

   elif(i==10):
      evalBoard = [ 
         0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
         0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5,
         0.5,  1.5,  1.2,  1.2,  1.2,  1.2,  1.5,  0.5,
         0.0,  2.0,  1.5,  1.5,  1.5,  1.5,  2.0,  0.0,
         0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
         1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
         5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
         0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]

   return evalBoard[newpos]

def knightPos(board,newpos):
   evalBoard = [
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
        -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
        -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
        -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
        -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
        -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
        -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
        -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
   return evalBoard[newpos]

def bishopPos(board,newpos,position):
   i = board[position]
   if(i==22):
      evalBoard = [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
                    -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
                    -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
                    -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
                    -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
                    -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
                    -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
                    -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
      return evalBoard[newpos]
   
   elif(i==12):
      evalBoard = [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
                    -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
                    -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
                    -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
                    -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
                    -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
                    -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
                    -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
      return evalBoard[newpos]

def rookPos(board,newpos,position):
   i = board[position]
   if(i==23): 
      evalBoard = [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
                     0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                     0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
      return evalBoard[newpos]

   elif(i==13):  
      evalBoard = [  0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                    -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
                     0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5,
                     0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]

      return evalBoard[newpos]

def queenPos(board,newpos):
   evalBoard= [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
                -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
                -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
                -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
                 0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
                -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
                -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
                -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
   return evalBoard[newpos]

def kingPos(board,newpos,position):
   i = board[position]
   if(i==15):
      evalBoard = [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0,
                     2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
                    -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
                    -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,  
                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0]
      return evalBoard[newpos]
   
   elif(i==25):
      evalBoard = [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                    -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
                    -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
                    -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
                     2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0,
                     2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0]
      return evalBoard[newpos]
   else: 
      return 0


def candidateMoves(board,player):
   accum = []
   
   playerPositions = GetPlayerPositions(board,player)

   for i in playerPositions:
      moves = GetPieceLegalMoves(board,i)
      for j in moves:
         if(check(board,player)==True):
            b = list(board)
            b[j] = b[i]
            b[i] = 0
            if check(b,player)==False:
               accum = accum +   [[[i,j],float(getPoints(board,i,j,player))]]
         else:

            accum = accum +   [[[i,j],float(getPoints(board,i,j,player))]]
   return accum

def top5(board,player,x):
   xTest = tree([[-1,-1],0])
   moves = []
   max1 = [[-1,-1],-1]
   max2 = [[-1,-1],-1]
   max3 = [[-1,-1],-1]
   max4 = [[-1,-1],-1]
   max5 = [[-1,-1],-1]
   max6 = [[-1,-1],-1]


   L = candidateMoves(board,player)

   for i in L:
         
      if (i[1]>max1[1]):
         max6 = max5
         max5 = max4
         max4 = max3
         max3 = max2
         max2 = max1
         max1 = i
      elif (i[1]>max2[1]):
         max6 = max5
         max5 = max4
         max4 = max3
         max3 = max2
         max2 = i
      elif (i[1]>max3[1]):
         max6 = max5
         max5 = max4

         max4 = max3
         max3 = i
      elif (i[1]>max4[1]):
         max6 = max5
         max5 = max4
         max4 = i
      elif (i[1]>max5[1]):
         max6 = max5
         max5 = i
      elif (i[1]>max6[1]):
         max6 = i

   moves = moves + [max1] + [max2] + [max3] + [max4] + [max5] + [max6]
   for l in moves:
      q = tree(l)
      x.AddSuccessor(q) 
   return x
   
def chessPlayer(board,player):
   if(player==10):
      oppPlayer = 20
   else:
      oppPlayer = 10
   x = tree([[-1,-2],0])

   #print("********************************************************")
   #print(top5(board,player,x))
   #print("********************************************************")
   top5(board,player,x)
   accum = x.getChildren()
   for i in accum:
      b = list(board)
      b[i.getMove()] = b[i.getPos()]
      b[i.getPos()] = 0
      top5(b,oppPlayer,i)         
      accum1 = i.getChildren()
      for j in accum1:
         b1 = list(b)
         b1[j.getMove()] = b1[j.getPos()]
         b1[j.getPos()] = 0
         top5(b1,player,j)
         accum2 = j.getChildren()
         for k in accum2:
            b2 = list(b1)
            b2[k.getMove()] = b2[k.getPos()]
            b2[k.getPos()] = 0
            top5(b2,oppPlayer,k)
            accum3 = k.getChildren()
            for l in accum3:
               b3 = list(b2)
               b3[l.getMove()] = b3[l.getPos()]
               b3[l.getPos()] = 0
               top5(b3,player,l)
               accum4 = l.getChildren()
               #for m in accum4:
                  #b4 = list(b3)
                  #b4[m.getMove()] = b3[l.getPos()]
                  #b4[m.getPos()] = 0
                  #top5(b4,oppPlayer,m)
                  #accum5 = m.getChildren()
                  #for n in accum5:
                     #b5 = list(b4)
                     #b5[m.getMove()] = b3[l.getPos()]
                     #b5[m.getPos()] = 0
                     #top5(b5,player,n)



   #x.Print_DepthFirst()
   #print("##################################")
   #print("x.store: " + str(x.store))
   #print("x.store[0][0]: " + str(x.store[0][0]))
   #print("x.store[0][0][0]: " + str(x.store[0][0][0]))
   #print("x.store[0][0][1]: " + str(x.store[0][0][1]))
    
   #print("##################################")
   #print(x.children)

   #print("##################################")
   #print(x.value)
   #print()
   if check(board,player)==True:
      M = candidateMoves(board,player)
      index = maxPointIndex(M) 
      move = M[index]
   else:
      y = AlphaBeta(x)
      move = y.alpha_beta_search(x)
   print("Move in chessplayer: " + str(move) )
   evalTree = x.Get_LevelOrder()
   #evalTree = x   
 
   print()
   print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
   print(move)
    
   return [True,move,x.getChildren(),evalTree]

def maxPointIndex(lst):
   index = 0 
   for i in range(0,len(lst),1):
      if(lst[i][1]>lst[index][1]):
         index = i
   return index


def getPoints(board,position,newpos,player):
   points = 0
   points = points + capture(board,newpos,player)
   points = points + positionWeight(board,position,newpos,player) 
   return points

"""
def main():
   board = genBoard()
   printBoard(board)
   #print(positionWeight(board,35,36))
   #print(getPoints(board,35,36,20))
   
   #print(candidateMoves(board,20))

   #chessPlayer(board,20)
   print(chessPlayer(board,20))
   #print(GetPieceLegalMoves(board,26))
   #print(safe(board,26,20))
   
   return True
"""


def main():
   board = genBoard()
   
   #board = [0,0,0,0,0,0,0,0,
   #         0,0,0,0,0,0,0,0,
   #         0,0,0,0,0,0,0,0,
   #         0,0,0,0,0,25,0,0,
   #         0,0,0,0,0,0,0,0,
   #         0,0,0,0,0,0,14,0,
   #         0,0,0,0,0,0,0,0,
   #         0,0,0,0,0,0,0,0]

           
   done=False
   #chessPlayer(board,10)
   while not(done):
      printBoard(board)
      valid = False
      """
      while valid==False:
         print(GetPlayerPositions(board,10))
         position = int(input("White Piece Position 0<=x<=63: "))
         moves = GetPieceLegalMoves(board,position)
         print(moves)
         x = int(input("White move 0<=x<=63: "))


         for i in range(0,len(moves),1):
            if x==moves[i]:
               valid = True
         if(valid == True):
            print("Valid")
            #board[x] = board[position]
            #board[position] = 0
         else:
            print("Invalid move")
      board[x] = board[position]
      board[position] = 0
      """

      #print("Candidate Moves: " + str(candidateMoves(board,10)))
      hold = chessPlayer(board,10)
      move = hold[1]
      
      board[move[0][1]] = board[move[0][0]]
      board[move[0][0]] = 0
      
      printBoard(board)
      #print("Candidate Moves: " + str(candidateMoves(board,20)))
      hold = chessPlayer(board,20)
      move = hold[1]
      
      board[move[0][1]] = board[move[0][0]]
      board[move[0][0]] = 0


      #verify this is a legal move otherwise re-ask for a move
      
      #bestmove = evalTree(board,player)
      #board[bestmove]
      

main()
 
