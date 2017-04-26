"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def mc_trial(board, player):
    """
    Function to take in board and play games with random moves.
    """
    current_player = player
    winner = None

    while winner == None:
        empty_spaces = board.get_empty_squares()
        move_space = random.choice(empty_spaces)
        board.move(move_space[0], move_space[1], current_player)
        winner = board.check_win()
        provided.switch_player(current_player)

def mc_update_scores(scores, board, player):
    """
    Function to take a grid of scores and updates the scores grid.
    """
    winner = board.check_win()

    for col in range(board.get_dim()):
        for row in range(board.get_dim()):

            if winner == provided.DRAW:
                scores[row][col] += 0

            elif winner == player and board.square(row, col) == player:
                scores[row][col] += SCORE_CURRENT
            elif winner == player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] -= SCORE_OTHER
            elif winner != player and board.square(row, col) == player:
                scores[row][col] -= SCORE_CURRENT
            elif winner != player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] += SCORE_CURRENT
            elif board.square(row, col) == provided.EMPTY:
                scores[row][col] += 0

def get_best_move(board, scores):
    """
    Takes in a board and grid of scores, finds empty squares and chooses the best move.
    """
    best_score = -50000000

    # iterates through board spaces and finds the max score
    for col in range(board.get_dim()):
        for row in range(board.get_dim()):
            if scores[row][col] > best_score and board.square(row, col) == provided.EMPTY:
                best_score = scores[row][col]

    # finds any empty space that matches the best score
    empty_spaces = board.get_empty_squares()
    move_list = []
    for space in empty_spaces:
        if scores[space[0]][space[1]] ==  best_score:
            move_list.append(space)

    best_move = random.choice(move_list)
    row = best_move[0]
    col = best_move[1]

    return row, col

def mc_move(board, player, trials):
    """
    Takes in a board, which player the machine player is and runs trials via the monte carlo method
    """
    scored_board = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]

    for dummy_num in range(trials):
        clone_board = board.clone()
        mc_trial(clone_board, player)
        mc_update_scores(scored_board, clone_board, player)

    return get_best_move(board, scored_board)

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.


# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
