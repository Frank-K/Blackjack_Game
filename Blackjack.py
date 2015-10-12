# Name: Frank Karunaratna
# Date: August 17, 2015
# File Name: Blackjack.py
# Description: This program allows the user to play blackjack against the
#              computer.

from Deck import *
from graphics import *
from button2 import *
import random

def setupGUI():
    '''Creates the GUI'''

    global win,start,quitt,userCard1,userCard2,dealerCard1,dealerCard2,hitMe
    global stand,message,playAgain,start

    #Draws the GUI
    win = GraphWin("Blackjack",700,400)
    win.setBackground('green4')

    titleOutline = Text(Point(353,170),"BLACKJACK")
    titleOutline.setStyle('bold')
    titleOutline.setFace('helvetica')
    titleOutline.setSize(30)
    titleOutline.draw(win)

    title = Text(Point(350,170),"BLACKJACK")
    title.setStyle('bold')
    title.setFace('helvetica')
    title.setSize(30)
    title.setFill('gold')
    title.draw(win)

    box = Rectangle(Point(200,188),Point(500,214))
    box.setFill('grey20')
    box.draw(win)

    message = Text(Point(350,201),"Press Start to start the game")
    message.setSize(12)
    message.setFace('arial')
    message.setFill('gold2')
    message.draw(win)

    userCard1 = Image(Point(340,325),'back.gif')
    userCard1.draw(win)

    userCard2 = Image(Point(360,325),'back.gif')
    userCard2.draw(win)

    dealerCard1 = Image(Point(340,75),'back.gif')
    dealerCard1.draw(win)

    dealerCard2 = Image(Point(360,75),'back.gif')
    dealerCard2.draw(win)

    start = Button(win,Point(300,235),83,30,"Start",'gray50')
    start.activate()

    quitt = Button(win,Point(600,201),80,30,"Quit",'LightBlue4')
    quitt.activate()

    playAgain = Button(win,Point(400,235),83,30,"Play Again",'gray50')

    hitMe = Button(win,Point(100,182),80,30,"Hit Me",'LightBlue4')

    stand = Button(win,Point(100,220),80,30,"Stand",'LightBlue4')

def dealerAI(cards,points,userPoints,deck):
    '''Runs the AI for the dealer and calls the endGame function'''

    if sum(userPoints) <= 21:

        #If the dealer has less than 15 he draws a card from the deck
        if sum(points) < 15:

            #Dealer hits him self
            card = deck.dealCard()
            cards.append(card)

            #Draws card to the window
            position = cards.index(card)
            card.draw(win,Point(340+(20*position),75))

            num = addTotal(card)
            points.append(num)

            points = winLose(points)

            #Re-calls dealerAI to see if the dealer has to hit himself again
            dealerAI(cards,points,userPoints,deck)

        #If the dealer has more than 15 he stands    
        else:
            endGame(userPoints,points)

    #If the user's total is over 21 the dealer stands        
    elif sum(userPoints) > 21:
        endGame(userPoints,points)

def addTotal(cardd):
    '''Returns the value of the card that was drawn'''
    
    if cardd.getRank() == 1:
        return 11
    
    elif cardd.getRank() >= 10:
        return 10
    
    else:
        return cardd.getRank()

def winLose(listt):
    '''Checks if the user's total is above 21, and returns a list with the
       values of the cards'''

    #If the user's total is above 21 it checks to see if there is an Ace in the
    #hand
    if sum(listt) > 21:
        
        for x in listt:
            
            if x == 11:
                
                #If there is an Ace the value is changed from a 11 to a 1
                listt.remove(11)
                listt.append(1)

                #Checks to see if user total is equal to 21
                if sum(listt) == 21:
                    message.setText("Your total is 21, you must stand.")
                    hitMe.deactivate()
                return listt

        #If the player doesn't have an Ace they have busted
        message.setText("Player bust, you must stand.")
        hitMe.deactivate()
        return listt

    #If the users total is 21 they are forced to stand    
    elif sum(listt) == 21:
        message.setText("Your total is 21, you must stand.")
        hitMe.deactivate()
        return listt

    else:
        return listt

def endGame(userPoints,dealerPoints):
    '''Decides who wins the game and prints the correct message'''

    #Checks to see who won and prints a message
    if sum(userPoints) > 21:
        message.setText("YOU BUSTED, DEALER WINS!")
        
    elif sum(dealerPoints) > 21:
        message.setText("DEALER BUSTED, YOU WIN!!!")
        
    elif sum(userPoints) > sum(dealerPoints):
        message.setText("YOU WIN!!!")

    elif sum(dealerPoints) > sum(userPoints):
        message.setText("DEALER WINS!")

    elif sum(userPoints) == sum(dealerPoints):
        message.setText("It's a tie!")
    
def main():
    '''Main program for the blackjack game'''

    #Creates the GUI and the deck object
    setupGUI()
    deck = Deck()

    #List of the card objects
    listUser = []
    listDealer = []

    #List the the card values
    userTotal = []
    dealerTotal = []

    counter = 0

    pt = win.getMouse()

    while not quitt.clicked(pt):

        if start.clicked(pt):

            #Shuffles the deck
            deck.shuffle()

            #Gets the users first 2 cards and draws them to the window
            uCard1 = deck.dealCard()
            uCard1.draw(win,userCard1.getAnchor())

            uCard2 = deck.dealCard()
            uCard2.draw(win,userCard2.getAnchor())

            #Adds the 2 cards to the users list of cards
            listUser.append(uCard1)
            listUser.append(uCard2)

            #Gets the dealers 2 cards and draws one of them to the window
            dCard1 = deck.dealCard()
            
            dCard2 = deck.dealCard()
            dCard2.draw(win,dealerCard2.getAnchor())

            #Adds the 2 cards to the dealers list of cards
            listDealer.append(dCard1)
            listDealer.append(dCard2)

            #Gets the values of the users cards and appends them to the list
            num = addTotal(uCard1)
            userTotal.append(num)

            num = addTotal(uCard2)
            userTotal.append(num)

            message.setText("Press Hit Me or Stand")

            start.deactivate()
            stand.activate()
            hitMe.activate()

            #Checks the users total to see if they have 21
            userTotal = winLose(userTotal)

        if hitMe.clicked(pt):

            #Deals a card to the user and adds it to the list
            listUser.append(deck.dealCard())

            #Draws the new card to the window
            x = userCard2.getAnchor().getX()
            y = userCard2.getAnchor().getY()
            listUser[counter+2].draw(win,Point(x+20*(counter+1),y))

            #Adds the value of the card to the list and checks to see if the
            #user has got 21 or over 21
            num = addTotal(listUser[counter+2])
            userTotal.append(num)

            userTotal = winLose(userTotal)
            
            counter = counter + 1

        if stand.clicked(pt):
            
            stand.deactivate()
            hitMe.deactivate()
            playAgain.activate()

            #Reveals the dealers cards
            dCard2.undraw()
            dCard1.draw(win,dealerCard1.getAnchor())
            dCard2.draw(win,dealerCard2.getAnchor())

            #Gets the value of the dealers cards and adds them to the list
            num2 = addTotal(dCard1)
            dealerTotal.append(num2)

            num2 = addTotal(dCard2)
            dealerTotal.append(num2)
            
            #Calls the dealerAI
            dealerAI(listDealer,dealerTotal,userTotal,deck)

        if playAgain.clicked(pt):

            #Undraws all the cards
            for card in listUser:
                card.undraw()

            for card in listDealer:
                card.undraw()

            #Empties the lists
            listUser = []
            listDealer = []
    
            userTotal = []
            dealerTotal = []

            counter = 0

            #Creates a new deck
            deck = Deck()

            playAgain.deactivate()
            start.activate()

            message.setText("Press Start to start the game")


        pt = win.getMouse()

    win.close()
    
main()
