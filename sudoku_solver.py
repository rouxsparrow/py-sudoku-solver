# import logging

# # Logging config
# logging.basicConfig(
#     filename="app.log",
#     filemode="w",
#     format="%(name)s - %(levelname)s - %(message)s",
#     level=logging.DEBUG,
# )

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-  -  -  -  -  -  -  -  - -")
        # print(board[i])
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end=" ")
            print(bo[i][j], end=" ")
            if j == len(bo[0]) - 1:
                print("\n")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, collumn
    return None


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # check collumn
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # check box
    box_i = pos[0] // 3  # box row
    box_j = pos[1] // 3  # box collumn

    for i in range(box_i * 3, box_i * 3 + 3):
        for j in range(box_j * 3, box_j * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(bo):
    # print_board(bo)
    # print("xxxxxxxxxxxxxxxxxxxxx")
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
        for i in range(1, 10):
            if valid(bo, i, (row, col)):
                bo[row][col] = i
                if solve(bo):
                    return True
                bo[row][col] = 0
    return False


# solve(board)
print_board(board)
