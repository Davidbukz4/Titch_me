#!/usr/bin/python3
'''
TEACHER MODEL
'''
import models
from models.base_model import BaseModel

class Teacher(BaseModel):
    ''' Teacher class '''

    teacherId = '' # reference user table
    department = ''
