class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty")

    def isEmpty(self):
        return not self.items

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise ValueError("Stack is empty")

    def size(self):
        return len(self.items)

def evaluate_postfix(expr):
    stack = Stack()
    for token in expr.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in {'+', '-', '*', '/'}:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                result = num1 + num2
            elif token == '-':
                result = num1 - num2
            elif token == '*':
                result = num1 * num2
            elif token == '/':
                result = num1 / num2
            stack.push(result)
    return stack.pop()


def parse_sentence(sentence):
    stack = Stack()
    words = []
    for char in sentence:
        if char.isalpha():
            stack.push(char)
        elif char == '(':
            stack.push('(')
        elif char == ')':
            while stack.peek() != '(':
                words.append(stack.pop())
            stack.pop()  # remove the '('
        elif char == ' ':
            while stack.peek() != '(':
                words.append(stack.pop())
            if stack.isEmpty():  # added check
                break
    while stack.peek() != '(':
        words.append(stack.pop())
    return words


ans = parse_sentence("hello (world) (this is) a test")
print(ans)