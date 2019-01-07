1# Making a board and assigning row column pair
board = {}
for i in range(1, 4):
    for j in range(1, 4):
        board.setdefault(str(i) + str(j), ' ')


# pluging values to the board and appearence
def BoardImage():
    print(board['11'] + '|' + board['12'] + '|' + board['13'])
    print('-+-+-')
    print(board['21'] + '|' + board['22'] + '|' + board['23'])
    print('-+-+-')
    print(board['31'] + '|' + board['32'] + '|' + board['33'])


BoardImage()


# input for row option
def Rowinput():
    while True:

        row = int(input("Input row for move " + str(i + 1) + " :"))
        print("")
        if (row == 1) or (row == 2) or (row == 3):
            return row

        else:
            print("Invalid row. Please renter row")
            print("")


# input for column function
def Columninput():
    while True:
        column = int(input("Input column for move " + str(i + 1) + " :"))
        print("")
        if (column == 1) or (column == 2) or (column == 3):
            return column
        else:
            print("Invalid column. Please renter column")


# defining valid move
turn = 'X'


def validmove():
    while True:
        a = Rowinput()
        b = Columninput()
        if board[str(a) + str(b)] == ' ':
            board[str(a) + str(b)] = turn
            break
        else:
            print("invalid block")
            print("")

# game logic

for i in range(0, 9):
    print("It is your turn," + turn)
    print("")
    validmove()
    # print(board)

    BoardImage()
    if (board['11'] == board['12'] == board["13"] == turn) or (
            board['21'] == board['22'] == board["23"] == turn) or (
            board['31'] == board['32'] == board["33"] == turn) or (
            board['11'] == board['21'] == board["31"] == turn) or (
            board['12'] == board['22'] == board["32"] == turn) or (
            board['13'] == board['23'] == board["33"] == turn) or (
            board['11'] == board['22'] == board["33"] == turn) or (
            board['13'] == board['22'] == board["31"] == turn):
        print(turn + " has won")
        print("")
        break
    elif i == 8:
        print("game is a tie")
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
