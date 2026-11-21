# Iterated Prisoner's Dilemma

# Project description

This project is a simple Python version of the "iterated prisoner's dilemma". Two players play several rounds, and in each round both choose to either "cooperate" or "defect". Each player's score depends on both choices. The project includes a function that runs a full game between any two strategies (both players can also use the same strategy in a game), two strategy functions (tit-for-tat and best response), a script that runs example games, and tests that check everything works as expected.

# The score table

| Player 1 | Player 2 | Player 1 score | Player 2 score |
|---|---|---|---|
| Cooperate | Cooperate | 3 | 3 |
| Cooperate | Defect | 0 | 5 |
| Defect | Cooperate | 5 | 0 |
| Defect | Defect | 1 | 1 |

# The strategies

- "Tit-for-tat" cooperates in the first round, then copies the opponent's last move.
- "Best response" cooperates in the first round. After that, it plays the move that would have given the opponent the highest score in the previous round, given its own last move. 

Every strategy is a function that receives the same three inputs: `my_moves` (its own previous moves), `opponent_moves` (the opponent's previous moves) and the score table. It returns `"Cooperate"` or `"Defect"`. Because of this shared format, the `play_game` function can run any two strategies against each other, and each strategy works the same way whether it plays as player 1 or player 2.

# Repository structure

| File | Contents |
|---|---|
| `score_table.py` | The score table, stored as a dictionary (`score_dilemma_dict`) |
| `strategies.py` | The strategy functions: `tit_for_tat` and `best_response` |
| `play_game_function.py` | `play_game(strategy1, strategy2, rounds, game)`, which plays a full game and returns both players' total scores |
| `run_game.py` | Runs four example games and prints the results (the results are also written as comments in the file) |
| `test_strategies_and_play_game.py` | Tests for the strategies and for `play_game`|

# How to run

1. Install the dependencies: `uv sync`
2. Run the example games: `uv run run_game.py`
   (or open `run_game.py` in VS Code and click ▶ Run)
3. Run the tests: `uv run pytest`

# Results of the example games

| Game | Player 1 | Player 2 | Rounds | Result |
|---|---|---|---|---|
| 1 | tit-for-tat | best response | 10 | (11, 16) |
| 2 | best response | tit-for-tat | 15 | (21, 16) |
| 3 | tit-for-tat | tit-for-tat | 15 | (45, 45) |
| 4 | best response | best response | 8 | (10, 10) |

These results match Axelrod's finding: cooperation pays off overall, even for self-interested players (when both players use tit-for-tat, they get the highest scores).

# What the tests check

- each strategy's move in the first round and in later rounds
- that best response really reads the score table, using a second, made-up table where it sometimes cooperates
- `play_game` results for several matchups, with the players in both orders and with both score tables

# Reproducibility

Neither strategy uses randomness, so every run gives exactly the same results. Anyone who clones the repository and runs `run_game.py` will get the scores shown in this README.


