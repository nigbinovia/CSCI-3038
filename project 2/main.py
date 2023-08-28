import random

# the card class is declared and defined
class Card:
# each of the suits are declared as a constant 
    CLUB = 0
    DIAMOND = 1
    HEART = 2
    SPADE = 3

# the constructor to make an individual card is declared and defined 
# the default settings are set to an Ace of Clubs card but this can
# be changed when the constructor is called in practice
    def __init__(self, faceValue = 1, suitValue = CLUB):
        self.faceValue = faceValue
        self.suit = suitValue

# this method takes a card and converts it into a value that can 
# be printed 
    def displayCard(self):
      
# the GetPointsValue() method is called to assign the points to 
# said card 
        point = self.getPointValue()
      
# two dicitionaries are made to first match the suit constants with their 
# matching strings, and second match the face valyes 1, 11, 12, and 13 to 
# their matching strings
        suitDisplay = {Card.CLUB: "CLUB", Card.DIAMOND: "DIAMOND", Card.HEART: "HEART", Card.SPADE: "SPADE"}
        faceDisplay = {11: "Jack", 12: "Queen", 13: "King", 1: "Ace"}
      
# the string version of the suit and face value is done by using each dictionary
        suitName = suitDisplay[self.suit]
        faceName = faceDisplay.get(self.faceValue, str(self.faceValue))
      
# a formatted string with the suit, face value and point value is returned 
        return f"{suitName}-{faceName} {point} points"

# this method returns the point value of a given card
    def getPointValue(self):

# if the face value is between 1 and 10, the point value is set to match
# the face value 
        if self.faceValue <= 10:
            return self.faceValue

# if the face value is between 11 and 13, the point value is set to 10 
        elif 11 <= self.faceValue <= 13:
            return 10

# this method uses __add__ to either add two cards' sums together or
# to add a card and a given integer together 
    def __add__(self, rhs):
# if the rhs is also a card in the card class and is not None, the two
# cards are added together and their sum is returned 
      if isinstance(rhs, Card) and rhs is not None:
        return self.getPointValue() + rhs.getPointValue()
        
# if the rhs is an integer and is not None, the card and the integer are 
# added together and their sum is returned 
      elif isinstance(rhs, int) and rhs is not None:
        return self.getPointValue() + rhs
      else:
# if the rhs isn't another card or an integer, none is returned 
        return None
        

# the deck class is declared and defined 
class Deck:
# this constructor creates a deck of cards as an array and calls the build
# method to add cards to this empty deck 
    def __init__(self):
        self.deck = []
        self.Build()

# this method creates all 52 cards in a given deck for the deck array 
    def Build(self):
# for every suit and for every face value, 14 cards are created for each suit 
# using the Card constructor and are added to the back of the deck 
        for suit in range(4):
            for faceValue in range(1, 14):
                card = Card(faceValue, suit)
                self.deck.append(card)

# this method shuffles the deck of cards using the random feature
    def Shuffle(self):
        random.shuffle(self.deck)

# this method draws a card from the deck 
    def Draw(self):
      
# referring to the isEmpty, if the deck isn't empty, the method pops a card
# from the deck array
        if not self.is_empty():
            return self.deck.pop()

# this method returns if the deck is empty or not 
    def is_empty(self):
      
# if the deck is emoty, the method will return the current number of cards
# in the deck, which are 0
        return len(self.deck) == 0

# this method returns the current size of the deck 
    def size(self):
        return len(self.deck)

# this method takes a given card and returns it a given location in the deck 
    def placeCard(self, card):
  # the method prompts the user asking where they'd like it insert the card 
        print("Where would you like to place the card?")
        print("1. Add to the top of the deck")
        print("2. Add to the bottom of the deck")
        print("3. Add at a specific index")

# after collecting their input, if their choice was 1, their card is added to the top
# of the deck, if their choice was 2, their card is added to the bottom of the deck, and
# if their choice was 3, the user is prompted to enter a valid index value and the card
# is replaced at that index value 
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            self.deck.insert(0, card)
        elif choice == "2":
            self.deck.append(card)
        elif choice == "3":
            index = int(input("Enter the index where you want to place the card: "))
            if 0 <= index <= len(self.deck):
                self.deck.insert(index, card)

# if the user enters an invalid choice or index value, the proper error message 
# is displayed 
            else:
                print("Invalid index. Card not placed.")
        else:
            print("Invalid choice. Card not placed.")

# this method prints the current deck of cards 
    def printDeck(self):
        for card in self.deck:
            print(card.displayCard())

# the hand class is declared and defined
class Hand:

# this constructor creates an empty hand for a player 
    def __init__(self):
        self.hand = []  

# this method adds a card a player's hand (to a maximum of 10 cards)
    def addCard(self, card):
        if len(self.hand) < 10:
            self.hand.append(card)
          
# if the maximum has been reached, an error message is displayed 
        else:
            print("Hand is already full. Cannot add more cards.")

# this method removes a card form a player's hand 
    def removeCard(self, index):

# while the hand isn't empty, a card can be removed from the hand 
        if (index != 0):
          return self.hand.pop(index)

# this method reset's the deck to its original form by removing all the cards 
# from a given hand 
    def Reset(self, index):
# while the hand isn't empty and a deck exists, each card is popped from the hand and added 
# to the bottom of the deck 
        if 0 <= index < len(self.hand):
            card = self.hand.pop(index)
            if isinstance(self.hand, Deck):
                self.hand.deck.append(card)  
              
# if a deck doesn't exist, an error message is displayed 
            else:
                print("Error: 'deck' is not an instance of the Deck class.")
            return card
# if there are no cards in the hand, an error message is displayed
        else:
            print("Invalid index. No card removed.")
            return None
          
# this method returns the total points of a hand
    def addScore(self):
        total_sum = 0
# for every card in the hand, each point value is added to the sum 
        for card in self.hand:
            total_sum += card.getPointValue()
        return total_sum

    def printHand(self):
        for card in self.hand:
            print(card.displayCard())
          

def main():
# Testing the Card class
    print("Card Class Test\n")

# two cards are created with the Card constructor
    card1 = Card(8, Card.SPADE)
    card2 = Card(4, Card.HEART)

# the two cards are displayed with the displayCard method
    print(card1.displayCard())  
    print(card2.displayCard()) 

# the __add__ function is tested by adding two cards together and
# adding an integer to a card
    print(card1 + card2)  
    print(card1 + 11)  

    print("\n")

# Testing the Deck Class
    print("Deck Class Test\n")

# an instanc of a deck is created and printed, and the current 
# size of the deck is printed as well
    deck = Deck()
    #print(f"Deck size: {deck.size()}")  # Output: Deck size: 52
    print("Current Deck Size: ", deck.size())
  
    print("\n")
    deck.printDeck()
    print("\n")

# the deck is shuffled and 5 cards are drawn from the deck and printed 
    deck.Shuffle()

    print("\n")
    print("Shuffled Deck:")
    deck.printDeck()
    print("\n")

    print("5 Drawn Cards:")
    for _ in range(5):
        card = deck.Draw()
        if card:
            print(card.displayCard())
        else:
            print("Deck is empty!")

# the current deck size is redisplayed 
    print("\n")
    print("Current Deck Size: ", deck.size())
    print("\n")

# another card is drawn, printed, and replaced using the placeCard method 
# the final deck is printed 
    print("Drawn Card: ")
    card1 = deck.Draw()
  
    if card1 is not None:
        print(card1.displayCard())
        print("\n")
        deck.placeCard(card1)
        print("\n")
        deck.printDeck()

    else:
        print("The deck is empty. Cannot draw a card.")


# Testing the Hand Class
    print("\n")
    print("Hand Class Test\n")

# the deck is reshuffled and an instance of a hand is created 
    print("Reshuffling the deck: ")
    deck.Shuffle()
    deck.printDeck()

    hand = Hand()

# 5 cards are drawn from the deck and added to the hand
    for _ in range(5):
        card = deck.Draw()  
        hand.addCard(card)

# Then the player's hand and the sum of that hand are printed 
    print("\n")
    print("Player's Hand")
    hand.printHand()

    print("\n")
    print("Player's Sum:")
    print(hand.addScore())  # Output: Sum of points in the hand

if __name__ == "__main__":
  main()
