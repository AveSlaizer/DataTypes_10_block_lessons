from data_structure.stack import Stack
from data_structure.queue import Queue
from data_structure.linkedList import LinkedList


def execute_application():
    lins = LinkedList()
    lins.add_first(1)
    lins.add_first(2)
    lins.add_last(3)
    lins.add_last(4)
    print(lins.remove_first())
    print(lins.remove_last())
    print(lins.remove_first())
    print(lins.remove_last())


if __name__ == "__main__":
    execute_application()
