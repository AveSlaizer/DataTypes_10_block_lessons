from data_structure.priorityQueue import PriorityQueue
from data_structure.heapSort import heap_sort
from heapq import heapify


def bubble_sorting(alist: list) -> list:
    """
    Сортировка пузырьком

    :type alist: object
    :param collection (list): Список для сортировки
    :return:
            collection (list): Отсортированный список
    """
    N = len(alist)
    for i in range(N - 1):
        swapped = True
        for j in range(N - i - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                swapped = False
        if swapped:
            break
    return alist


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
