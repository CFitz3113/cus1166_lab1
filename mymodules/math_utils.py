# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 07:05:13 2019

@author: cfitz662
"""

def average_grade(roster):
    total=0
    for student in roster:
        total+=student.get_grade()
    average=total/len(roster)
    return average
 