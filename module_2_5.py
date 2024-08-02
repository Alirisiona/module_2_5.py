n = int(input("Напишите количество строк матрицы: "))
m = int(input("Напишите количество столбцов матрицы: "))
value = input("Напишите  значения матрицы: ")

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return(matrix)

matrix = get_matrix(n, m, value)

if n <= 0:
    print([])
elif m <= 0:
    print([])
else:
    print(matrix)
