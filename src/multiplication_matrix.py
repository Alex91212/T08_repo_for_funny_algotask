# mat_one = [[1, 2], [3, 4]]
# mat_two = [[5, 6], [7, 8]]
#
# mat_rez = [[0, 0], [0, 0]]
# 1 2 * 5 6 = 5+14  6+16  = 19 22
# 3 4   7 8   15+28 18+32   43 50

def infill_mat(n):
    mat = []
    for i in range(n):
        tmp_arr = []
        for j in range(n):
            num = int(input())
            tmp_arr.append(num)
        mat.append(tmp_arr)
    return mat

def infill_zero(n):
    mat = []
    for i in range(n):
        mat.append([0] * n)
    return mat

print("введите размерность квадратных матриц, которые вы хотите перемножить")
cnt = int(input())

mat_one = infill_mat(cnt)
mat_two = infill_mat(cnt)
print(mat_one)
print(mat_two)

mat_rez = infill_zero(cnt)
print(mat_rez)

for i in range(cnt):
    n = 0
    for j in range(cnt * cnt):
        mat_rez[i][n] += mat_one[i][j % cnt] * mat_two[j % cnt][n]
        if ((j % cnt) == cnt - 1):
            n += 1


print(mat_rez)
