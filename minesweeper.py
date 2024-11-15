import random

def display_board(board):
    print("Board:")
    print("-" * 21)
    for row in board:
        print("|", end=" ")
        for col in row:
            if col == -1:
                print("?", end=" | ")
            else:
                print(col, end=" | ")
        print()
    print("-" * 21)

def display_solution(board):
    print("Solution:")
    print("-" * 21)
    for row in board:
        print("|", end=" ")
        for col in row:
            if col == -1:
                print("X", end=" | ")
            else:
                print(str(col), end=" | ")
        print()
    print("-" * 21)

def check_mines(board, row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < 5 and j >= 0 and j < 5:
                if board[i][j] == 1:
                    count += 1
    return count

def main():
    # board user can NOT see (solution)
    # 0: no bomb
    # 1: bomb
    board = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    # board user can see
    # -1: not clicked
    board_user = [[-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1]]

    # prompt user for number of mines
    num_mines = 26
    while num_mines > 25 or num_mines < 1:
        num_mines = int(input("Enter number of mines (max 25): "))
        if num_mines > 25:
            print("Invalid input. Max number of mines is 25. Please try again.")

    # randomly place mines on board
    for i in range(num_mines):
        row = random.randint(0, 4)
        col = random.randint(0, 4)
        if board[row][col] == 0:
            board[row][col] = 1
        else:
            i -= 1

    # display_solution(board)
    display_board(board_user)
    
    guess = 0
    while guess < 25 - num_mines:
        row = 6
        col = 6
        while row < 1 or row > 5 or col < 1 or col > 5:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            if row < 1 or row > 5 or col < 1 or col > 5:
                print("Invalid input. Please enter a number between 1 and 5.")
            elif board_user[row-1][col-1] != -1:
                print("You have already checked that cell. Please try again.")
                row = 6
                col = 6
        print()

        row -= 1
        col -= 1
        if board[row][col] == 1:
            print("Game Over!")
            display_solution(board)
            break
        else:
            board_user[row][col] = check_mines(board, row, col)
            guess += 1
            display_board(board_user)
    print("\nCongratulations! You won!")
    display_solution(board_user)
    
if __name__ == "__main__":
    main()