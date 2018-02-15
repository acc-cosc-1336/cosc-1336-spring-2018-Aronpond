import unittest
a = 4
A = 4
b = 3
B = 3
C = 2
c = 2
d = 1
D = 1
f = 0
F = 0
#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average

from src.homework.homework4 import sample_function
from src.homework.homework4 import valid_letter_grade
from src.homework.homework4 import get_credit_points
from src.homework.homework4 import get_grade_points
from src.homework.homework4 import get_grade_point_average
class TestHomework2(unittest.TestCase):

    def test_example(self):
        '''
        This is just an example.
        DON'T CHANGE THIS FUNCTION
        '''
        #assert that 1 equals the return value of the sample_function(1) with argument 1
        self.assertEqual(1, sample_function(1));

    #WRITE 5 TESTS FOR get_credit_points with the letter A, B, C, D, and F as arguments

    def test_GCP(self):
        self.assertEqual(4, get_credit_points('A'));
        self.assertEqual(3, get_credit_points('B'));
        self.assertEqual(2, get_credit_points('C'));
        self.assertEqual(1, get_credit_points('D'));
        self.assertEqual(0, get_credit_points('F'));

    #WRITE 5 TESTS FOR get_credit_points with the letter a, b, c, d, and f as arguments

    def test_gcp(self):
        self.assertEqual(4, get_credit_points('a'));
        self.assertEqual(3, get_credit_points('b'));
        self.assertEqual(2, get_credit_points('c'));
        self.assertEqual(1, get_credit_points('d'));
        self.assertEqual(0, get_credit_points('f'));
        
    #WRITE A TEST FOR valid_letter_grade with letter B as argument

    def test_vlg_w_B(self):
        self.assertEqual(3, valid_letter_grade('B'));

    #WRITE A TEST FOR valid_letter_grade with letter Z as argument

    def test_vlg_w_Z(self):
        self.assertEqual(False, valid_letter_grade('Z'));

    #WRITE A TEST FOR get_grade_points with arguments 3 and 4

    def test_ggp(self):
        self.assertEqual(12, get_grade_points(3,4));

    #WRITE A TEST FOR get_grade_point_average with arguments 9.0 and 36.0

    def test_gpa(self):
        self.assertEqual('4.00', get_grade_point_average(9.0,36.0))
