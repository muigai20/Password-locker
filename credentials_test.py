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
def test_save_multiple_credentials(self):
    """
    Test for saving multiple credentials
    """
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Heavenly","Angels","Boatross")
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),2)
def test_save_multiple_credentials(self):
    """
    Test for saving multiple credentials
    """
    self.new_credentials.save_credentials()
    test_credentials = Credentials("Heavenly","Angels","Boatross")
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),2)

def test_view_credentials(self):
    """
    Test to view an account credential
    """
    self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

def test_delete_credentials(self):
    """
    Test to delete account credentials
    """
    self.new_credentials.save_credentials()
    test_credentials = Credentials("EAsport","Striker4","makesmewonder")
    test_credentials.save_credentials()
    self.new_credentials.delete_credentials()
    self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':

    unittest.main()




