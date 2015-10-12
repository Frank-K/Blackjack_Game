# Name: Frank Karunaratna
# Date: August 17, 2015
# File Name: Deck.py
# Description: This class creates a deck class that will store a deck of card.

from card import *
import random

class Deck:
    '''A Deck is a list of card objects. The deck can be shuffled and the card
       at the top can be selected'''

    def __init__(self):
        '''creates a list with all the cards in a deck'''

        self.card_list = []
        letter_list = ['S','C','D','H']

        for letter in letter_list:
            for num in range(1,14):
                self.card_list.append(Card(num,letter))

    def shuffle(self):
        '''shuffles the deck of cards'''
        
        random.shuffle(self.card_list)

    def dealCard(self):
        '''returns the first card in the list of cards and removes it from
           the list'''
        
        topCard = self.card_list[0]
        del self.card_list[0]

        return topCard

    def cardsLeft(self):
        '''returns the number of cards left in the list'''
        
        return len(self.card_list)

    def getDeck(self):
        '''returns the list of the card objects'''
        
        return self.card_list
