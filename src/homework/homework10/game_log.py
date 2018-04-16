#write import statement for ScoreEntry

from score_entry import ScoreEntry

#create a class named GameLog with a parameterless constructor-create an empty list of score_entries class attribute in
# constructor

class GameLog(self):

    def __init__(self):
        self.score_entries = []
        
#Create a class method add_score_entry with a score_entry parameter, in the method code append the score_entry parameter
#to the score_entries class attribute

    def add_score_entry(self, score_entry):
        self.score_entries.append(score_entry)

#Create a display_log method with no parameters-in this method iterate through display_log and display each
#score entry to screen

    def display_log(self):
        for i in score_entries:
            print(i.score_entry_id, i.die1_value, i.die2_value)
            
