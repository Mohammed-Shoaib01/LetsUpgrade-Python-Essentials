import unittest
import prime_number
class testPrime(unittest.TestCase):
    def test(self):
        num = 7
        result = prime_number.prime(num)
        self.assertEqual(result,True)
if __name__ == "__main__":
    unittest.main()

#Commmand Prompt
#
#Input: pylint "prime_number.py"
#Output:
# -------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 2.50/10, +7.50)


#Input: Batch-7_Day-9>batch-7_day-9_Q-1.py
#Output:
#.
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK
