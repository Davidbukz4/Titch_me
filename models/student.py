#!/usr/bin/python3
'''
STUDENT MODEL
'''
import models
from models.user import User, Base


class Student(User):
    ''' Student Class '''

    faculty = ''
    department = ''
    grade_level = ''
    studentId = ''

    def __init__(self):
        super().__init__()
