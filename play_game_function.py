# This file contains the function to play the prisoner's dilemma game.
# The function takes in two strategies, the number of rounds to play, and the game (score table) as inputs. 

def play_game(strategy1, strategy2, rounds, game):

    player1_moves = [] # Two empty lists, the history of each player’s moves.
    player2_moves = []
    total_score1 = 0  # Each player’s running score, starting at 0.
    total_score2 = 0

    for i in range(rounds): 
        move1 = strategy1(player1_moves, player2_moves, game) # Returns the move of each player 
        move2 = strategy2(player2_moves, player1_moves, game) # based on their strategy.
        score1, score2 = game[(move1, move2)] # Returns the scores based on players moves.
        total_score1 += score1 # Each score added to the total score of each player.
        total_score2 += score2
        player1_moves.append(move1) # Saves the move of each player.
        player2_moves.append(move2)

    return total_score1, total_score2
