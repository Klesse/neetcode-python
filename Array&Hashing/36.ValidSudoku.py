# Brute Force, but sent

def isValidSudoku(board):
    dim = 9
    aux_cols_dir = []
    for i in range(dim):
        aux_row = []
        aux_col = []
        for j in range(dim):
            aux_cols_dir.append(board[j][i])
            if board[i][j].isnumeric():
                aux_row.append(int(board[i][j]))
            if board[j][i].isnumeric():
                aux_col.append(int(board[j][i]))
        if sorted(aux_row) != sorted(list(set(aux_row))) or sorted(aux_col) != sorted(list(set(aux_col))):
            return False

    index1, index2, index3 = 0, 1, 2
    grids = [[] for i in range(9)]

    counter_x = 0

    for i in range(0,80+1,9):
        if (aux_cols_dir[i].isnumeric()):
            grids[index1].append(int(aux_cols_dir[i]))
        if (aux_cols_dir[i+1].isnumeric()):
            grids[index1].append(int(aux_cols_dir[i+1]))
        if (aux_cols_dir[i+2].isnumeric()):
            grids[index1].append(int(aux_cols_dir[i+2]))
        
        if (aux_cols_dir[i+3].isnumeric()):
            grids[index2].append(int(aux_cols_dir[i+3]))
        if (aux_cols_dir[i+4].isnumeric()):
            grids[index2].append(int(aux_cols_dir[i+4]))
        if (aux_cols_dir[i+5].isnumeric()):
            grids[index2].append(int(aux_cols_dir[i+5]))
        
        if (aux_cols_dir[i+6].isnumeric()):
            grids[index3].append(int(aux_cols_dir[i+6]))
        if (aux_cols_dir[i+7].isnumeric()):
            grids[index3].append(int(aux_cols_dir[i+7]))
        if (aux_cols_dir[i+8].isnumeric()):
            grids[index3].append(int(aux_cols_dir[i+8]))
        counter_x +=1
        
        if counter_x == 3:
            index1 += 3
            index2 += 3
            index3 += 3
            counter_x = 0
        
    for i in range(9):
        print()
        if sorted(grids[i]) != sorted(list(set(grids[i]))):
            return False
    return True

