class MyQueue:

    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []

    def push(self, x: int) -> None:
        self.__stack1.append(x)

    def pop(self) -> int:
        while len(self.__stack1) > 0:
            self.__stack2.append(self.__stack1.pop())
        first = self.__stack2.pop()
        while len(self.__stack2) > 0:
            self.__stack1.append(self.__stack2.pop())
        return first

    def peek(self) -> int:
        while len(self.__stack1) > 0:
            self.__stack2.append(self.__stack1.pop())
        first = self.__stack2[-1]
        while len(self.__stack2) > 0:
            self.__stack1.append(self.__stack2.pop())
        return first

    def empty(self) -> bool:
        if not self.__stack1:
            return True
        else:
            return False
