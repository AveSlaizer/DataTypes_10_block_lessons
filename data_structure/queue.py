

class Queue:

    def __init__(self):
        self.__data = []

    def enqueue(self, item):
        self.__data.append(item)

    def dequeue(self):
        return self.__data.pop(0)

    def peek(self):
        return self.__data[0]

    def size(self):
        return len(self.__data)

    def is_empty(self):
        return not self.__data

    # enqueue(item) – добавление нового элемента в очередь.
    # dequeue() – удаление и возврат очередного элемента в порядке «первым вошел, первым вышел» (First In First Out – FIFO).
    # peek() – возврат(без удаления) очередного элемента в очереди в порядке FIFO.
    # size() – возврат количества элементов в очереди (будет использоваться __len()__)
    # is_ empty() – возврат True, если в очереди нет элементов, иначе возврат False.
