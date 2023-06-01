#!/usr/bin/python3
'''
Base Model
'''
import uuid

class Student:
    ''' Student class '''
    def __init__(self, fname, lname, dob, gender, email, phone, address,
                 faculty, department):
        ''' Defines common attributes/methods for other classes '''
        self.id = str(uuid.uuid4())
        self.firstname = fname
        self.lastname = lname
        self.dob = dob
        self.gender = gender
        self.email = email
        self.phone = phone
        self.address = address
        self.faculty = faculty
        self.department = department

    def __str__(self):
        ''' Returns a string representation of the object '''
        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
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
