#Function and classes
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class Deck(Card):
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    def __str__(self):
         deck_comp = ""
         for crd in self.deck:
             deck_comp += "\n" + crd.__str__()
         return "Deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def addCard(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if values[card.rank] == 11:
            self.aces += 1

    def adjustAce(self):
        while self.value > 21 and  self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much you want to bet? "))
        except:
            print("Sorry, please input an integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you don't have enough chips! You have {}".format(chips.total))
            else:
                break

def hit(deck,hand):
    the_card = deck.deal()
    hand.addCard(deck.deal())
    hand.adjustAce()

def hit_or_stand(deck,hand):
    global playing
    while True:
        ans = input("Hit or Stand? Enter h or s: ")
        if ans[0].lower() == "h":
            hit(deck,hand)
            break
        elif ans[0].lower() == "s":
            print("Player Stands. \nDealer's turn")
            playing = False
            break
        else:
            print("Couldn't understand please try again!")
            continue

def dealer_turn(deck,hand):
    while hand.value < 17:
        hit(deck,hand)

def player_bust(chips):
    print("\nBUST PLAYER!\n")
    chips.lose_bet()

def player_wins(chips):
    print("\nPLAYER WINS!\n")
    chips.win_bet()

def dealer_bust(chips):
    print("\nPLAYER WINS! DEALER BUSTED\n")
    chips.win_bet()

def dealer_wins(chips):
    print("\nDEALER WINS!\n")
    chips.lose_bet()

def push(chips):
    print("\nDealer and player tie! PUSH!!\n")


#Game starts here
print("Welcome to Blackjack!")
while True:
    try:
        para = int(input("How many chips? "))
        break
    except:
        print("Please input an integer.")
        continue
player_chips = Chips(para)

while True:
    print("Shuffle the deck dealer!")
    kagit = Deck()
    kagit.shuffle()
    player_hand = hand()
    dealer_hand = hand()
    player_hand.addCard(kagit.deal())
    dealer_hand.addCard(kagit.deal())
    player_hand.addCard(kagit.deal())
    dealer_hand.addCard(kagit.deal())
    take_bet(player_chips)
    print("\n"*100 + "Dealer's cards are:")
    print("<card hidden>")
    for i in range(len(dealer_hand.cards)-1):
        print(dealer_hand.cards[i],"\n")
    print("Your cards are:")
    for i in range(len(player_hand.cards)):
        print(player_hand.cards[i])
    print(player_hand.value)
    playing = True
    while playing:
        hit_or_stand(kagit,player_hand)
        print("\n"*100 + "Dealer's cards are:")
        print("<card hidden>")
        for i in range(len(dealer_hand.cards)-1):
            print(dealer_hand.cards[i],"\n")
        print("Your cards are:")
        for i in range(len(player_hand.cards)):
            print(player_hand.cards[i])
        print(player_hand.value)
        if player_hand.value > 21:
            player_bust(player_chips)
            break
        else:
            dealer_turn(kagit,dealer_hand)
    if player_hand.value > 21:
        print("You have {} chips remaining".format(player_chips.total))
        print("Would you like to bet again?")
        res = input("Enter y or n: ")
        if res[0].lower() == "y":
            continue
        elif res[0].lower() == "n":
            print("Thank you for playing.\nHope to see you again!")
            break
        else:
            break
    print("\nDealer got:\n")
    for i in range(len(dealer_hand.cards)):
        print(dealer_hand.cards[i])
    print(dealer_hand.value)
    if dealer_hand.value > 21:
        dealer_bust(player_chips)
    elif dealer_hand.value > player_hand.value:
        dealer_wins(player_chips)
    elif dealer_hand.value == player_hand.value:
        push(player_chips)
    else:
        player_wins(player_chips)
    if player_chips.total == 0:
        print("You have {} chips remaining".format(player_chips.total))
        print("Thank you for playing.\nHope to see you again!")
        break
    print("You have {} chips remaining".format(player_chips.total))
    print("Would you like to bet again?")
    res = input("Enter y or n: ")
    if res[0].lower() == "y":
        continue
    elif res[0].lower() == "n":
        print("Thank you for playing.\nHope to see you again!")
        break
    else:
        break
