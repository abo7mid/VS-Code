import unittest





def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False





#This code is related to TDD (Test-Driven Development)

# This code does not work becouse some functions need to be overridden ex setUp & teadDown ..
# and this would be done through class inheritance

# test = unittest.TestCase()
# test.assertEqual(isEven(2),True)
# test.assertEqual(isEven(5),False)
# def setUp():
#     print("setup")




class IsEventTests(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(isEven(2),True)
        self.assertTrue(isEven(2))


    def testThree(self):
        self.assertEqual(isEven(5),False)
        # self.assertFalse(isEven(3))

    def testFour(self):
        self.assertGreater(isEven(2),False)
    # any task you want run before any method above is executed, put them in the setUp method
    # setUp & tearDown functions runs 3 times since there are three tests
    def setUp(self):
        # add the setUp tasks 
        print("Running setUp")

    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")



if __name__ == "__main__":
    unittest.main() #runs the tests