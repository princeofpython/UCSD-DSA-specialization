# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    self.resultIN = []
    self.resultPRE = []
    self.resultPOST = []
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,index=0):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if self.left[index]!=-1:
      self.inOrder(self.left[index])
    self.resultIN.append(self.key[index])
    if self.right[index]!=-1:
      self.inOrder(self.right[index])


  def preOrder(self,index=0):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.resultPRE.append(self.key[index])
    if self.left[index]!=-1:
      self.preOrder(self.left[index])
    if self.right[index]!=-1:
      self.preOrder(self.right[index])            

  def postOrder(self,index=0):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if self.left[index]!=-1:
      self.postOrder(self.left[index])
    if self.right[index]!=-1:
      self.postOrder(self.right[index])  
    self.resultPOST.append(self.key[index])         

def main():
	tree = TreeOrders()
	tree.read(); tree.inOrder(); tree.preOrder();  tree.postOrder()
	print(" ".join(str(x) for x in tree.resultIN))
	print(" ".join(str(x) for x in tree.resultPRE))
	print(" ".join(str(x) for x in tree.resultPOST))

threading.Thread(target=main).start()
