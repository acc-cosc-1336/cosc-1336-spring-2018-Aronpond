#create import statement for Customer class

from src.assignments.assignment11.customer import Customer

'''
Create an AverageCustomer class that inherits from Customer class with parameters first_name, last_name, and phone_number.
Call the Customer(superclass) constructor method and pass all the parameters including self to the method.
In the constructor method create a new class attribute named discount and set value to .03.
Create a get_discount_rate method that returns the attribute discount.
'''

class AverageCustomer:
    def __init__(self, first_name, last_name, phone_number):
        Customer.__init__(self, first_name, last_name, phone_number)
        self.discount = .03
    def get_discount_rate():
        return self.discount
