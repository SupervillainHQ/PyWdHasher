'''
Created on 3 Jul 2019

@author: anderskrarup
'''
from __builtin__ import NotImplementedError

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
        
class Special(object):
    '''
    Ohh you're so special - more entropy with larger character selection
    Special star awarded if you also want users to truncate the password to length ...idiot!
    ... and also, this character-shifting may introduce a single quote in the password - IN THE PASSWORD!!! muahaha!
    '''
    
    def __init__(self, length = 3, reverse = False):
        self.length = length
        self.reverse = reverse
        
    def apply(self, word):
        if self.reverse:
            word = word[::-1]
            
        for x in range(self.length):
            char = word[x].upper()
            n = ord(char)
            if n > 48 and 57 > n:
                # shift digits down to special chars (still above printable asciis)
                shift = 15
            elif n > 64 and 91 > n:
                # shift upper alphas down to special chars (still above printable asciis)
                shift = 32
            newN = n - shift
            newChar = chr(newN)
            word = word[:x] + newChar + word[x+1:]
        
        if self.reverse:
            word = word[::-1]
            
        return word
        