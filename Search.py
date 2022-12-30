from random import choice


def hoar_sort(array):
    '''
    Функция сортировки Хоара производит устойчивою сортировку массива array
    '''
    if len(array) <= 1:
        return
    barrier = array[0]
    left, middle, right = [], [], []
    for elem in array:
        if elem < barrier:
            left.append(elem)
        elif elem > barrier:
            right.append(elem)
        else:
            middle.append(elem)
    hoar_sort(left)
    hoar_sort(right)
    array.clear()
    array.extend(left)
    array.extend(middle)
    array.extend(right)


def merge_sort(array):
    '''
    Функция сортировки слиянием производит устойчивою сортировку массива array
    '''
    if len(array) <= 1:
        return
    middle = len(array) // 2
    left = [array[i] for i in range(0, middle)]
    right = [array[i] for i in range(middle, len(array))]
    merge_sort(left)
    merge_sort(right)
    i = j = 0
    c = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1
    c.extend(left[i:])
    c.extend(right[j:])
    for i in range(len(array)):
        array[i] = c[i]


def left_boundary(array, key):
    '''
    Функция бинарного поиска левой границы значения key в массиве array
    '''
    left = -1
    right = len(array)
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] < key:
            left = middle
        else:
            right = middle
    return left


def right_boundary(array, key):
    '''
    Функция бинарного поиска правой границы значения key в массиве array
    '''
    left = -1
    right = len(array)
    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] <= key:
            left = middle
        else:
            right = middle
    return right


def generate_numbers(N: int, M: int, prefix=None):
    '''
    Функция генерирует числа в системе счисления N
    с количеством знаков M с начальными значениями prefix
    '''
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M - 1, prefix)
        prefix.pop()


def largest_common_subsequence(first, second):
    '''
    Функция находит наибольшую общую подпоследовательность
    массивов first и second и возвращает ее длинну
    '''
    result = [[0] * (len(second) + 1) for i in range(len(first) + 1)]
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i - 1] == second[j - 1]:
                result[i][j] = 1 + result[i - 1][j - 1]
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])
    print(*result, sep='\n')
    return result[-1][-1]


def greatest_increasing_subsequence(array):
    '''
    Функция находит наибольшую возрастающую подпоследовательность
    массива array и возвращает ее длинну
    '''
    result = [0] * (len(array) + 1)
    for i in range(1, len(array) + 1):
        m = 0
        for j in range(0, i):
            if array[i - 1] > array[j - 1] and result[j] > m:
                m = result[j]
        result[i] = m + 1
    return result[-1]


def levenstain(first, second):
    '''
    Функция поиска наименьшего редакционного расстояния
    для приведени строки first к строке second
    возвращает наименьшее количество редакционных правок
    '''
    result = [[i + j if not i * j else 0 for j in range(len(second) + 1)] for i in range(len(first) + 1)]
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i - 1] == second[j - 1]:
                result[i][j] = result[i - 1][j - 1]
            else:
                result[i][j] = 1 + min(result[i - 1][j], result[i][j - 1], result[i - 1][j - 1])
    return result[-1][-1]


string_a = 'колокольня'
string_b = 'молокольня'
print(levenstain(string_a,string_b))
