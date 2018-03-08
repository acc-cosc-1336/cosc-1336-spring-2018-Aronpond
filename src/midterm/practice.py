def get_km_per_hour(miles, total_minutes):
    '''
    Write a program that asks user for miles ridden on a bike and the total time ridden. Display average
    speed per hour in kilometers
    CREATE A TEST CASE FOR THIS FUNCTION
    :param miles:  Miles ridden on a bike
    :param total_minutes: Total minutes elapsed
    :return: Average speed per hour to hundredths place
    '''
    hours = total_minutes / 60
    return round(miles / hours * 1.6 , 2)
'''
Create a function get_shipping_charge with one parameter named weight 
that returns rate per pound according to this table.
CREATE A TEST CASE FOR THIS FUNCTION

Weight                      Rate per Pound
0 to 2                      1.25
Over 2 but less than 6      2.75
Over 6 but less than 10     3.75
Over 10                     4.50

'''
def get_shipping_charge(weight):
    if weight >= 0 and weight <= 2:
        rate = 1.25
    elif weight > 2 and weight <=  6:
        rate = 2.75
    elif weight > 6 and weight < 10:
        rate = 3.75
    elif weight >= 10:
        rate = 4.50
    return rate
        

'''
Create a function get_total_of_numbers_squared with a parameter named num
tha returns the total sum of the numbers squared.
CREATE A TEST CASE FOR THIS FUNCTION 

Sample Data
param num value 5
0
1
4
9
16

Returns 30
'''
def get_total_of_numbers_squared(num):
    i = 0
    t = 0
    while i < num:
        t += i ** 2
        i += 1
    return t

'''
Create a function get_quiz_list that returns a list of students
that have more than six quiz scores.
CREATE A TEST CASE FOR THIS FUNCTION.
Sample Data:
[
['joe', 10, 15, 20, 30, 40]
['bill', 23, 16, 19, 22]
['sue', 8 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17]
['grace', 12, 28, 21, 45, 26, 10, 11]
['john', 14, 32, 25, 16, 89]
]

Return Value:
['Sue','grace']
get_quiz_list([
['joe', 10, 15, 20, 30, 40]
['bill', 23, 16, 19, 22]
['sue', 8, 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17]
['grace', 12, 28, 21, 45, 26, 10, 11]
['john', 14, 32, 25, 16, 89]
])
'''
def get_quiz_list(list1):
   rl = []
   for sub in list1:
       if len(sub) > 7:
          rl.append(sub[0])
   return rl
def get_quiz_list_file():
    file = open('quiz.dat', 'r')
    return_list = []

    for line in file:
        list1 = line.split()
        if len(list1) > 7:
            return_list.append(list1[0])

    file.close()

    return  return_list

