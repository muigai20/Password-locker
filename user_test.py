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
        self.new_user = User("Joseph","Kamau","cooperative")
    
    def test_init(self):
        '''
        test to correct initialization
        '''
        self.assertEqual(self.new_user.first_name,"Joseph")
        self.assertEqual(self.new_user.last_name,"Kamau")
        self.assertEqual(self.new_user.password,"cooperative")
    def test_save_user(self):
        '''
        test to confirm whether app saves user login details
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
