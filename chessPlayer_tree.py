from chessPlayer_queue import *



class tree:
    def __init__(self,x):
        self.store = [x,[]]
        self.root = self.store[0]
        self.Name = self.store[0]
        self.children = self.store[1]   
        self.value = self.store[0][1] 

    def AddSuccessor(self,x):

        #self.store[1] = self.store[1] + [x]
        self.store[1] += [x]
        return True

    def getChildren(self):
        #print(self.children)
        return self.children
    
    def getMove(self):
        return self.store[0][0][1]
    
    def getPos(self):
        return self.store[0][0][0]
    
    def Print_DepthFirst(self):
        self.Print_DepthFirst_helper("   ")
        return True


    def Print_DepthFirst_helper(self,prefix):
        print (prefix+str(self.store[0]))
        for i in self.store[1]:
             i.Print_DepthFirst_helper(prefix+"   ")
        return True


    def Get_LevelOrder(self):
       x=queue()
       x.enqueue(self.store)
       accum=[]
       while True:
          y=x.dequeue()
          # y is a 2-list where y[0]=True/False
          # and y[1] is the actual dequeued value when y[0]=True
          if (y[0]==False):
             break
          else:
             v=y[1]
             accum=accum+[v[0]]
             for i in v[1]:
                x.enqueue(i.store)
       return accum

def main():
   """
   a = tree(10)
   b = tree(20)
   c = tree(30)

   a.AddSuccessor(b)
   a.AddSuccessor(c)
   a.Print_DepthFirst()
   a.getChildren()
   """

main()
