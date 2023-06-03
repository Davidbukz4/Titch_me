#!/usr/bin/python
'''
ENROLLMENT MODEL
'''
import models
from models.base_model import BaseModel


class Enrollment(BaseModel):
    ''' Enrollment class '''

    enrollmentId = '' # reference basemodel table or generate new id
    StudentId = '' # refenrence student table or generate new id
    courseId = '' # reference course table
    enrollment_date = ''
