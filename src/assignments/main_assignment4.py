from assignment4 import factorial
def main():#void function
    '''
    Create a loop that'll run until the user doesn't type the letter 'y'
    In the loop,
    Capture one number from the keyboard and validate for a range between 1 and 10.
    Call the factorial function.
    Save the result to a variable.
    Print the variable value.

    Ask the user if they want to continue.

    TO RUN YOUR PROGRAM GO TO IN PYTHON IDLE RUN->RUN MODULE.
    IN THE PYTHON SHELL TYPE main()

    DON'T ADD A RETURN STATEMENT TO THIS FUNCTION
    '''
    
    keep_going = 'y'
    while keep_going == 'y':
        
    #keep_going = input(print("press enter y to keep going"):
        number = int(input('number: '))
        while number < 0 or number > 10:
            print('invalid')
            number = int(input('number: '))
        result = factorial(number)
        print(result)
        keep_going = int(input('keep going?')
                       
   # x = input(print("enter a number between 1 and 10")
        #   y = factorial(x)
       # print(y)
#main()
              
