# python3
import sys

def BWT(text):
    double =  2*text
    length = len(text)
    return ''.join([each[-1] for each in sorted([double[i:i+length] for i in range(length)])])

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))