# This file is the main file to run the prisoner's dilemma game.
# It imports the necessary functions and score table from other files

from score_table import score_dilemma_dict
from strategies import *
from play_game_function import play_game


# game 1 when player 1 uses tit_for_tat and player 2 uses best_response for 10 rounds
game1 = play_game(tit_for_tat, best_response, 10, score_dilemma_dict)
print("Game 1 results:", game1, "|", "Player 1 score:", game1[0], ";","Player 2 score:", game1[1])
# results game 1: (11, 16) Player 1 score: 11 Player 2 score: 16

# game 2 when player 1 uses best_response and player 2 uses tit_for_tat for 15 rounds
game2 = play_game(best_response, tit_for_tat, 15, score_dilemma_dict)
print("Game 2 results:", game2, "|", "Player 1 score:", game2[0], ";", "Player 2 score:", game2[1])
# results game 2: (21, 16) Player 1 score: 21 Player 2 score: 16

# game 3 when player 1 uses tit_for_tat and player 2 uses tit_for_tat for 15 rounds
game3 = play_game(tit_for_tat, tit_for_tat, 15, score_dilemma_dict)
print("Game 3 results:", game3, "|", "Player 1 score:", game3[0], ";", "Player 2 score:", game3[1])
# results game 3: (45, 45) Player 1 score: 45 Player 2 score: 45

# game 4 when player 1 uses best_response and player 2 uses best_response for 8 rounds
game4 = play_game(best_response, best_response, 8, score_dilemma_dict)
print("Game 4 results:", game4, "|", "Player 1 score:", game4[0], ";", "Player 2 score:", game4[1])
# results game 4: (10, 10) Player 1 score: 10 Player 2 score: 10
