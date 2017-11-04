from judge import JudgeSystem
from randomai import RandomPlayer

NUMOFGAMES = 500;
test = JudgeSystem(RandomPlayer, RandomPlayer)
test.run_games(NUMOFGAMES)
msg = 'Draw: {}, Black: {}, White: {}'.format(*test.get_results())
print(msg)
