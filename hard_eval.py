import chess
import numpy as np


piece_scores = {
    "p" : 1,
    "q" : 9,
    "k" : 200,
    "n" : 3,
    "b" : 3,
    "r" : 5,
    "P" : -1,
    "Q" : -9,
    "K" : -200,
    "N" : -3,
    "B" : -3,
    "R" : -5
}

#non symmetrical for kingside/queenside castling
WHITE_KING_GRID = np.array([
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3], 
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3], 
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2],
    [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.2, 0.2],
    [0.2, 0.3, 0.25, 0.0, 0.0, 0.1, 0.3, 0.2]
])
blk = WHITE_KING_GRID * -1
BLACK_KING_GRID = blk[::-1]

WHITE_KNIGHT_GRID = np.array([
    [-0.5, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.5], 
    [-0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4], 
    [-0.4, 0.0, 0.1, 0.2, 0.2, 0.1, 0.0, -0.4],
    [-0.4, 0.0, 0.2, 0.3, 0.3, 0.2, 0.0, -0.4],
    [-0.4, 0.0, 0.2, 0.3, 0.3, 0.2, 0.0, -0.4],
    [-0.4, 0.0, 0.1, 0.2, 0.2, 0.1, 0.0, -0.4],
    [-0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4],
    [-0.5, -0.4, -0.4, -0.4, -0.4, -0.4, -0.4, -0.5]
])
BLACK_KNIGHT_GRID = WHITE_KNIGHT_GRID * -1


WHITE_PAWN_GRID = np.array([
    [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9], 
    [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6], 
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
    [0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [-0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1]
])
blkp = WHITE_PAWN_GRID * -1
BLACK_PAWN_GRID = blkp[::-1]

WHITE_QUEEN_GRID = np.array([
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
])
BLACK_QUEEN_GRID = WHITE_QUEEN_GRID * -1

WHITE_ROOK_GRID = np.array([
    [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3], 
    [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], 
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
    [0.0, 0.1, 0.1, 0.25, 0.25, 0.2, 0.1, 0.0]
])
blkr = WHITE_ROOK_GRID * -1
BLACK_ROOK_GRID = blkr[::-1]

WHITE_BISHOP_GRID = np.array([
    [-0.4, -0.3, -0.1, -0.1, -0.1, -0.1, -0.3, -0.4],
    [-0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1],
    [-0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, -0.1],
    [-0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, -0.1],
    [-0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, -0.1],
    [-0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, -0.1],
    [-0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, -0.1],
    [-0.4, -0.3, -0.1, -0.1, -0.1, -0.1, -0.3, -0.4]
])
blkb = WHITE_BISHOP_GRID * -1
BLACK_BISHOP_GRID = blkb[::-1]

col_to_idx = {
    "a" : 0,
    "b" : 1,
    "c" : 2,
    "d" : 3,
    "e" : 4,
    "f" : 5,
    "g" : 6,
    "h" : 7
}

def Knight(board, color):
    pawns = 0
    if color == "BLACK":
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.PAWN:
                if piece.color == chess.BLACK:
                    pawns += 1
        return pawns * 0.01 * -1
    else:
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.PAWN:
                if piece.color == chess.WHITE:
                    pawns += 1
        return pawns * 0.01 
    
def Bishop(board, color):
    bishop = 0
    if color == "BLACK":
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.BISHOP:
                if piece.color == chess.BLACK:
                    bishop += 1
        if bishop >= 2:
            return -0.7
        else:
            return 0.0
    else:
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.BISHOP:
                if piece.color == chess.WHITE:
                    bishop += 1
        if bishop >= 2:
            return 0.7 
        else:
            return 0.0

def Rook(board, color):
    summ = 0.0
    if color == "BLACK":
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.PAWN:
                if piece.color == chess.BLACK:
                    summ += 0.05
    
    else:
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece and piece.piece_type == chess.PAWN:
                if piece.color == chess.WHITE:
                    summ -= 0.05 
    return summ

# def Pawn(board, color):
#     summ = 0.0
#     if color == "BLACK":
#         for square in chess.SQUARES:
#             piece = board.piece_at(square)
#             if piece and piece.piece_type == chess.PAWN:
#                 column_index = chess.square_file(square)
#                 column = chess.FILE_NAMES[column_index]
#                 print(square)
#                 for rank in chess.RANK_NAMES:
#                     sq = chess.square(chess.FILE_NAMES.index(column), int(rank))
#                     print(sq)
#                     if sq < 64:
#                         piece = board.piece_at(sq)
#                         if piece and piece.color == chess.BLACK and piece.piece_type == chess.PAWN:
#                             summ += 0.4
    
    # else:
    #     for square in chess.SQUARES:
    #         piece = board.piece_at(square)
    #         if piece and piece.piece_type == chess.PAWN:
    #             column_index = chess.square_file(square)
    #             column = chess.FILE_NAMES[column_index]
    #             for rank in chess.RANK_NAMES:
    #                 sq = chess.square(chess.FILE_NAMES.index(column), int(rank))
    #                 if sq < 64:
    #                     piece = board.piece_at(sq)
    #                     if piece and piece.color == chess.WHITE and piece.piece_type == chess.PAWN:
    #                         summ -= 0.4
    # return summ




def reward(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            sqname = chess.square_name(square)
            col = col_to_idx[sqname[0]]
            row = int(sqname[1]) - 1
            if piece.symbol().islower():
                color = "WHITE"
            else:
                color = "BLACK"
            if piece.symbol().lower() == "q":
                func = f"{color}_QUEEN_GRID[{row}][{col}]"
                score += eval(func)
            elif piece.symbol().lower() == "b":
                func = f"{color}_BISHOP_GRID[{row}][{col}]"
                score += eval(func) + Bishop(board, color)
            elif piece.symbol().lower() == "n":
                func = f"{color}_KNIGHT_GRID[{row}][{col}]"
                score += eval(func) + Knight(board, color)
            elif piece.symbol().lower() == "r":
                func = f"{color}_ROOK_GRID[{row}][{col}]"
                score += eval(func) + Rook(board, color)
            elif piece.symbol().lower() == "p":
                func = f"{color}_PAWN_GRID[{row}][{col}]"
                score += eval(func)
            else:
                func = f"{color}_KING_GRID[{row}][{col}]"
                score += eval(func)
                

    return score * -1


def raw_evaluate(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            score += piece_scores[piece.symbol()]
    return score * -1

    

def depth_evaluate(board):
    curr_eval = raw_evaluate(board)

    if board.turn == chess.WHITE: #look for all white pieces that can capture black pieces
        max_move = None
        for square in chess.scan_reversed(board.occupied_co[chess.WHITE]):  # Scan for white pieces
            piece = board.piece_at(square)
            piece_value = piece_scores[piece.symbol()]
            legal_moves = [move for move in board.legal_moves if move.from_square == square]
            for move in legal_moves:
                target_square = move.to_square
                target_piece = board.piece_at(target_square)
                if target_piece and target_piece.color == chess.BLACK:
                    target_value = piece_scores[target_piece.symbol()]
                    if abs(target_value) >= abs(piece_value):
                        board.push(move)
                        eva = raw_evaluate(board)
                        if eva > curr_eval:
                            curr_eval = eva
                            max_move = move
                        board.pop()
    else:
        min_move = None
        for square in chess.scan_reversed(board.occupied_co[chess.BLACK]):  # Scan for black pieces
            piece = board.piece_at(square)
            piece_value = piece_scores[piece.symbol()]
            legal_moves = [move for move in board.legal_moves if move.from_square == square]
            for move in legal_moves:
                target_square = move.to_square
                target_piece = board.piece_at(target_square)
                if target_piece and target_piece.color == chess.WHITE:
                    target_value = piece_scores[target_piece.symbol()]
                    if abs(target_value) >= abs(piece_value):
                        board.push(move)
                        eva = raw_evaluate(board)
                        if eva < curr_eval:
                            curr_eval = eva
                            min_move = move
                        board.pop()
    return curr_eval


def total_evaluate(board):
    return (reward(board) + depth_evaluate(board)) 

def mm_evaluate(board):
    factor = 1
    if board.turn == chess.WHITE:
        factor = -1
    return total_evaluate(board) * factor

# board = chess.Board("r1bqkb1r/ppppp1pp/2n1p3/8/2BP4/2N1BN2/PPP2PPP/R2Q1RK1 b kq - 0 1")
# print(f"Raw Evaluation: {raw_evaluate(board)}")
# print(f"Depth Evaluation: {total_evaluate(board)}")
# print(f"MM Evaluation: {mm_evaluate(board)}")