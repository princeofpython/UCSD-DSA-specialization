# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def build_trie(patterns):
    tree = dict()
    # write your code here
    node=0
    tree[node]=dict()
    for pattern in patterns:
        currNode=0
        letter=0
        length=len(pattern)
        while letter<length and pattern[letter] in tree[currNode]:
            currNode=tree[currNode][pattern[letter]]
            letter+=1
        while letter<length:
            node+=1
            tree[currNode][pattern[letter]]=node
            tree[node]=dict()
            currNode=node
            letter+=1
    return tree

def PrefixTrieMatching(text, tree):
	currNode = 0
	letter = 0
	length = len(text)
	alpha = text[letter]
	while True:
		if len(tree[currNode])==0:
			return True
		elif alpha in tree[currNode]:
			currNode=tree[currNode][alpha]
			letter+=1
			if letter==length and len(tree[currNode]) != 0:
				return False
			elif letter<length:
				alpha=text[letter]
		else:
			return False


def solve (text, n, patterns):
	result = []
	tree = build_trie(patterns)
	length = len(text)
	for i in range(length):
		if PrefixTrieMatching(text[i:], tree):
			result.append(i)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
