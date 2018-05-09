class Customer:

    def __init__(self, name, address, phone):

        self.name = name
        self.address = address
        self.phone = phone

class Car:

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year

class ServiceQuote:

    def __init__(self, customer, car, parts_cost, labor_cost):

        self.customer = customer
        self.car = car
        self.parts_cost = parts_cost
        self.labor_cost = labor_cost

    def get_cost(self):

        return self.parts_cost + labor_cost

class MainApp:

    def main(self, customer, car):

        quote = ServiceQuote(customer, car, 10000, 5000)
