import unittest

class MyTest(unittest.TestCase):

    def __init__(self, testName, extraArg):
        super(MyTest, self).__init__(testName)  # calling the super class init varies for different python versions.  This works for 2.7
        self.myExtraArg = extraArg

    def test_something(self):
        print(self.myExtraArg)
    
    def test_something2(self):
        print(self.myExtraArg+'him')



# call your test
suite = unittest.TestSuite()
suite.addTest(MyTest('test_something', 'extraArg'))
suite.addTest(MyTest('test_something2', 'Himanshu'))
unittest.TextTestRunner(verbosity=2).run(suite)
