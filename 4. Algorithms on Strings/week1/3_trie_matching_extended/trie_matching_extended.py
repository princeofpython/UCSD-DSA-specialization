# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def build_trie(patterns):
    tree = dict()
    node=0
    tree[node]=[dict(),False]
    for pattern in patterns:
        currNode=0
        letter=0
        length=len(pattern)
        while letter<length and pattern[letter] in tree[currNode][0]:
            currNode=tree[currNode][0][pattern[letter]]
            letter+=1
        while letter<length:
            node+=1
            tree[currNode][0][pattern[letter]]=node
            tree[node]=[dict(),False]
            currNode=node
            letter+=1
        tree[currNode][1]=True
    return tree 
def PrefixTrieMatching(text, tree):
	currNode = 0
	letter = 0
	length = len(text)
	alpha = text[letter]
	while True:
		if tree[currNode][1]:
			return True
		elif alpha in tree[currNode][0]:
			currNode=tree[currNode][0][alpha]
			letter+=1
			if letter==length and ( tree[currNode][1]==False):
				return False
			elif letter<length:
				alpha=text[letter]
		else:
			return False


def solve (text, n, patterns):
	result = []
	tree= build_trie(patterns)
	#print(tree)
	length = len(text)
	for i in range(length):
		if PrefixTrieMatching(text[i:], tree ):
			result.append(i)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
