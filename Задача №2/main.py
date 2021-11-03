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


def balance_check(string_with_brackets):
    stack_object = Stack()
    result_balance = 'Сбалансировано'
    result_unbalances = 'Несбалансированно'

    if len(string_with_brackets) % 2 != 0:
        return result_unbalances

    opening_brackets = set('([{')
    matching_brackets = {('(', ')'), ('{', '}'), ('[', ']')}

    for bracket in string_with_brackets:
        if bracket in opening_brackets:
            stack_object.push(bracket)
        else:
            if stack_object.size() == 0:
                return result_unbalances
            last_open = stack_object.pop()
            if (last_open, bracket) not in matching_brackets:
                return result_unbalances
    if stack_object.size() == 0:
        return result_balance


print(balance_check('()'))
print(balance_check('([])'))
print(balance_check('[([])((([[[]]])))]{()}'))
print(balance_check('{{[()]}}'))
print('-' * 30)
print(balance_check('}{}'))
print(balance_check('{{[(])]}}'))
print(balance_check('[[{())}]'))
