#!/usr/bin/python
'''
ENROLLMENT MODEL
'''
import models
from models.user import User, Base


class Enrollment(User):
    ''' Enrollment class '''

    enrollmentId = '' # primary key
    userId = '' # reference user table
    courseId = '' # reference course table
    enrollment_date = ''

    def __init__(self):
        super().__init__()
