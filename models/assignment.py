#!/usr/bin/python3
'''
ASSIGNMENT MODEL
'''
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship


class Assignment(BaseModel, Base):
    ''' Assignment class '''

    __tablename__ = 'assignments'
    assignmentId = Column(String(60), primary_key=True)
    lessonId = '' # reference lesson table
    title = Column(String(256))
    description = Column(String(256))
    due_date = Column(Date)

    submissions = relationship('Submission', )
