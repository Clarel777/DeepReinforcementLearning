from game import Game
from funcs import playMatchesBetweenVersions
import loggers as lg

run_version = 1

#use -1 for human player
player1_version = -1
player2_version = 25

#how many rounds
episodes = 2

env = Game()
playMatchesBetweenVersions(env, run_version, player1_version, player2_version, episodes, lg.logger_play_game, 0)