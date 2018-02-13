#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from homework4 import valid_letter_grade, get_credit_points, get_grade_points, get_grade_point_average
#import sample_function# from homework4.py
#import valid_letter_grade
#import get_credit_points
#import get_grade_points
#import get_grade_point_average

'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Vaidate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

#WRITE YOUR CODE IN THE MAIN FUNCTION BELOW
def main():
    n = input(print('Enter the number of students:'))
    g = input(print('Enter the number of grades: '))            
#for n in range(input(print('Enter the number of students? '))):
#for g in range(input(print('Enter the number of grades? '))):
    letter_grade = valid_letter_grade(input(print('What is the letter grade for student?')))
    if valid_letter_grade(letter_grade) == false:
        print('Please enter a valid letter grade')
    credit_hours = input(print('How many credit hours? '))
    credit_points = get_credit_points(letter_grade)
    grade_points = get_grade_points(credit_hours, credit_points)
                
                
#CALL THE MAIN FUNCTION
main()
