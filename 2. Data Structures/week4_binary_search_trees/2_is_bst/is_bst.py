#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c
    return self.n

  def isBinarySearchTree(self,index=0):
    if self.left[index]==-1 and self.right[index]==-1:
      return self.key[index],self.key[index],True
    
    if self.left[index]!=-1:
      left=self.isBinarySearchTree(self.left[index])
      #leftMin=left[0]
      #leftMax=left[1]
      #leftbool=left[2]

    if self.right[index]!=-1:
      right=self.isBinarySearchTree(self.right[index])
    if self.left[index]==-1:
      return min(self.key[index],right[0]), right[1], self.key[index]<=right[0] and right[2]

    elif self.right[index]==-1:
      return left[0], max(self.key[index],left[1]), self.key[index]>left[1] and left[2]

    else:
      return min(self.key[index],left[0]), max(self.key[index],right[1]), self.key[index]>left[1] and self.key[index]<=right[0] and left[2] and right[2]
    
def main():
  tree = Tree()
  n=tree.read()
  if n==0 or tree.isBinarySearchTree()[2]:
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
