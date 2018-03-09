#write import statement for reverse string function
from src.midterm.exam import reverse_string

'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
def main():
    keep = 'y'
    while keep == 'y':
        
        string = (input('type a string to be reversed'))
        print(reverse_string(string))
        keep = input('press y to keep going')

main()
