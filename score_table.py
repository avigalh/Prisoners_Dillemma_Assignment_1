# This file contains the scores for the prisoner's dilemma game.

# The scores are represented as a dictionary where the keys represent the actions of the two players 
# and the values represent the score for each player. 
# In each key and value, the first item is player 1's and second is player 2's.                        
score_dilemma_dict = {("Cooperate", "Cooperate"): (3, 3),
                      ("Cooperate", "Defect"): (0, 5),
                      ("Defect", "Cooperate"): (5, 0),
                      ("Defect", "Defect"): (1, 1)}
print(score_dilemma_dict)
