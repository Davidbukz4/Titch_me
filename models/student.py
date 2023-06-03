#!/usr/bin/python3
'''
STUDENT MODEL
'''
import models
from models.base_model import BaseModel


class Student(BaseModel):
    ''' Student Class '''

    studentId = '' # reference user table
    faculty = ''
    department = ''
    grade_level = ''
