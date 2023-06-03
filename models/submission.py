#!/usr/bin/python3
'''
SUBMISSION MODEL
'''
import models
from models.base_model import BaseModel


class Submission(BaseModel):
    ''' Submission class '''

    submissionId = '' # reference basemodel or generate new id
    assignmentId = '' # reference assignment table
    StudentId = '' # reference student table
    submission_date = ''
    grade = ''
