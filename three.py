from random import randint as rand
main_matrix = []

#-------------------------------------------------------------------

for i in range(10):
    local_matrix = []
    for j in range(10):
        local_matrix.append(rand(1, 100)) #задаем матрицу
    main_matrix.append(local_matrix[:])

#-------------------------------------------------------------------

for i in main_matrix:
    print(i, '\n') #распечатаем матрицу

#-------------------------------------------------------------------


count = 0

for i in main_matrix:
    for j in i:
        if j < i[j + 1] and j<i[j - 1]

