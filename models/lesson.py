#!/usr/bin/python3
'''
LESSON MODEL
'''
import models
from models.user import User, Base


class Lesson(User):
    ''' Lesson class '''

    lessonId = '' # primary key
    courseId = '' # reference course table
    title = ''
    content = ''

    def __init__(self):
        super().__init__()
