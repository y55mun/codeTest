# 실패
# 45 합을 기준으로 만든 수도쿠
# 값이 중복되더라도 합이 45가 되는 반례가 존재함

'''
각 사각형의 합

a[0][0] a[0][1] a[0][2]
a[1][0] a[1][1] a[1][2]
a[2][0] a[2][1] a[2][2]

a[0][3] a[0][4] a[0][5]
a[1][3] a[1][4] a[1][5]
a[2][3] a[2][4] a[2][5]

a[0][6] a[0][7] a[0][8]
a[1][6] a[1][7] a[1][8]
a[2][6] a[2][7] a[2][8]

a[3][0] a[3][1] a[3][2]
a[4][0] a[4][1] a[4][2]
a[5][0] a[5][1] a[5][2]

a[3][3] a[3][4] a[3][5]
a[4][3] a[4][4] a[4][5]
a[5][3] a[5][4] a[5][5]

a[3][6] a[3][7] a[3][8]
a[4][6] a[4][7] a[4][8]
a[5][6] a[5][7] a[5][8]

a[6][0] a[6][1] a[6][2]
a[7][0] a[7][1] a[7][2]
a[8][0] a[8][1] a[8][2]

a[6][3] a[6][4] a[6][5]
a[7][3] a[7][4] a[7][5]
a[8][3] a[8][4] a[8][5]

a[6][6] a[6][7] a[6][8]
a[7][6] a[7][7] a[7][8]
a[8][6] a[8][7] a[8][8]

3개 * 3개 만큼 이중반복하면 될 듯!

'''

sudoku = [list(map(int, input().split())) for _ in range(9)]

cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in range(9):
    print(sum(sudoku[i]))
    if sum(sudoku[i]) == 45:
        cnt1 = 0
    else:
        cnt1 = 1

    tmp = 0
    for j in range(9):
        tmp += sudoku[j][i]
    print(tmp)
    if tmp == 45:
        cnt2 = 0
    else:
        cnt2 = 1

for l1 in range(3):
    for l2 in range(3):
        tmp2 = 0
        tmp2 += sudoku[l1 * 3][l2 * 3]
        tmp2 += sudoku[l1 * 3][l2 * 3 + 1]
        tmp2 += sudoku[l1 * 3][l2 * 3 + 2]
        tmp2 += sudoku[l1 * 3 + 1][l2 * 3]
        tmp2 += sudoku[l1 * 3 + 1][l2 * 3 + 1]
        tmp2 += sudoku[l1 * 3 + 1][l2 * 3 + 2]
        tmp2 += sudoku[l1 * 3 + 2][l2 * 3]
        tmp2 += sudoku[l1 * 3 + 2][l2 * 3 + 1]
        tmp2 += sudoku[l1 * 3 + 2][l2 * 3 + 2]
        print(tmp2)
        if tmp2 == 45:
            cnt3 = 0
        else:
            cnt3 = 1

if cnt1 == 1 or cnt2 == 1 or cnt3 == 1:
    print('NO')
else:
    print('YES')