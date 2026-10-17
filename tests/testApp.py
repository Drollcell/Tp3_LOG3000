import unittest
from app import calculate, index

class TestCalculate(unittest.TestCase):
    def test_calculate_add_digits(self):
        """Test l'addition de deux chiffres"""
        self.assertEqual(calculate("2+3"), float(5))

    def test_calculate_add_numbers(self):
        """Test l'addition de deux nombres"""
        self.assertEqual(calculate("10+15"), float(25))
    
    def test_calculate_add_big_numbers(self):
        """Test l'addition de deux gros nombres"""
        self.assertEqual(calculate("123444+444123"), float(567567))

    def test_calculate_add_zero_first(self):
        """Test l'addition de deux chiffres avec zero en premère position"""
        self.assertEqual(calculate("0+5"), float(5))

    def test_calculate_add_zero_second(self):
        """Test l'addition de deux chiffres avec zero en seconde position"""
        self.assertEqual(calculate("5+0"), float(5))

    def test_calculate_add_zeros(self):
        """Test l'addition de deux zeros"""
        self.assertEqual(calculate("0+0"), float(0))

    def test_calculate_add_negative_positive_digits(self):
        """Test l'addition de deux chiffres ou le premier est négatif"""
        self.assertEqual(calculate("-2+3"), float(1))

    def test_calculate_add_positive_negative_digits(self):
        """Test l'addition de deux chiffres ou le second est négatif"""
        self.assertEqual(calculate("2+-3"), float(-1))

    def test_calculate_add_negative_positive_digits(self):
        """Test l'addition de deux chiffres négatifs"""
        self.assertEqual(calculate("-2+-2"), float(-4))

    def test_calculate_add_zero_first_negative(self):
        """Test l'addition d'un zero en permière position et 
        d'un nombre négatif en seconde"""
        self.assertEqual(calculate("0+-2"), float(-2))

    def test_calculate_add_zero_second_negative(self):
        """Test l'addition d'un nombre négatif en première position et
        d'un zero en seconde"""
        self.assertEqual(calculate("-2+0"), float(-2))

    def test_calculate_subtract_digits(self):
        """Test la soustraction de deux chiffres"""
        self.assertEqual(calculate("3-2"), float(1))

    def test_calculate_subtract_numbers(self):
            """Test la soustraction de deux nombres"""
            self.assertEqual(calculate("21-10"), float(11))

    def test_calculate_subtract_failure(self):
        """Test d'echec de la soustraction de deux chiffres"""
        self.assertNotEqual(calculate("5-3"), float(6))

    def test_calculate_subtract_negative(self):
        """Test la soustraction de deux chiffres donnant une réponse négative"""
        self.assertEqual(calculate("2-3"), float(-1))

    def test_calculate_subtract_zero_first(self):
            """Test la soustraction de deux chiffres avec zero en permière position"""
            self.assertEqual(calculate("0-1"), float(-1))

    def test_calculate_subtract_zero_second(self):
        """Test la soustraction de deux chiffres avec zero en seconde position"""
        self.assertEqual(calculate("1-0"), float(1))

    def test_calculate_subtract_zeros(self):
        """Test la soustraction de deux zeros"""
        self.assertEqual(calculate("0-0"), float(0))

    def test_calculate_subtract_big_numbers(self):
        """Test la soustraction de deux gros nombres"""
        self.assertEqual(calculate("999999-100000"), float(899999))

    def test_calculate_subtract_negative_first(self):
        """Test la soustraction de deux chiffres ou le permier est négatif"""
        self.assertEqual(calculate("-2-1"), float(-3))

    def test_calculate_subtract_negative_second(self):
        """Test la soustraction de deux chiffres ou le second est négatif"""
        self.assertEqual(calculate("2-1"), float(3))

    def test_calculate_subtract_negatives(self):
        """Test la soustraction de deux chiffres négatifs"""
        self.assertEqual(calculate("-2--3"), float(1))
    
    def test_calculate_multiply_digits(self):
        """Test la multiplication de deux chiffres"""
        self.assertEqual(calculate("2*3"), float(6))
            
    def test_calculate_multiply_zero_first(self):
        """Test la multiplication de deux chiffres ou le premier est zero"""
        self.assertEqual(calculate("2*0")), float(0)
        
    def test_calculate_multiply_big_numbers(self):
        """Test la multiplication de deux gros nombres"""
        self.assertEqual(calculate("1234*5678"), float(7006652))

    def test_calculate_multiply_zero_second(self):
        """Test la multiplication de deux chiffres ou le second est zero"""
        self.assertEqual(calculate("5*0"), float(0))

    def test_calculate_multiply_zeros(self):
        """Test la multiplication de deux zeros"""
        self.assertEqual(calculate("0*0"), float(0))
    
    def test_calculate_multiply_negative(self):
        """Test la multiplication de deux chiffres ou le premier est négatif"""
        self.assertEqual(calculate("-2*3"), float(-6))
        
    def test_calculate_multiply_negative_numbers(self):
        """Test la multiplication de deux chiffres ou le second est négatif"""
        self.assertEqual(calculate("-2*-3"), float(6))
        
    def test_calculate_multiply_by_one(self):
        """Test la multiplication de deux chiffres ou le second est 1"""
        self.assertEqual(calculate("5*1"), float(5))
    
    def test_calculate_divide_digits(self):
        """Test la division de deux chiffres"""
        self.assertEqual(calculate("6/3"), float(2))

    def test_calculate_divide_digits_float(self):
        """Test la division de deux chiffres ou la réponse est un float"""
        self.assertEqual(calculate("5/2"), float(2.5))
            
    def test_calculate_divide_by_zero(self):
        """Test la division par zero"""
        with self.assertRaises(ZeroDivisionError):
            calculate("5/0")
                
    def test_calculate_divide_negative_numbers(self):
        """Test la division de deux chiffres ou le permier est négatif"""
        self.assertEqual(calculate("-6/3"), float(-2))
            
    def test_calculate_divide_big_numbers(self):
        """Test la division de deux gros nombres"""
        self.assertEqual(calculate("1000000/1000"), float(1000))
            
    def test_calculate_divide_two_negative_numbers(self):
        """Test la division de deux chiffres négatifs"""
        self.assertEqual(calculate("-6/-3"), float(2))
            
    def test_calculate_divide_by_one(self):
        """Test la division par 1"""
        self.assertEqual(calculate("5/1"), float(5))
            
    def test_calculate_divide_zero_by_number(self):
        """Test la division ou la dividende est 0"""
        self.assertEqual(calculate("0/5"), float(0))
        
class TestIndex(unittest.TestCase):