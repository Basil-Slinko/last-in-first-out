class Stack:

    def __init__(self, stack):
        self.stack = stack

    def is_empty(self):
        return bool(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()
        return self.stack[-1]

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack_list = Stack([1, 2, 3, 4, 5])
    print(stack_list.peek())
