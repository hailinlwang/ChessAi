
      """ 
      valid = False
      printBoard(board)
      while valid==False:
         position = int(input("Black Piece Position 0<=x<=63: "))
         if (position - 20) < 0 :
            print("invalid")
         else: 
            x = int(input("Black move 0<=x<=63: "))
            moves = GetPieceLegalMoves(board,position)
            for i in range(0,len(moves),1):
               if x==moves[i]:
                  valid = True
         if(valid == True):
            print("Valid")
         else:
            print("Invalid move")

      board[x] = board[position]
      board[position] = 0

      #verify this is a legal move otherwise re-ask for a move
      """
