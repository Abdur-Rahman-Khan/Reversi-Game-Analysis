import mover
import writer
BOARD_SIZE =2
BLACK = "B"
WHITE = "W"
PLAYERS = {BLACK: "Black", WHITE: "White"}


def create_board():
    board = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    X=(BOARD_SIZE-1)//2
    Y=1+((BOARD_SIZE-1)//2)
    board[X][Y] = BLACK
    board[Y][Y] = WHITE
    board[X][X] = WHITE
    board[Y][X] = BLACK
    return board

def print_board(board):
    print("  " + " ".join(  str(i+1) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(str(chr(ord("a") + i)) + " " + " ".join(cell or "-" for cell in row))

def is_valid_move(board, x, y, player):
    if board[x][y] is not None:
        return False
    other_player = BLACK if player == WHITE else WHITE
    directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    # directions = ((-1,0),(0,-1),(0,1),(1,0))
    for dx, dy in directions:
        x_, y_ = x + dx, y + dy
        if not (0 <= x_ < BOARD_SIZE and 0 <= y_ < BOARD_SIZE):
            continue
        if board[x_][y_] != other_player:
            continue
        x_, y_ = x_ + dx, y_ + dy
        while 0 <= x_ < BOARD_SIZE and 0 <= y_ < BOARD_SIZE and board[x_][y_] == other_player:
            x_, y_ = x_ + dx, y_ + dy
        if 0 <= x_ < BOARD_SIZE and 0 <= y_ < BOARD_SIZE and board[x_][y_] == player:
            return True
    return False

def make_move(board, x, y, player):
    board[x][y] = player
    other_player = BLACK if player == WHITE else WHITE
    directions = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    # directions = ((-1,0),(0,-1),(0,1),(1,0))
    flipped = []
    for dx, dy in directions:
        x_, y_ = x + dx, y + dy
        if not (0 <= x_ < BOARD_SIZE and 0 <= y_ < BOARD_SIZE):
            continue
        if board[x_][y_] != other_player:
            continue
        # x_, y_ = x_ + dx, y_ + dy
        temp_flipped = []
        while 0 <= x_ < BOARD_SIZE and 0 <= y_ < BOARD_SIZE and board[x_][y_] == other_player:
            temp_flipped.append((x_, y_))
            x_, y_ = x_ + dx, y_ + dy
        if 0 <= x_ < BOARD_SIZE and 0 <= y_ < BOARD_SIZE and board[x_][y_] == player:
            flipped.extend(temp_flipped)
    # print(flipped)
    for x_, y_ in flipped:
        board[x_][y_] = player
    return board

def get_valid_moves(board, player):
    valid_moves = []
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if is_valid_move(board, x, y, player):
                valid_moves.append((x, y))
    # print(valid_moves)
    return valid_moves

def get_score(board):
    black_score = 0
    white_score = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x][y] == BLACK:
                black_score += 1
            elif board[x][y] == WHITE:
                white_score += 1
    return {BLACK: black_score, WHITE: white_score}

def game_over(board
):
    return not any(is_valid_move(board, x, y, player) for player in (BLACK, WHITE) for x in range(BOARD_SIZE) for y in range(BOARD_SIZE))

def play_game(BOARD_SIZE_PASSED=8,file_name="temp",printBoard=False,writeToFile=False):
    global BOARD_SIZE
    BOARD_SIZE=BOARD_SIZE_PASSED
    board = create_board()
    current_player = BLACK
    OverAllContent=""
    # print_board(board)
    while not game_over(board):
        valid_moves = get_valid_moves(board, current_player)
        if valid_moves:
            # print(f"{PLAYERS[current_player]}'s turn")
            # x, y = input("Enter your move (e.g. b3): ").lower().strip()
            x,y=mover.get_move(board,current_player)
            x, y = ord(x) - ord("a"), int(y) - 1
            # x,y =y,x
            # print(x,y)
            if (x, y) in valid_moves:
                prev_score = get_score(board)
                make_move(board, x, y, current_player)
                # print_board(board)
                score = get_score(board)
                #player,player_gained_score,player_score,opponent_score
                content="{} {} {} {}\n".format(current_player,score[current_player]-prev_score[current_player],score[current_player],score[get_opponent(current_player)])
                # content=[current_player,score[current_player],score[current_player]-score[get_opponent(current_player)],score[current_player],score[get_opponent(current_player)]]
                OverAllContent+=content
                # writer.write_file(file_name,content)
                # print(f"{PLAYERS[BLACK]}: {score[BLACK]}, {PLAYERS[WHITE]}: {score[WHITE]}")
                current_player = BLACK if current_player == WHITE else WHITE
            else:
                # print("Invalid move")
                continue
        else:
            # print(f"No valid moves for {PLAYERS[current_player]}")
            current_player = BLACK if current_player == WHITE else WHITE
        score = get_score(board)
    if printBoard:
        print_board(board)
    # print(score[WHITE]-score[BLACK])
    # if score[WHITE]-score[BLACK]>32:
    #     print_board(board)
    if writeToFile:
        writer.write_file(file_name,OverAllContent)
    if score[BLACK] > score[WHITE]:
        # print(f"{PLAYERS[BLACK]} wins")
        # print(score[BLACK],score[WHITE],score[BLACK]-score[WHITE])
        # print_board(board)
        # print("\n\n")
        return BLACK
    elif score[WHITE] > score[BLACK]:
        # print(f"{PLAYERS[WHITE]} wins")
        return WHITE
    else:
        # print("Draw")
        return "D"


def get_opponent(player):
    if player == BLACK:
        return WHITE
    else:
        return BLACK