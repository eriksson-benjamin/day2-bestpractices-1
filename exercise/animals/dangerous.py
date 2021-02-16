# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:16:00 2021

@author: bener807
"""


class Fish:
    def __init__(self):
        '''
        Constructor for Fish class.
        '''
        self.members = ['Shark', 'Piranha', 'Nessie']
        
    def printMembers(self):
        for member in self.members:
            print('\t%s' % member)

class Mammals:
    def __init__(self):
        '''
        Constructor for Mammals class.
        '''
        self.members = ['Tiger', 'Lion', 'Bear', 'Ewok']
        
    def printMembers(self):
        for member in self.members:
            print('\t%s' % member)
            
    
class Birds:
    def __init__(self):
        '''
        Constructor for Birds class
        '''
        # Create some members
        self.members = ['Eagle', 'Hawk', 'Dragon']
        
    def printMembers(self):
        for member in self.members:
            print('\t%s' % member)


