#!/usr/bin/python3
'''
LESSON MODEL
'''
import models
from models.base_model import BaseModel


class Lesson(BaseModel):
    ''' Lesson class '''

    lessonId = '' # reference basemodel or genereate new id
    courseId = '' # reference course table
    title = ''
    content = ''
