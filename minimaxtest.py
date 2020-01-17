from treeorin import *

##########################
###### MINI-MAX A-B ######
##########################

class AlphaBeta:
    # print utility value of root node (assuming it is max)
    # print names of all nodes visited during search
    def __init__(self, game_tree):
        self.game_tree = game_tree  # GameTree
        self.root = game_tree.root  # GameNode
        return

    def alpha_beta_search(self, node):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity
        print("node: " + str(node))
        print("Children: " + str(node.children))
        successors = self.getSuccessors(node)
        print("successors: " + str(successors))
        best_state = None
        for state in successors:
            value = self.min_value(state, best_val, beta)
            if value > best_val:
                best_val = value
                best_state = state
        print( "AlphaBeta:  Utility Value of Root Node: = " + str(best_val))
        #print( "AlphaBeta:  Best State is: " + best_state.Name)
        return best_state

    def max_value(self, node, alpha, beta):
        print( "AlphaBeta-->MAX: Visited Node :: " + str(node.Name))
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = -infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = max(value, self.min_value(state, alpha, beta))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, node, alpha, beta):
        print( "AlphaBeta-->MIN: Visited Node :: " + str(node.Name))
        if self.isTerminal(node):
            return self.getUtility(node)
        infinity = float('inf')
        value = infinity

        successors = self.getSuccessors(node)
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value
    #                     #
    #   UTILITY METHODS   #
    #                     #

    # successor states in a game tree are the child nodes...
    def getSuccessors(self, node):
        assert node is not None
        return node.children

    # return true if the node has NO children (successor states)
    # return false if the node has children (successor states)
    def isTerminal(self, node):
        assert node is not None
        return len(node.children) == 0

    def getUtility(self, node):
        assert node is not None
        return node.value


def main():
   a1 = tree(6)
   a2 = tree(3)
   b2 = tree(6)
   c2 = tree(5)
   
   a3 = tree(5)
   b3 = tree(3)
   c3 = tree(6)
   d3 = tree(7)
   e3 = tree(5)
   f3 = tree(5)

   a4 = tree(5)
   b4 = tree(4)
   c4 = tree(3)
   d4 = tree(6)
   e4 = tree(6)
   f4 = tree(7)
   g4 = tree(5)
   h4 = tree(8)
   i4 = tree(6)

   a1.AddSuccessor(a2)
   a1.AddSuccessor(b2)   
   a1.AddSuccessor(c2)   

   a2.AddSuccessor(a3)
   a2.AddSuccessor(b3)
   b2.AddSuccessor(c3)
   b2.AddSuccessor(d3)
   c2.AddSuccessor(e3)
   c2.AddSuccessor(f3)

   a3.AddSuccessor(a4)
   a3.AddSuccessor(b4)
   b3.AddSuccessor(c4)
   c3.AddSuccessor(d4)
   c3.AddSuccessor(e4)
   d3.AddSuccessor(f4)
   e3.AddSuccessor(g4)
   f3.AddSuccessor(h4)
   f3.AddSuccessor(i4)

   y = AlphaBeta(a1)
   y.alpha_beta_search(a1)



main()

