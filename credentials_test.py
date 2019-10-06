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