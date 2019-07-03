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
        