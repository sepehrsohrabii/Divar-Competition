def printDiagonalSums():
    Rows = int(input())
    Columns = Rows
    n = Rows
    mat = []
    # taking RowsxColumns matrix from the user
    for i in range(Rows):
        # taking input for the row from the user
        single_row = list(map(int, input().split()))
        # appending the 'single_row' to the 'example_matrix'
        mat.append(single_row)
        # printing the matrix given by user
    result = 0
    result_list = []
    for i in range(0, n):
        for j in range(0, n):

            if (i == j):
                result_list.append(mat[i][j])

            if ((i + j) == (n - 1)):
                result_list.append(mat[i][j])

    for item in result_list:
        if (item-1) % 3 == 0:
            result += item


    print(result)
printDiagonalSums()