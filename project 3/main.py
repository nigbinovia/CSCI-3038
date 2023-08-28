import random

# the card class is declared and defined
class Card:
# each of the suits are declared as a constant
  CLUB = 0
  DIAMOND = 1
  HEART = 2
  SPADE = 3

# the constructor to make an individual card is declared and defined 
  def __init__(self, faceValue = 1, suitValue = CLUB):
# the default settings are set to an Ace of Clubs card but this can
# be changed when the constructor is called in practice
        self.faceValue = faceValue
        self.suit = suitValue

# this method returns the point value of a given card
  def getPointValue(self):
# if the face value is between 1 and 10, the point value is set to match
# the face value 
    if self.faceValue <= 10:
      return self.faceValue
# if the face value is between 11 and 13, the point value is set to 10 
    elif 11 <= self.faceValue <= 13:
      return 10

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
# if the rhs isn't another card or an integer, none is returned       
    else:
        return None

# this method uses __add__ to either add two cards' sums together or
# to add a card and a given integer together, but in the reverse order
  def __radd__(self, lhs):
# if the lhs is also a card in the card class and is not None, the two
# cards are added together and their sum is returned 
    if isinstance (lhs, Card) and lhs is not None:
      return lhs.getPointValue() + self.getPointValue()
# if the lhs is an integer and is not None, the card and the integer are 
# added together and their sum is returned 
    elif isinstance(lhs, int) and lhs is not None:
      return lhs + self.getPointValue()
# if the lhs isn't another card or an integer, none is returned  
    else:
      return None
        
# the deck class is declared and defined 
class Deck:

# this constructor creates a deck of cards as an array and calls the build
# method to add cards to this empty deck 
  def __init__(self):
    self.deck = []
    self.Build()

# this method returns if the deck is empty or not 
  def isEmpty(self):
# if the deck is empty, the method will return the current number of cards
# in the deck, which are 0
    return len(self.deck) == 0

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
    if not self.isEmpty():
      return self.deck.pop()

# this method takes a given card and returns it a given location in the deck 
  def placeCard(self, card):
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

# this method returns the current size of the deck 
  def __len__(self):
    return len(self.deck)

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
# using the sum() function, for every card in the hand, each point value 
# is added to the sum
    total = sum(card.getPointValue() for card in self.hand)
    return total

# this method prints all the cards in a hand 
  def printHand(self):
    for card in self.hand:
      print(card.displayCard())

# this method returns the size of a hand 
  def __len__(self):
    return len(self.hand)


def main():

# an instance of the deck and a hand for the player and the dealer
# are created
  deck = Deck()
  hand1 = Hand()
  hand2 = Hand()

# the deck is shuffled 
  deck.Shuffle()

# using a for loop, the first two cards are drawn for the player and are
# added to their hand 
  for _ in range(2):
    card = deck.Draw()
    hand1.addCard(card)

# the player's hand is displyed along with the player's sum 
  print("------------------------")
  print("Player's Hand:")
  hand1.printHand()
  print("------------------------")
  
  print("Player's Sum:")
  print(hand1.addScore())
  print("------------------------")

# the user is prompted to either hit or stand and the option is returned to
# the program
  print("What's your next choice?")
  print("1. Hit")
  print("2. Stand")
  choice = int(input("Enter your choice:\n"))

# if the player chooses 1, a new card is drawn, added to their hand and their 
# sum is updated 
  while (choice != 2):
    card = deck.Draw()
    hand1.addCard(card)
    print("------------------------")
    print("------------------------")
    print("Player's Hand:")
    hand1.printHand()
    print("------------------------")

    print("Player's Sum:")
    print(hand1.addScore())
    print("------------------------")

# if the player's hand ever exceeds 21, a bust is called and the player loses
    if (hand1.addScore() > 21):
      print("------------------------")
      print("------------------------")
      print("BUST. Player lost. Dealer wins.")
      print("------------------------")
      print("------------------------")
      break

# if the player's hand is still under or at 21, they're again prompted to either 
# hit again or stand 
    else:
      print("What's your next choice?")
      print("1. Hit")
      print("2. Stand")
      choice = int(input("Enter your choice:\n"))

# if the player chooses 2, their option is printed and the game moves on to the dealer 
  if (choice == 2):
    print("------------------------")
    print("------------------------")
    print("You chose to stand.")

# the dealer draws cards until their sum is at or above 17 points
    while (hand2.addScore() < 17):
      card = deck.Draw()
      hand2.addCard(card)

# afterwards, the dealer's hand is revealed with their sum
    print("------------------------")
    print("------------------------")
    print("REVEAL:")
    print("------------------------")
    print("------------------------")

    print("Dealer's Hand:")
    hand2.printHand()
    print("------------------------")
    print("Dealer's Sum:")
    print(hand2.addScore())
    print("------------------------")

# two variables score1 and score2 are used to determine who has a closer score 
# to 21 -- the smaller the variable, the closer to 21 (the winner)
    score1 = (21 - hand1.addScore())
    score2 = (21 - hand2.addScore())

# if the dealer exceeded 21 in their drawing process, a bust is called and the dealer
# loses
    if (hand2.addScore() > 21):
      print("BUST. Dealer lost. Player wins.")
# whichever score variable is smaller determines the winner and if the score variables 
# match, a draw is called 
    else:
      if (score1 < score2):
        print("Player wins.")
      elif(score2 < score1):
        print("Dealer wins.")
      elif (score1 == score2):
        print("Draw.")

  
  
if __name__ == "__main__":
  main()
