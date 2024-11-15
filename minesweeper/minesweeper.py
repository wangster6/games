import random

def display_board(board_user):
    print("Board:")
    print("-" * 21)
    for row in board_user:
        print("|", end=" ")
        for col in row:
            if col == -1:
                print("?", end=" | ")
            else:
                print(col, end=" | ")
        print()
    print("-" * 21)

def display_solution(board, board_user):
    print("Board:")
    print("-" * 21)
    for i in range(len(board_user)):
        print("|", end=" ")
        for j in range(len(board_user)):
            if board[i][j] == 1:
                print("X", end=" | ")
            else:
                print(str(check_mines(board, i, j)), end=" | ")
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

def reveal_empty(board, board_user, row, col, visited, count):
    visited.append((row, col))
    
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i >= 0 and i < 5 and j >= 0 and j < 5 and (i, j) not in visited:
                visited.append((i, j))
                if check_mines(board, i, j) == 0:
                    board_user[i][j] = 0
                    count += 1
                    board_user, count = reveal_empty(board, board_user, i, j, visited, count)
                else:
                    board_user[i][j] = check_mines(board, i, j)
                    count += 1
                    
    
    return board_user, count

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
        while board[row][col] != 0:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
        board[row][col] = 1
        

    # display_solution(board)
    display_board(board_user)
    
    guess = 0
    visited = []
    while guess < 25 - num_mines:
        row = 6
        col = 6
        while row < 1 or row > 5 or col < 1 or col > 5:
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
            except Exception as e:
                print("Invalid input. Make sure you are entering an integer!")
            else:
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
            display_solution(board, board_user)
            exit()
        else:
            board_user[row][col] = check_mines(board, row, col)
            count = 0
            if board_user[row][col] == 0:
                board_user, count = reveal_empty(board, board_user, row, col, visited, count)
                print("count:", count)
                guess += count
            guess += 1
            print("total guesses:", guess)
            display_board(board_user)
    print("\nCongratulations! You won!")
    display_solution(board, board_user)
    
if __name__ == "__main__":
    main()