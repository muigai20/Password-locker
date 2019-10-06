import string
import random

class User:
    '''
    class that defines user login details in the application
    '''
    user_list = []

    def __init__(self,first_name,last_name,password):
        '''
        fuction to initalize user field correctly
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    def save_user(self):
        '''
        function to save user login details
        '''
        User.user_list.append(self)
class Credentials:
    credentials_list = []
    '''
    class that defines credentials for differents accounts
    '''
    def __init__(self,account_name,username,password):
        '''
        function to initialize credentials field correctly
        '''
        self.account_name = account_name
        self.username = username
        self.password = password
    def save_credentials(self):
        '''
        function to save credentials 
        '''
        Credentials.credentials_list.append(self)
    @classmethod
    def find_by_name(cls,name):
        '''
        function that take the account name and returns the object
        '''
        for account in cls.credentials_list:
            if account.account_name == name:
                return account