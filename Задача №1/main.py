class Stack:

    def __init__(self):
        self.stack = list()

    def is_empty(self):
        return bool(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        result = self.stack[-1]
        self.stack.pop()
        return result

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack_list = Stack([1, 2, 3, 4, 5])
    print(stack_list.peek())
