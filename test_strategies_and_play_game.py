# This file's purpose is to test the strategies and play_game function.
# Note: make sure that "pytest" is installed in your environment.
# Note #2 : to run the tests, run the command "uv run pytest" in the terminal,
# while using the project directory.


from strategies import *
from score_table import score_dilemma_dict
from play_game_function import play_game

# Tests for tit-for-tat strategy.
def test_tit_for_tat_cooperate_when_first_move():
    assert tit_for_tat([], [], score_dilemma_dict) == "Cooperate"

def test_tit_for_tat_defect_when_opponent_defect_last_move():
    assert tit_for_tat(["Cooperate"], ["Defect"], score_dilemma_dict) == "Defect"
    assert tit_for_tat(["Defect"], ["Defect"], score_dilemma_dict) == "Defect"

def test_tit_for_tat_cooperate_when_opponent_cooperated_last_move():
    assert tit_for_tat(["Defect"], ["Cooperate"], score_dilemma_dict) == "Cooperate"
    assert tit_for_tat(["Cooperate"], ["Cooperate"], score_dilemma_dict) == "Cooperate"


# Tests for best-response strategy.
def test_best_response_cooperate_when_first_move():
    assert best_response([], [], score_dilemma_dict) == "Cooperate"

# This strategy gives always "Defect" besides the first round.
# When my last move is "Cooperate", the opponent's best response is "Defect" (5 > 3).
# When my last move is "Defect", the opponent's best response is "Defect" (1 > 0).
# The next test checks that the best_response function returns "Defect" in all cases.
def test_best_response_defect_always():
    assert best_response(["Cooperate"], ["Cooperate"], score_dilemma_dict) == "Defect"
    assert best_response(["Cooperate"], ["Defect"], score_dilemma_dict) == "Defect"
    assert best_response(["Defect"], ["Cooperate"], score_dilemma_dict) == "Defect"
    assert best_response(["Defect"], ["Defect"], score_dilemma_dict) == "Defect"


# To see that the function returns the correct values and not just "Defect" in all cases,
# I will add a new score table to check the best_response function. 
score_dilemma_mixed = {("Cooperate", "Cooperate"): (0, 0),
                       ("Cooperate", "Defect"): (5, 1),
                       ("Defect", "Cooperate"): (1, 5),
                       ("Defect", "Defect"): (3, 3)}

def test_best_response_works_with_new_scores():
    assert best_response(["Cooperate"], ["Cooperate"], score_dilemma_mixed) == "Defect"
    assert best_response(["Cooperate"], ["Defect"], score_dilemma_mixed) == "Defect"
    assert best_response(["Defect"], ["Cooperate"], score_dilemma_mixed) == "Cooperate" 
    assert best_response(["Defect"], ["Defect"], score_dilemma_mixed) == "Cooperate"


# Tests for "play_game" function.
# This test checks with all the games in "run_game.py".
def test_play_game_for_all_games_from_run_game_file():
    assert play_game(tit_for_tat, best_response, 10, score_dilemma_dict) == (11, 16)
    assert play_game(best_response, tit_for_tat, 15, score_dilemma_dict) == (21, 16)
    assert play_game(tit_for_tat, tit_for_tat, 15, score_dilemma_dict) == (45, 45)
    assert play_game(best_response, best_response, 8, score_dilemma_dict) == (10, 10)

def test_play_game_with_different_games():
    assert play_game(tit_for_tat, best_response, 1, score_dilemma_dict) == (3, 3)
    assert play_game(best_response, tit_for_tat, 5, score_dilemma_dict) == (11, 6)
    assert play_game(tit_for_tat, tit_for_tat, 10, score_dilemma_dict) == (30, 30)
    assert play_game(best_response, best_response, 5, score_dilemma_dict) == (7, 7)

def test_play_game_with_new_score_table():
    assert play_game(tit_for_tat, best_response, 10, score_dilemma_mixed) == (29, 25)
    assert play_game(best_response, tit_for_tat, 5, score_dilemma_mixed) == (12, 12)
    assert play_game(tit_for_tat, tit_for_tat, 10, score_dilemma_mixed) == (0, 0)
    assert play_game(best_response, best_response, 5, score_dilemma_mixed) == (6, 6)

