# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 07:05:12 2019

@author: cfitz662
"""

class Student:
    def __init__(self, name, grade):
        self.student_name=name
        self.student_grade=grade
        
    def set_grade(self, grade):
        self.student_grade=grade
    
    def get_grade(self):
        return self.student_grade
    
    def print_student_info (self):
        print('Name: {}, grade: {}'.format(self.student_name, self.student_grade))
        
    