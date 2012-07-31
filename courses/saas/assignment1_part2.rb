class WrongNumberOfPlayersError < StandardError ; end
class NoSuchStrategyError < StandardError ; end

Strategies = ["R", "P", "S"]

def rps_game_winner(game)
	# Initialize
	first, second = game[0][1], game[1][1]
  
  # Precondition check
  raise WrongNumberOfPlayersError unless game.length == 2
  raise NoSuchStrategyError unless Strategies.include?(first) and Strategies.include?(second)

  
  if first == second
  	return game[0]
  elsif first == "R" and second == "S"
  	return game[0]
  elsif first == "S" and second == "R"
  	return game[1]
  elsif first == "S" and second == "P"
  	return game[0]
  elsif first == "P" and second == "S"
  	return game[1]
  elsif first == "P" and second == "R"
  	return game[0]
  elsif first == "R" and second == "P"
  	return game[0]
  end
  	
end

puts rps_game_winner([["Armando","P"], ["Dave","S"]]).inspect

=begin 
(b) A rock, paper, scissors tournament is encoded as a bracketed array of games - that is, each
element can be considered its own tournament.
[
[
[ ["Armando", "P"], ["Dave", "S"] ],
[ ["Richard", "R"], ["Michael", "S"] ],
],
[
[ ["Allen", "S"], ["Omer", "P"] ],
[ ["David E.", "R"], ["Richard X.", "P"] ]
]
]
Under this scenario, Dave would beat Armando (S>P), Richard would beat Michael (R>S), and
then Dave and Richard would play (Richard wins since R>S); similarly, Allen would beat Omer,
Richard X would beat David E., and Allen and Richard X. would play (Allen wins since S>P);
and finally Richard would beat Allen since R>S, that is, continue until there is only a single
winner.
● Write a method rps_tournament_winner that takes a tournament encoded as
a bracketed array and returns the winner (for the above example, it should return
[“Richard”, “R”]).
● Tournaments can be nested arbitrarily deep, i.e., it may require multiple rounds to get to
a single winner. You can assume that the initial array is well formed (that is, there are
2^n players, and each one participates in exactly one match per round).
=end

def rps_tournament_winner(tournaments)

end

puts rps_tournament_winner([
[
[ ["Armando", "P"], ["Dave", "S"] ],
[ ["Richard", "R"], ["Michael", "S"] ],
],
[
[ ["Allen", "S"], ["Omer", "P"] ],
[ ["David E.", "R"], ["Richard X.", "P"] ]
]
])