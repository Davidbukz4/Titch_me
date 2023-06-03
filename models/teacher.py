#!/usr/bin/python3
'''
TEACHER MODEL
'''
import models
from models.user import User, Base

class Teacher(User):
    ''' Teacher class '''

    teacherId = '' # primary key
    department = ''
    userId = '' # reference user table

    def __init__(self):
        super().__init__()
