class Mammals:
    def __init__(self):
        '''
        Constructor for Mammals class.
        '''
        self.members = ['Tiger', 'Lion', 'Bear', 'Cat', 'Dog', 'Ewok']
        self.harmless = ['Cat', 'Dog']
        self.dangerous = ['Tiger', 'Lion', 'Bear', 'Ewok']

    def printMembers(self):
        for member in self.members:
            print('\t%s' % member)
            
    