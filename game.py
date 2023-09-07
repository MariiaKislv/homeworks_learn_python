import random


def draw_board(board):
    lines = ['-------------']
    for row in board:
        line = '| '
        for cell in row:
            line += cell + ' | '
        lines.append(line[:-1])
        lines.append('-------------')
    return '\n'.join(lines)


def check_win(board, player: str) -> bool:
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def read_user_move(board):
    valid_coordinates = {}
    while not valid_coordinates:
        try:
            move = input("Введите координаты вашего хода в формате 'строка,столбец': ")
            coordinates = move.split(',')
            row = int(coordinates[0]) - 1
            col = int(coordinates[1]) - 1
        
            if check_if_params_valid(board, row, col):
                valid_coordinates['row'] = row
                valid_coordinates['col'] = col
            else:
                print("Недопустимый ход. Попробуйте снова.")
        except (ValueError, IndexError):
            print("Недопустимый ход")
    return valid_coordinates


def make_player_move(board, person: str) -> None:
    coordinates = read_user_move(board)
    board[coordinates['row']][coordinates['col']] = person


def check_if_params_valid(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


def get_available_moves(board):
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                available_moves.append((i, j))
    return available_moves


def make_computer_move(board, computer: str) -> None:
    available_moves = get_available_moves(board)
    if available_moves:
        row, col = random.choice(available_moves)
        board[row][col] = computer


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    person = random.choice(players)
    computer = 'X' if person == 'O' else 'O'
    current_player = random.choice(players)

    while True:
        print(draw_board(board))

        if current_player == person:
            make_player_move(board, person)
        else:
            make_computer_move(board, computer)

        if check_win(board, current_player):
            print(draw_board(board))
            print("Игрок", current_player, "победил!")
            break

        if not get_available_moves(board):
            print(draw_board(board))
            print("Ничья!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
