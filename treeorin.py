from queue import *



class tree:
    def __init__(self,x):
        self.store = [x,[]]
        self.root = self.store[0]
        self.Name = self.store[0]
        self.children = self.store[1]   
        self.value = self.store[0] 

    def AddSuccessor(self,x):

        #self.store[1] = self.store[1] + [x]
        self.store[1] += [x]
        return True

    def getChildren(self):
        print(self.children)

    def Print_DepthFirst(self):
        self.Print_DepthFirst_helper("   ")
        return True


    def Print_DepthFirst_helper(self,prefix):
        print (prefix+str(self.store[0]))
        for i in self.store[1]:
             i.Print_DepthFirst_helper(prefix+"   ")
        return True


    def Get_LevelOrder (self):
        x = queue()
        x.enqueue(self)
        accum = []
        while x.empty() == False:
            r = x.dequeue()
            accum = accum + [r.store[0]]
            for i in r.store[1:len(r.store)][0]:
                x.enqueue(i)
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
