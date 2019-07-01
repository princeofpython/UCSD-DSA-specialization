# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 21:57:55 2019

@author: Dell
"""

import random
def max_pairwise_product_fast(n, a):
      global fast
      max_index1 = -1
      for i in range(n):
          if max_index1 == -1 or a[i] > a[max_index1]:
              max_index1 = i

      max_index2 = -1
      for i in range(n):
          if i != max_index1 and (max_index2 == -1 or a[i] > a[max_index2]):
              max_index2 = i
      fast = a[max_index1] * a[max_index2]
      return fast

def max_pairwise_product(n, a):
            global result
            for i in range(0, n):
                for j in range(i + 1, n):
                    if a[i] * a[j] > result:
                        result = a[i] * a[j]
            return result

result = 0
fast = 0

while result == fast:
    if __name__ == '__main__':
        n = (random.randint(2, 11))
        a = list(random.randint(0, 99999) for r in range(n))
        assert (len(a) == n)
        result = max_pairwise_product(n, a)

        fast=max_pairwise_product_fast(n, a)
        print(fast, result, "OK")
    else:
        print("Wrong Answer")