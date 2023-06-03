#!/usr/bin/python3
'''
COURSE MODEL
'''
import models
from models.user import User, Base


class Course(User):
    ''' Course class '''

    courseId = '' # primary key
    title = ''
    description = ''
    teacherID = '' # reference teacher table
    enrollmentId = '' # reference enrollment table

    def __init__(self):
        super().__init__()
