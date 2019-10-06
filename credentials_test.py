import unittest
from password import Credentials

class TestCredentials(unittest.TestCase):
    '''
    class to test credential class bahavior
    '''
def setUp(self):
    '''
    setUp methods to define instructions
    '''
    self.new_credentials = Credentials("Jose","Ian","Peter")
def tearDown(self):
    '''
    Method that cleans up after each test
    '''
    Credentials.credentials_list = []
def test_init(self):
    '''
    test to correct initialization
    '''
    self.assertEqual(new_credentials.account_name,"Jose")
    self.assertEqual(new_credentials.username,"Ian")
    self.assertEqual(new_credentials.password,"Peter")
def test_save_credentials(self):
    """
    Test to check whether app saves account credentials
    """
    self.new_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)



if __name__ == '__main__':
    unittest.main()