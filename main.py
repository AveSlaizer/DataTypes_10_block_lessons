from data_structure.priorityQueue import PriorityQueue
from data_structure.heapSort import heap_sort


def execute_application():
    queue = PriorityQueue()
    queue.insert("123", 3)
    queue.insert("ky=ky", 13)
    queue.insert("кря", 14)
    print(queue)



if __name__ == "__main__":
    execute_application()