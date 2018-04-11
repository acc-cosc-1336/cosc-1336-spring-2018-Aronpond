from player import Player

#write import statement for GameLog class
from game_log import GameLog

#Create a game log instance
a = GameLog()

#SEnd the game_log instance to Player class as an argument
Player(a).roll_doubles()

#call the game log display method below
a.display_log()



