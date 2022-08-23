# python prog01.py
'''
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''

# test all page

def add(a, b):
    return a + b

import unittest

class TestNotebook(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        #self.assertEqual(add(2, 2), 5)

# test in terminal
# python prog01.py
unittest.main()

# test in jupyter
#unittest.main(argv=[''], verbosity=2, exit=False)

#print(add(2,4))