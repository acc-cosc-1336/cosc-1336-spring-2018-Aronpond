A = 4
b = 3
B = 3
c = 2
C = 2
d = 1
D = 1

F = 0
f= 0
def sample_function(value):
    '''Return value given'''
    return value

def valid_letter_grade(letter_grade):
    '''
    Given a letter grade determine if it's in the range A, B, C, D, F, a, b, c, d, f
    :param letter_grade: A letter grade
    :return: True boolean expression if letter grade in range False otherwise.
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''
    a = 4
    A = 4
    b = 3
    B = 3
    c = 2
    C = 2
    d = 1
    D = 1
    F = 0
    f= 0
   #, or 'A',or 'b', or 'B', or 'c', or 'C', or 'd', or 'D', or 'f', or 'F')
    if (letter_grade)==('a'):
        return True
    if (letter_grade)==('A'):
        return True
    if (letter_grade)==('b'):
        return True
    if (letter_grade)==('B'):
        return True
    if (letter_grade)==('c'):
        return True
    if (letter_grade)==('C'):
        return True
    if (letter_grade)==('d'):
        return True
    if (letter_grade)==('D'):
        return True
    if (letter_grade)==('f'):
        return True
    if (letter_grade)==('F'):
        return True
    else:
        return False

    #elif (letter_grade) != ['a','A','b','B','C','c','d','D','f','F']:
     #   return False
    #elif (letter_grade) != ['a','A','b','B','C','c','d','D','f','F']:
    #    return False
def get_credit_points(letter_grade):
    '''
    Given a letter grade return the credit points associated with that grade.
    IN BLACKBOARD: SEE TABLE IN HOMEWORK 4 ASSIGNMENT.
    :param letter_grade: One letter grade
    :return: a whole number representing the credit points
    WRITE YOUR CODE AFTER THE THREE QUOTES BELOW
    '''
#    return letter_grade
    a = 4
    A = 4
    b = 3
    B = 3
    c = 2
    C = 2
    d = 1
    D = 1
    F = 0
    f = 0

    if (letter_grade) == (a) or letter_grade == (A):
        return 4
    if (letter_grade) == (b) or letter_grade == (B):
        return 3
    if (letter_grade) == (c) or letter_grade == (C):
        return 2
    if (letter_grade) == (d) or letter_grade == (D):
        return 1
    if (letter_grade) == (f) or letter_grade == (F):
        return 0
    
    
#    if letter_grade == 'b' or letter_grade == 'B':
#        credit_points == 3
#        return
#    if letter_grade == 'c' or letter_grade == 'C':
#        credit_points == 2
#        return
#    if letter_grade == 'd' or letter_grade == 'D':
#        credit_points == 1
#        return
#    if letter_grade == 'f' or letter_grade == 'F':
#        credit_points == 0
#        return
def get_grade_points(credit_hours, credit_points):
    '''
    Return grade points given credit hours and credit points.

    :param credit_hours: Credit hours for a class
    :param credit_points: Credit points for a class
    :return: Total grade points for a class
    '''
    grade_points = (credit_hours) * (credit_points)
    return grade_points

def get_grade_point_average(credit_hours, grade_points):
    grade_point_average = int(grade_points) / int(credit_hours)
    return format(grade_point_average, '.2f')
