import unittest
from operators import add, subtract, multiply, divide


class TestAdd(unittest.TestCase):
    def test_add_digits(self):
        """Test l'addition de deux chiffres"""
        self.assertEqual(add(2, 3), 5)

    def test_add_numbers(self):
        """Test l'addition de deux nombres"""
        self.assertEqual(add(10, 15), 25)
    
    def test_add_big_numbers(self):
        """Test l'addition de deux gros nombres"""
        self.assertEqual(add(123444, 444123), 567567)

    def test_add_zero_first(self):
        """Test l'addition de deux chiffres avec zero en premère position"""
        self.assertEqual(add(0, 5), 5)

    def test_add_zero_second(self):
        """Test l'addition de deux chiffres avec zero en seconde position"""
        self.assertEqual(add(5, 0), 5)

    def test_add_zeros(self):
        """Test l'addition de deux zeros"""
        self.assertEqual(add(0, 0), 0)

    def test_add_negative_positive_digits(self):
        """Test l'addition de deux chiffres ou le premier est négatif"""
        self.assertEqual(add(-2, 3), 1)

    def test_add_positive_negative_digits(self):
        """Test l'addition de deux chiffres ou le second est négatif"""
        self.assertEqual(add(2, -3), -1)

    def test_add_negative_positive_digits(self):
        """Test l'addition de deux chiffres négatifs"""
        self.assertEqual(add(-2, -2), -4)

    def test_add_zero_first_negative(self):
        """Test l'addition d'un zero en permière position et 
        d'un nombre négatif en seconde"""
        self.assertEqual(add(0, -2), -2)

    def test_add_zero_second_negative(self):
        """Test l'addition d'un nombre négatif en première position et
        d'un zero en seconde"""
        self.assertEqual(add(-2, 0), -2)


class TestSubstract(unittest.TestCase):
    def test_subtract_digits(self):
        """Test la soustraction de deux chiffres"""
        self.assertEqual(subtract(3, 2), 1)

    def test_subtract_numbers(self):
         """Test la soustraction de deux nombres"""
         self.assertEqual(subtract(21, 10), 11)

    def test_subtract_failure(self):
        """Test d'echec de la soustraction de deux chiffres"""
        self.assertNotEqual(subtract(5, 3), 6)

    def test_subtract_negative(self):
        """Test la soustraction de deux chiffres donnant une réponse négative"""
        self.assertEqual(subtract(2, 3), -1)

    def test_subtract_zero_first(self):
         """Test la soustraction de deux chiffres avec zero en permière position"""
         self.assertEqual(subtract(0, 1), -1)

    def test_subtract_zero_second(self):
         """Test la soustraction de deux chiffres avec zero en seconde position"""
         self.assertEqual(subtract(1, 0), 1)

    def test_subtract_zeros(self):
         """Test la soustraction de deux zeros"""
         self.assertEqual(subtract(0, 0), 0)

    def test_subtract_big_numbers(self):
        """Test la soustraction de deux gros nombres"""
        self.assertEqual(subtract(999999, 100000), 899999)

    def test_subtract_negative_first(self):
         """Test la soustraction de deux chiffres ou le permier est négatif"""
         self.assertEqual(subtract(-2, 1), -3)

    def test_subtract_negative_second(self):
         """Test la soustraction de deux chiffres ou le second est négatif"""
         self.assertEqual(subtract(2,-1), 3)

    def test_subtract_negatives(self):
         """Test la soustraction de deux chiffres négatifs"""
         self.assertEqual(subtract(-2, -3), 1)

        
class TestMultiply(unittest.TestCase):
    def test_multiply_digits(self):
        """Test la multiplication de deux chiffres"""
        self.assertEqual(multiply(2, 3), 6)
        
    def test_multiply_zero_first(self):
        """Test la multiplication de deux chiffres ou le premier est zero"""
        self.assertEqual(multiply(0, 5), 0)
        
    def test_multiply_big_numbers(self):
        """Test la multiplication de deux gros nombres"""
        self.assertEqual(multiply(1234, 5678), 7006652)

    def test_multiply_zero_second(self):
        """Test la multiplication de deux chiffres ou le second est zero"""
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_zeros(self):
        """Test la multiplication de deux zeros"""
        self.assertEqual(multiply(0, 0), 0)
    
    def test_multiply_negative(self):
        """Test la multiplication de deux chiffres ou le premier est négatif"""
        self.assertEqual(multiply(-2, 3), -6)
        
    def test_multiply_negative_numbers(self):
        """Test la multiplication de deux chiffres ou le second est négatif"""
        self.assertEqual(multiply(-2, -3), 6)
        
    def test_multiply_by_one(self):
        """Test la multiplication de deux chiffres ou le second est 1"""
        self.assertEqual(multiply(5, 1), 5)

        
class TestDivide(unittest.TestCase):
    
    def test_divide_digits(self):
        """Test la division de deux chiffres"""
        self.assertEqual(divide(6,3), 2)

    def test_divide_digits_float(self):
        """Test la division de deux chiffres ou la réponse est un float"""
        self.assertEqual(divide(5, 2), 2.5)
            
    def test_divide_by_zero(self):
        """Test la division par zero"""
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
                
    def test_divide_negative_numbers(self):
        """Test la division de deux chiffres ou le permier est négatif"""
        self.assertEqual(divide(-6, 3), -2)
            
    def test_divide_big_numbers(self):
        """Test la division de deux gros nombres"""
        self.assertEqual(divide(1000000, 1000), 1000)
            
    def test_divide_two_negative_numbers(self):
        """Test la division de deux chiffres négatifs"""
        self.assertEqual(divide(-6, -3), 2)
            
    def test_divide_by_one(self):
         """Test la division par 1"""
        self.assertEqual(divide(5, 1), 5)
            
    def test_divide_zero_by_number(self):
        """Test la division ou la dividende est 0"""
        self.assertEqual(divide(0, 5), 0)

    def test_divide_large_amount_digits_float(self):
        """Test la division ou la réponse contient plus de décimales qu'on ne peut afficher"""
        self.assertAlmostEqual(divide(10, 3), 3.3333333333333333)