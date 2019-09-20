# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 07:03:56 2019

@author: cfitz662
"""
from mymodules.models import Student
from mymodules.math_utils import average_grade

def main():
    roster = [Student('Billy', 90),
              Student('Jimmy', 92),
              Student('Claude', 94),
              Student('Dimitri', 88),
              Student('Dorothea', 76),
              Student('Petra', 96),
              Student('Felix', 100),
              Student('Raphael', 75),
              Student('Lorenz', 95),
              Student('Hilda', 79)]
    for i in roster:
        i.print_student_info()
    
    print('\nAverage grade: {:.2f}'.format(average_grade(roster)))
    
    main()


 
 

