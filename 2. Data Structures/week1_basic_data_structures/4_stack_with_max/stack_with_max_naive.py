#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.auxstack=[]

    def Push(self, a):
        self.__stack.append(a)
        if(self.auxstack):
            if self.auxstack[-1]<a:
                self.auxstack.append(a)
            else:
                self.auxstack.append(self.auxstack[-1])
        else:
            self.auxstack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.auxstack.pop()

    def Max(self):
        assert(len(self.__stack))
        return (self.auxstack[-1])


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
