# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return Bracket(next,i)
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return Bracket(next,i)
    if not opening_brackets_stack:
        return None 
    else:
        return opening_brackets_stack[0]

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch==None:
        print("Success")
    else:
        print(mismatch.position+1)

if __name__ == "__main__":
    main()
