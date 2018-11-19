# -*- coding: utf-8 -*-

'''
Python Study

SeunghyunSEO

18.11.13(Tue) // day2

fluent-python-2015(ENG)
p8~11
"How special methods are used"

Ex1-2
'''


import torch
from math import hypot
from random import choice

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __abs__(self):
        return hypot(self.x,self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)

    def __mul__(self, scalar):
        #then what is 'def __mul__(self, other):' ???
        return Vector(self.x*scalar, self.y*scalar)

    def __repr__(self):
        #why 'overrides method in object' happens?
        #오버라이딩이면 문제 없는거 아닌가?
        return 'Vector(%r,%r)' % (self.x, self.y)
    '''
    wtf?
        def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass
        
    '''


if __name__=='__main__':
    vec=Vector(4,5)
    print(vec.__abs__()) # may be 6.4031242374328485

    '''
    시간이 없어서 오늘까지는 예제만 하고 다음주부터는 응용예제해보기로
    '''