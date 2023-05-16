class Stack:

    def __init__(self):
        self.__data = []

    @staticmethod
    def __is_integer(item):
        if not isinstance(item, int):
            raise ValueError(f"Недопустимый тип данных '{item.__class__.__name__}', ожидался 'int'")

    def push(self, item: int):
        self.__is_integer(item)
        self.__data.append(item)

    def pop(self):
        return self.__data.pop()

    def peek(self):
        return self.__data[-1]

    def size(self):
        return self.__data.__len__()

    def is_empty(self):
        return self.size() == 0

    # push – добавление нового элемента в стек.
    # pop – удаление и возврат очередного элемента в порядке «последним пришел, первым вышел» (Last In First Out – LIFO)
    # peek – возврат очередного элемента в порядке «последним пришел, первым вышел» (LIFO).
    # size  –  возврат количества элементов в стеке (будет использоваться метод __len__).
    # is_empty – возврат True, если в стеке нет элементов, иначе возврат False
