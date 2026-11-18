# This file contains the strategies for the prisoner's dilemma game.
# The chosen strategies are tit-for-tat and "best response" strategy.
# The tit-for-tat strategy starts with cooperation and then mimics the opponent's previous move.
# The "best response" chooses the action that could have given the best score to the opponent in the previous round.

# Every strategy function takes two lists (my_moves, opponent_moves) and the score table (score_dilemma_dict).
# The function returns "Cooperate" or "Defect" based on the strategy's logic.

# tit-for-tat strategy
# score_dilemma_dict is received only to keep all strategies' inputs the same.
def tit_for_tat(my_moves, opponent_moves, score_dilemma_dict):
    # when there are no previous moves, cooperate.
    if (len(opponent_moves) == 0 
    or
      opponent_moves[-1] == "Cooperate"):
        return "Cooperate" 
    else: 
        return "Defect"

# Best response strategy- a more complex strategy
def best_response(my_moves, opponent_moves, score_dilemma_dict):
    # when there are no previous moves, cooperate.
    if len(opponent_moves) == 0:
        return "Cooperate" 
    # Look up the opponent's possible scores, defined by *my* last move. [1] = opponent's score from the score table.
    opp_score_if_cooperate = score_dilemma_dict[(my_moves[-1], "Cooperate")][1]
    opp_score_if_defect = score_dilemma_dict[(my_moves[-1], "Defect")][1]
    # on a tie (equal score) also cooperate.
    if opp_score_if_cooperate >= opp_score_if_defect:
        return "Cooperate" 
    else:
        return "Defect"
