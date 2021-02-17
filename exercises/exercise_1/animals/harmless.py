# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:28:10 2021

@author: bener807
"""

class Fish:
    def __init__(self):
        '''
        Constructor for Fish class.
        '''
        self.members = ['Salmon', 'Bass', 'Pike']
        
    def printMembers(self):
        for member in self.members:
            print('\t%s' % member)

class Mammals:
    def __init__(self):
        '''
        Constructor for Mammals class.
        '''
        self.members = ['Cat', 'Dog', 'Monkey']
        
    def printMembers(self):
        for member in self.members:
            print('\t%s' % member)
            
    
class Birds:
    def __init__(self):
        '''
        Constructor for Birds class
        '''
        # Create some members
        self.members = ['Sparrow', 'Red Robin', 'Pidgeon']
        
    def printMembers(self):
        for member in self.members:
            print('\t%s' % member)


