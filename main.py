from data_structure.stack import Stack


def is_correct_brackets(sequence: str):
    """"""
    brackets_dict = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }
    stack = Stack()

    for symbol in sequence:
        if symbol in brackets_dict.keys():
            stack.push(symbol)
        elif not stack.is_empty() and symbol == brackets_dict[stack.peek()]:
            stack.pop()
        else:
            return False
    if stack.is_empty():
        return True
    return False


def execute_application():
    print(eval("8+3*2+7*(6+3*4)"))


if __name__ == "__main__":
    execute_application()
