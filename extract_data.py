import chess.pgn
import chess
import chess.engine
import random
import numpy as np


squares_index = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7
}
def square_to_index(square):
    letter = chess.square_name(square)
    return 8 - int(letter[1]), squares_index[letter[0]]

def split_dims2(board): 
    board3d = np.zeros((12, 8, 8), dtype = np.int8) # 12 pieces of 8 rows and 8 columns,
    #12 for pieces on board, +2 for all squares covered by black piece and white pieces, +1 for turn
    for piece in chess.PIECE_TYPES:
        for square in board.pieces(piece, chess.WHITE):
            idx = np.unravel_index(square, (8, 8))
            board3d[piece - 1][7 - idx[0]][idx[1]] = 1

        for square in board.pieces(piece, chess.BLACK):
            idx = np.unravel_index(square, (8, 8))
            board3d[piece + 5][7 - idx[0]][idx[1]] = 1
            
    return board3d

def split_dims1(board):
    board3d = np.zeros((14, 8, 8), dtype = np.int8) # 12 pieces of 8 rows and 8 columns,
    #12 for pieces on board, +2 for all squares covered by black piece and white pieces, +1 for turn
    for piece in chess.PIECE_TYPES:
        for square in board.pieces(piece, chess.WHITE):
            idx = np.unravel_index(square, (8, 8))
            board3d[piece - 1][7 - idx[0]][idx[1]] = 1

        for square in board.pieces(piece, chess.BLACK):
            idx = np.unravel_index(square, (8, 8))
            board3d[piece + 5][7 - idx[0]][idx[1]] = 1

    real_turn = board.turn
    board.turn = chess.WHITE
    for move in board.legal_moves:
        i, j = square_to_index(move.to_square)
        board3d[12][i][j] = 1
    board.turn = chess.BLACK
    for move in board.legal_moves:
        i, j = square_to_index(move.to_square)
        board3d[13][i][j] = 1
    board.turn = real_turn
            
    return board3d

def encode_move(move):
    b = np.zeros((8, 8), dtype = np.int8)
    # source = move[:2]
    dest = move[-2:]
    # col_s = squares_index[source[0]]
    # row_s = 8 - int(source[1])
    col_d = squares_index[dest[0]]
    row_d = 8 - int(dest[1])
    # b[row_s][col_s] = 1
    b[row_d][col_d] = 1
    return b

# Path to your PGN file
pgn_file_path = "fishybear2.pgn"

# Open the PGN file
count = 0
with open(pgn_file_path) as pgn_file:
    w_positions = []
    w_next_pos = []
    b_positions = []
    b_next_pos = []
    while count != 4800:
        # Parse the next game
        game = chess.pgn.read_game(pgn_file)
        if game is None:
            break
        if "fishybear2" == game.headers["Black"]:
            #we only want black/even indices
            turn = 0
            board = game.board()
            append = False
            num_moves = sum(1 for _ in game.mainline_moves())
            if num_moves >= 22:
                for move in game.mainline_moves():
                    turn += 1
                    if turn % 2 == 0:
                        x1 = split_dims1(board)
                        #x2 = np.full((1, 8, 8), -1)
                        #x3 = np.concatenate((x1, x2), axis=0)
                        b_positions.append(x1)
                        append = True
                    elif turn % 2 != 0 and append == True:
                        em = chess.Move.uci(move)
                        e = encode_move(em)
                        b_next_pos.append(e)
                        append = False
                    if turn >= 20 and append == False:
                        break 
                    board.push(move)
                assert len(b_next_pos) == len(b_positions)

        else:
            #predicting for white
            turn = 0
            board = game.board()
            append = False
            num_moves = sum(1 for _ in game.mainline_moves())
            if num_moves >= 22:
                for move in game.mainline_moves():
                    turn += 1
                    if turn % 2 != 0:
                        x1 = split_dims1(board)
                        #x2 = np.full((1, 8, 8), 1)
                        #x3 = np.concatenate((x1, x2), axis=0)
                        w_positions.append(x1)
                        append = True
                    elif turn % 2 == 0 and append == True:
                        em = chess.Move.uci(move)
                        e = encode_move(em)
                        w_next_pos.append(e)
                        append = False
                    if turn >= 20 and append == False:
                        break 
                    board.push(move)
                assert len(w_next_pos) == len(w_positions)
        # Process the game
        count+=1
    np.savez("fishybear2_white.npz", w_positions, w_next_pos)
    np.savez("fishybear2_black.npz", w_positions, w_next_pos)

