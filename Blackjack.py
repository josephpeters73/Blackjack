#!/usr/bin/env python
# coding: utf-8

# In[13]:


#blackjack(21)

from random import shuffle
#multi deck of cards
#value set to cards
#suit assigned to cards {X}
#name set to cards

suits = ("Heart","Spade","Club","Diamond")

names = ("Two","Three","Four","Five","Six","seven","eight","Nine","Ten",
        "Jack","Queen","King","Ace")

values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"seven":7,"eight":8,
         "Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11} 

class Card:
    
    def __init__(self,suit,name):
        self.suit = suit
        self.name = name
        self.value = values[name]
        
    def __str__(self):
        return self.name + ' of ' + self.suit + 's'
    
class Deck:
    
    def __init__(self):
        self.all_cards = []
       
        for suit in suits:
            for name in names:
                self.all_cards.append(Card(suit,name))
            
                    
    def shuffle(self):
        shuffle(self.all_cards)
        
    def deal(self):
        return self.all_cards.pop(0)
        
    def __str__(self):
        return self.all_cards    
    
class Dealer:
    
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def hit_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
            
    def __str__(self):
        return f'{self.name} has the {self.all_cards[0]} showing!'
        
class Player:
    
    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self):
        return f'{self.name} has the {self.all_cards[0]} and the {self.all_cards[1]}'
        
        
    


# In[ ]:


#Game Logic    
player_one_name = input("Please provide your name:")
player_one = Player(player_one_name)
house = Dealer("Dealer")

#Setup New Game
new_deck = Deck()
new_deck.all_cards = new_deck.all_cards * 4
new_deck.shuffle()


def deal():
    
    for x in range(2):                #deals cards
        player_one.add_cards(new_deck.deal())
        house.add_cards(new_deck.deal())
        
        
''''class FirstDeal:
#    
#    def __init__(self,player):
#        self.player = player
    
    def hand(self):
        if player == 22:
            player == player - 10 
        elif player == 21:
            Print ("Player one has BlackJack you win this hand")
        elif player[0].value == player[1].value:
            choice = input(f'{player}would you like to split your hand')
        else: 
            choice = input(f"player one Would like to hit,stay")
    
    def __str__(self):
        print ("hello")'''

def dealers_cards(house_deal):
   
    hand = True
    global dealer
    second_deal = []
    
    if house_deal == 21:
        print (f"Dealer has Blackjack!! {player_one_name} losses ")
    else:
        pass
    
    while hand == True: 
        if house_deal == 22:
            house_deal = (house_deal - 10)

        elif house_deal < 16:
	       
        	house.add_cards(new_deck.deal())
        	second_deal = (house.all_cards[0].value + house.all_cards[1].value + house.all_cards[2].value)
        	
        	house_deal = second_deal
        	second_deal = []

        elif house_deal > 16 and house_deal <= 21:
            print (f"Dealer has {house_deal}")
            hand = False
        elif house_deal > 21:
            print (f"Dealer has Busted, {player_one_name} has Won this hand!")
            hand = False
    pass
    
    
def players_cards(house_deal):
   
    hand = True
    global player_one
    second_deal = []
    
    if house_deal == 21:
        print (f"Dealer has Blackjack!! {player_one_name} losses ")
    else:
        pass
    
    while hand == True: 
        if house_deal == 22:
            house_deal = (house_deal - 10)

        elif house_deal < 16:
	       
        	house.add_cards(new_deck.deal())
        	second_deal = (house.all_cards[0].value + house.all_cards[1].value + house.all_cards[2].value)
        	
        	house_deal = second_deal
        	second_deal = []

        elif house_deal > 16 and house_deal <= 21:
            print (f"Dealer has {house_deal}")
            hand = False
        elif house_deal > 21:
            print (f"Dealer has Busted, {play_one_name} has Won this hand!")
            hand = False
    pass
        
        

#Play the Game
deal()


first_deal_player_one = (player_one.all_cards[0].value + player_one.all_cards[1].value)
house_deal = (house.all_cards[0].value + house.all_cards[1].value)

player_one_hand = (player_one)
dealer_hand = (house)


print (player_one_hand)
print (first_deal_player_one)
#FirstDeal(player_one_hand)
#hand(player_one_hand)
#print ("\n")
dealers_cards(house_deal)





#if choice == "stay":
#    print (player_one_hand)
#elif choice == "hit":
#    hit_choice()
#    print(player_one_hand)
#   second_deal = (player_one.all_cards[0].value + player_one.all_cards[1].value + player_one.all_cards[2].value)
    
#    print(second_deal)
    

#print (player_two_hand)
#print (first_deal_player_two)

#while game_on == True:
     #pass
        
        
    
#shuffle the decks

#one player vs Computer

#deal the hand between two players
#show cards to player only show one card for dealer until player stays

#player can hit or stay (possiblly split)

#player wil have starting pot and control betting

#rolling tally of money and max oeamount of bet

#alret player of Blackjack, win, lose or Bust


# In[ ]:


'''hit_cards(dealer)
        second_deal = (dealer.all_cards[0].value + dealer.all_cards[1].value + dealer.all_cards[2].value)
        print (second_deal)
        first_deal_dealer = second_deal
        second_deal = []'''

