from data_structure.stack import Stack


def execute_application():
    stack = Stack()

    stack.push(11)
    stack.push(22)
    stack.push(33)
    print(stack.size())
    print(stack.pop())
    print(stack.size())
    print(stack.peek())
    print(stack.is_empty())


if __name__ == "__main__":
    execute_application()
