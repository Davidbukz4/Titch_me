#!/usr/bin/python3
'''
ASSIGNMENT MODEL
'''
from models.user import User, Base
import models


class Assignment(User):
    ''' Assignment class '''

    assignmentId = '' # primary key
    lessonId = '' # reference lesson table
    title = ''
    description = ''
    due_date = ''

    def __init__(self):
        super().__init__()
