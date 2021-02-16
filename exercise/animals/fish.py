class Fish:
    def __init__(self):
        '''
        Constructor for Fish class.
        '''
        self.members = ['Salmon', 'Shark', 'Bass']
        
    def printMembers(self):
        for member in self.members:
            print('\t%s' % member)