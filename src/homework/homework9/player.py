#write import statement for Die class
from src.homework.homework9.die import Die


'''
Create a Player class.

'''

class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''

        self.die1 = Die()
        self.die2 = Die()
        

    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        
        throw1 = 0
        throw2 = 7
        while throw1 != throw2:
            throw1 = self.die1.roll()
            throw2 = self.die2.roll()
            print('You rolled ', (throw1) , ' and ' , (throw2)  )
        if throw1 == throw2:
            print('Congradulations you rolled a double')


