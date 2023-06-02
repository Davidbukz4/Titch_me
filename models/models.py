#!/usr/bin/python3
'''
Data Model
'''
import uuid


class User:
    ''' User class '''
    firstname = ''
    lastname = ''
    date_of_birth = ''
    gender = ''
    email = ''
    password = ''
    phone = ''
    photo = ''
    def __init__(self, fname, lname, dob, gender, phone, email, pwd, photo):
        ''' Defines common attributes/methods for other classes '''
        self.userId = str(uuid.uuid4())

    def __str__(self):
        ''' Returns a string representation of the object '''
        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        ''' save method '''
        # update property
        # save object

    def to_dict(self):
        ''' returns a dictionary containing all key, value of the instance '''
        # code here

    def delete(self):
        ''' delete instance from storage '''
        # code here



class Student(User):
    ''' Student Class '''
    
    faculty = ''
    department = ''
    grade_level = ''
    studentId = ''
    
    def __init__(self):
        super().__init__()

class Teacher(User):
    ''' Teacher class '''

    teacherId = '' # primary key
    department = ''
    userId = '' # reference user table

    def __init__(self):
        super().__init__()


class Course(User):
    ''' Course class '''
    
    courseId = '' # primary key
    title = ''
    description = ''
    teacherID = '' # reference teacher table
    enrollmentId = '' # reference enrollment table

    def __init__(self):
        super().__init__():


class Enrollment(User):
    ''' Enrollment class '''

    enrollmentId = '' # primary key
    userId = '' # reference user table
    courseId = '' # reference course table
    enrollment_date = ''


class Lesson(User):
    ''' Lesson class '''

    lessonId = '' # primary key
    courseId = '' # reference course table
    title = ''
    content = ''


class Assignment(User):
    ''' Assignment class '''

    assignmentId = '' # primary key
    lessonId = '' # reference lesson table
    title = ''
    description = ''
    due_date = ''


class Submission(User):
    ''' Submission class '''

    submissionId = '' # primary key
    assignmentId = '' # reference assignment table
    userId = '' # reference user table
    submission_date = ''
    grade = ''


class Discussion(User):
    ''' Discussion class '''

    discussionId = '' # primary key
    courseId = '' # reference course table
    userId = '' # reference user table
    message = ''
    timestamp = ''
