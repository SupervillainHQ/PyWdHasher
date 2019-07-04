'''
Created on 3 Jul 2019

@author: anderskrarup
'''

class UCFirst(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    

    def apply(self, word):
        return word.capitalize()
    
class UCLast(object):
    
    def apply(self, word):
        rev = word[::-1]
        revCapped = rev.capitalize()
        return revCapped[::-1]

class UC(object):
    
    def apply(self, word):
        return word.upper()
        
class Reverse(object):
    
    def apply(self, word):
        return word[::-1]
        
class Truncate(object):
    
    def __init__(self, length, reverse = False):
        self.length = length
        self.reverse = reverse
        
    def apply(self, word):
        if self.reverse:
            last = word[-self.length:]
            return last
        else:
            return word[0:self.length]
        