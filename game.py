import random

board = [[' ' for _ in range(3)] for _ in range(3)]

def draw_board():
    print('---------')
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, '|', end='')
        print('\n---------')

def check_win(player: str) -> bool:
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def make_player_move(person: str) -> None:
    while True:
        try:
            move = input("Введите координаты вашего хода в формате 'строка,столбец': ")
            coordinates = move.split(',')
            row = int(coordinates[0]) - 1
            col = int(coordinates[1]) - 1
        
            if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] != ' ':
                print("Недопустимый ход. Попробуйте снова.")
            else:
                board[row][col] = person
                break
        except ValueError:
            print("Недопустимый ход. Попробуйте снова.")

def make_computer_move(computer: str) -> None:
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                available_moves.append((i, j))

    if available_moves:
        row, col = random.choice(available_moves)
        board[row][col] = computer

players = ['X', 'O']
person = random.choice(players)
computer = 'X' if person == 'O' else 'O'
current_player = random.choice(players)

while True:
    draw_board()

    if current_player == 'X':
        make_player_move(person)
    else:
        make_computer_move(computer)

    if check_win(current_player):
        draw_board()
        print("Игрок", current_player, "победил!")
        break

    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        draw_board()
        print("Ничья!")
        break

    current_player = 'O' if current_player == 'X' else 'X'
