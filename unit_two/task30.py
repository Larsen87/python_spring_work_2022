# todo: Найти сумму элементов матрицы,
# Написать msum(matrix)  которая подсчитывает сумму всех элементов функцию Найти сумму всех элементов матрицы:
#
# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21
#
# >>> msum(load_matrix('matrix.txt'))
# 423

matrix = [[1, 2, 3], [4, 5, 6]]


def msum(matrix):
    res = sum([x for i in matrix for x in i])
    return print(res)


def load_matrix(filename):
    with open(filename, mode="rt", encoding="UTF-8") as f:
        lines = f.readlines()
        res = [[int(i) for i in new_lists] for new_lists in [i.split() for i in lines]] \
            if len(set(len(i) for i in [i.split() for i in lines])) == 1 else False
        f.close()
        return res


msum(matrix)
msum(load_matrix('matrix.txt'))
