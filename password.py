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