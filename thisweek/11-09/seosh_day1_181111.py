# -*- coding: utf-8 -*-

'''
Python Study

SeunghyunSEO

18.11.11(sun) // day1

fluent-python-2015(ENG)
p3~8
'''


import torch
import collections
from random import choice

#Library for using List/Dictionary/String/etc...

Card=collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA') # number 2~11 , jack ,queen ,king ,ace
    #['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = 'spades diamonds clubs hearts'.split()
    #['spades', 'diamonds', 'clubs', 'hearts']

    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits
                     for rank in self.ranks]
        '''
        _cards 기본생성자?
        [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), ... Card(rank='A', suit='spades'), 
        Card(rank='2', suit='diamonds'), Card(rank='3', suit='diamonds'), ... Card(rank='A', suit='diamonds'), 
        Card(rank='2', suit='clubs'), Card(rank='3', suit='clubs'), ... Card(rank='A', suit='clubs'), 
        Card(rank='2', suit='hearts'), Card(rank='3', suit='hearts'), ... Card(rank='A', suit='hearts')]
        '''

    def __len__(self):
        return len(self._cards)
        # len = Number of all cards 52

    def __getitem__(self, position):
        return self._cards[position]
    '''
    for example, a[0] = spades 2, Card(rank='2', suit='spades')
    a[-1] = Card(rank='A', suit='spades')
    '''

if __name__=='__main__':
    deck=FrenchDeck()
    mydeck=[choice(deck) for n in range(5)]
    print(mydeck)