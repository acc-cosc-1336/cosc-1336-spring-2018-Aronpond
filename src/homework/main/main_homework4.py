import homework4 from cosc-1336-spring-2018-Aronpond/src/homework
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
    n = int(input(print('Enter the number of students:')))
    for count in range (0,n):
        g = input(print('Enter the number of grades: '))
        h = input(print('Enter how many credit hours is this class? '))
        letter_grade = homework4.valid_letter_grade(input(print('What is the letter grade for student?')))
        if letter_grade == False:
            letter_grade = homework4.valid_letter_grade(input(print('please enter a valid letter grade')))
        credit_points = homework4.get_credit_points(letter_grade)
        print('credit points are', credit_points)
        grade_points = homework4.get_grade_points(h,credit_points)
        s = grade_points + h
        gpa = homework4.get_grade_point_average(h,grade_points)
        print('sum of grade points and credit hours are', s)
        print('student', count + 1, 'GPA is ',gpa)
main()


