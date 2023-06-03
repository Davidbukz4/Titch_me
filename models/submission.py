#!/usr/bin/python3
'''
SUBMISSION MODEL
'''
import models
from models.user import User, Base


class Submission(User):
    ''' Submission class '''

    submissionId = '' # primary key
    assignmentId = '' # reference assignment table
    userId = '' # reference user table
    submission_date = ''
    grade = ''

    def __init__(self):
        super().__init__()
