#!/usr/bin/python3
'''
COURSE MODEL
'''
import models
from models.base_model import BaseModel


class Course(BaseModel):
    ''' Course class '''

    courseId = '' # reference basemodel table or generate new id
    title = ''
    description = ''
    teacherID = '' # reference teacher table
    enrollmentId = '' # reference enrollment table
