import random


def bogo_sort(a):
    n = len(a)
    while is_sorted(a) == False:
        shuffle(a)
        print(a)


def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            return False
    return True


def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]


listToSort = [3, 1, 2, 6, 8, 5, 7]
bogo_sort(listToSort)
