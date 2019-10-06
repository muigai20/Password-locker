import unittest
from password import User

class TestUser(unittest.TestCase):
    '''
    class to test the behaviour of the test class
    '''

    def setUp(self):
        '''
        setUp method defines instruction
        '''
        self.new_user = User("Joseph","Kamau","Muigai")
