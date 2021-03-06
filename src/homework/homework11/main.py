
#write import statements for Die6 and Die8 classes
from src.homework.homework11.die6 import Die6
from src.homework.homework11.die8 import Die8
from src.homework.homework11.player import Player
from src.homework.homework11.game_log import GameLog
game_log = GameLog()

#ASSIGNMENT 12: Write statements to create Die6 and Die8 instances
die6 = Die6()
die8 = Die8()

#ASSIGNMENT12: pass the Die6 and Die8 instance object variables to the Player instantiation below as parameters after
#the game_log parameter
Player(game_log, die6, die8).roll_doubles()

game_log.display_log()

#ASSIGNMENT12: Create another GameLog instance
game_log2 = GameLog()
#ASSIGNMENT12: Write statements to create Die6 and Die8 instances
die62 = Die6()
die82 = Die8()
#ASSIGNMENT12: Create a new instance of the Player class and pass it the game log, die6, and die8 instances.
#ASSIGNMENT12: Call the player instance roll_doubles.
Player(game_log, die62, die82).roll_doubles()
#ASSIGNMENT12: Call the game log instance display_log method.
game_log.display_log()
