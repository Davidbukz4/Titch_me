#!/usr/bin/python3
'''
Data Model
'''
import uuid


class User:
    ''' User class '''
    firstname = ''
    lastname = ''
    date_of_birth = ''
    gender = ''
    email = ''
    password = ''
    phone = ''
    photo = ''
    def __init__(self):
        ''' Defines common attributes/methods for other classes '''
        self.userId = str(uuid.uuid4())

    def __str__(self):
        ''' Returns a string representation of the object '''
        return '[{}] ({}) {}'.format(type(self).__name__, self.userId,
                                     self.__dict__)

    def save(self):
        ''' save method '''
        # update property
        # save object

    def to_dict(self):
        ''' returns a dictionary containing all key, value of the instance '''
        # code here

    def delete(self):
        ''' delete instance from storage '''
        # code here

    def update_photo(self):
        ''' updates profile photo of user '''
        # code here

    def reset_password(self):
        ''' updates and save new password '''
        # code here

    def view_grades(self):
        ''' retrieves/returns the user grade '''
        # code here

    def submit_assignment(self):
        ''' submit an assignment for the user '''
