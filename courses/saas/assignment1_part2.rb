class WrongNumberOfPlayersError < StandardError ; end
class NoSuchStrategyError < StandardError ; end

AllowedStrategies = ["R", "P", "S"]

def rps_game_winner(game)
  raise WrongNumberOfPlayersError unless game.length == 2
  raise NoSuchStrategyError unless game[0][0] 
end