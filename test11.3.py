import random

def display_board(board):
    for row in board:
        print(" ".join(row))

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def player_move(board, row, col):
    if board[row - 1][col - 1] == ' ':
        board[row - 1][col - 1] = 'X'
        return True
    return False

def computer_move(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'O'
                return

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    computer = 'O'

    while True:
        display_board(board)
        row, col = map(int, input("Enter row and column (e.g., '1 2'): ").split())
        if player_move(board, row, col):
            if check_win(board, player):
                display_board(board)
                print("Congratulations! You win!")
                break
            elif is_board_full(board):
                display_board(board)
                print("It's a tie!")
                break

        computer_move(board)
        if check_win(board, computer):
            display_board(board)
            print("Computer wins!")
            break
        elif is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
