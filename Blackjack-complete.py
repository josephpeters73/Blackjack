
import random
from random import shuffle
from time import sleep
import os
from os import system, name


suits = ("Heart","Spade","Club","Diamond")

names = ("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten",
        "Jack","Queen","King","Ace")

values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,
         "Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11} 

bet = random.randrange(100,5000,100)
funds = bet

player_standing = ""
player_standing = player_standing.upper()

insurance_standing = ""

house_total = 0
player_total = 0
players_bet = 0
ins_bet = 0


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
            
            
    def __str__(self):
        return f'{self.name} has the {self.all_cards[0]} showing!\n'
        
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
        return f"{self.name} has the {self.all_cards[0]} and the {self.all_cards[1]}\n"

player_one_name = input("Please provide your name: \n")

new_deck = Deck()

new_deck.all_cards = new_deck.all_cards * 4

new_deck.shuffle()


def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')


def player():
    
    global player_one
    global house
    
    player_one = Player(player_one_name)

    house = Dealer("Dealer")

def deal():
    
    global player_one
    global house
    
    for x in range(2):               
        player_one.add_cards(new_deck.deal())
        house.add_cards(new_deck.deal())
        
def insurance():
    
    global ins_bet
    global insur
    global insurance_standing
    
    choice = True
    while choice == True:
        insur = input(f"THE DEALER HAS AN ACE SHOWING WOULD YOU LIKE INSURANCE? Insurance will be half your current bet of {players_bet}. YES or NO")
        sleep(3)
        insur = insur.upper()
        if insur == "YES":
            insurance_standing = "YES"
            ins_bet = int(players_bet / 2)
            choice = False
            break
        elif insur == "NO":
            choice = False
            break
        elif insur != "YES":
            choice = False
            break
            
def int_var():

    global players_bet
    

    testing = True
    while testing:
        players_bet = input(f"\n{player_one_name} please place a bet, you have {funds} dollars.\n")
        try:
            players_bet = int(players_bet)
            testing =False
        except:
            print("that is not a number")

    else:
        pass


def bet_var():

    testing = True
    while testing:
        if players_bet < 1 or players_bet > funds:
            print (" not a valid bet")
            int_var()
        else:
            testing = False
            
def ace_house(deck):
    
    global house_total
    house_total = 0
    
    a = 0
    b = 0
    
    if deck[0] == 11 and deck[1] == 11:
        a = deck.pop(0)
    elif deck[0] == 11 and deck[1] != 11:
        a = deck.pop(0)
    elif deck[0] != 11 and deck[1] == 11:
        b = deck.pop(1)
    elif deck[0] != 11 and deck[1] != 11:
        pass
        
    
    for index, item in enumerate(deck):
        if item == 11:
            deck[index] = deck[index] - 10
            
    if a > b:
        deck.insert(0,a)
    elif b > a:
        deck.insert(1,b)
        
    for x in deck:
        house_total = house_total + x
        

        
def ace_player(deck):
    
    global player_total
    player_total = 0
    
    a = 0
    b = 0
    
    if deck[0] == 11 and deck[1] == 11:
        a = deck.pop(0)
    elif deck[0] == 11 and deck[1] != 11:
        a = deck.pop(0)
    elif deck[0] != 11 and deck[1] == 11:
        b = deck.pop(1)
        
    
    for index, item in enumerate(deck):
        if item == 11:
            deck[index] = deck[index] - 10
            
    if a > b:
        deck.insert(0,a)
    elif b > a:
        deck.insert(1,b)
        
    for x in deck:
        player_total = player_total + x
        
        
def player_cards(player_deal):

    global player_one_name
    global player_one
    global player_standing

    if player_total == 21 and len(player_one.all_cards) == 2:
        print (f"{player_one_name} has Blackjack!!\nDealer losses\n")
        player_standing = "BLACKJACK"
        betting()

    elif player_total > 21:
        print (f"{player_one_name} has Busted, Dealer has Won this hand!\n")
        player_standing = "BUST"
        betting()

    else:
         pass
        
def hit():

    global player_deal
    global house_deal
    card = True
    
    while card == True:

        if player_total <= 21:
            choice = input(f"\n{player_one_name} would you like to HIT or STAY? \n")
            choice = choice.upper()
            
            
        
            if choice == "HIT" and len(player_one.all_cards) == 2:
                
                player_one.add_cards(new_deck.deal())
                player_value = [player_one.all_cards[0].value,player_one.all_cards[1].value,player_one.all_cards[2].value]
                ace_player(player_value)
                print (f'\n{player_one.all_cards[0]},{player_one.all_cards[1]},{player_one.all_cards[2]}\nthe card total is {player_total}\n')
                player_cards(player_total)
                
            elif choice == "HIT" and len(player_one.all_cards) == 3:

                player_one.add_cards(new_deck.deal())
                player_value = [player_one.all_cards[0].value,player_one.all_cards[1].value,player_one.all_cards[2].value,player_one.all_cards[3].value]
                ace_player(player_value)
                print (f'\n{player_one.all_cards[0]},{player_one.all_cards[1]},{player_one.all_cards[2]},{player_one.all_cards[3]}\nthe card total is {player_total}\n')

                player_cards(player_total)


            elif choice == "HIT" and len(player_one.all_cards) == 4:

                player_one.add_cards(new_deck.deal())
                player_value = [player_one.all_cards[0].value,player_one.all_cards[1].value,player_one.all_cards[2].value,player_one.all_cards[3].value,player_one.all_cards[4].value]
                ace_player(player_value)
                print (f'\n{player_one.all_cards[0]},{player_one.all_cards[1]},{player_one.all_cards[2]},{player_one.all_cards[3]},{player_one.all_cards[4]}\nthe card total is {player_total}\n')

                player_cards(player_total)

            elif choice == "HIT" and len(player_one.all_cards) == 5:

                player_one.add_cards(new_deck.deal())
                player_value = [player_one.all_cards[0].value,player_one.all_cards[1].value,player_one.all_cards[2].value,player_one.all_cards[3].value,player_one.all_cards[4].value,player_one.all_cards[5].value]
                ace_player(player_value)
                print (f'\n{player_one.all_cards[0]},{player_one.all_cards[1]},{player_one.all_cards[2]},{player_one.all_cards[3]},{player_one.all_cards[4]},{player_one.all_cards[5]}\nthe card total is {player_total}\n')
            
            elif choice == "STAY":
                hand = False
                break
                
                
            elif house_total > 21:
                print (f"Dealer has Busted, his hand total is {house_total}\n{player_one_name} has Won this hand!:\n")
                player_standing = "WIN"
                
                hand = False
                break    
    
        
def dealers_cards(house_deal):
    
    hand = True
    
    global dealer_hand
    global dealer
    global player_standing
    
    
    if house_deal == 21 and len(house.all_cards) == 2:
        print (f"Dealers cards are {house.all_cards}/n Dealer has Blackjack!!/n {player_one_name} losses ")
        player_standing = "LOSS"
        betting()
    
    
    elif house_deal == 22:
        card_values = house.all_cards[0].value, house.all_cards[1].value
        ace_check(card_values)
        print("dealer")
        
    while hand == True:
        
        if house_total > 21:
            print (f"\nDealer has Busted,\nhis hand total is {house_total}\n{player_one_name} has Won this hand!:\n")
            player_standing = "WIN"
           
            hand = False
            break

        elif house_total >= 17 and house_total <= 21:
            print (f"\nDealer has {house_total}\n")
            
            break
            
        elif house_total < 17 and len(house.all_cards) == 2:

            house.add_cards(new_deck.deal())
            house_value = [house.all_cards[0].value,house.all_cards[1].value,house.all_cards[2].value]
            print(f"\n{house.all_cards[0]},{house.all_cards[1]},{house.all_cards[2]}")
            ace_house(house_value)
            
            
        elif house_total < 17 and len(house.all_cards) == 3: 
            house.add_cards(new_deck.deal())
            house_value = [house.all_cards[0].value,house.all_cards[1].value,house.all_cards[2].value,house.all_cards[3].value]
            print(f"\n{house.all_cards[0]},{house.all_cards[1]},{house.all_cards[2]},{house.all_cards[3]}")
            ace_house(house_value)
            
            
        elif house_total < 17 and len(house.all_cards) == 4:
            
            house.add_cards(new_deck.deal())    
            house_value = [house.all_cards[0].value,house.all_cards[1].value,house.all_cards[2].value,house.all_cards[3].value,house.all_cards[4].value]
            print(f"\n{house.all_cards[0]},{house.all_cards[1]},{house.all_cards[2]},{house.all_cards[3]},{house.all_cards[4]}")
            ace_house(house_value)
    
            
            
    else:
        print (f"Dealer has the {house.all_cards}\nwith a total of {house_total}\n")
        hand = False
    
    
def winner():
    global player_standing
    
    if player_total > house_total and player_total < 21:
        print (f"\n{player_one_name} WINS!!!")
        player_standing = "WIN"
        betting()

    elif player_total < house_total and house_total < 21:
        print (f"\nDealer WINS!!!\n")
        player_standing = "LOSS"
        betting()

    elif player_total == house_total:
        print (f"\nTie Game")
        player_standing = "TIE"
        betting()
    else:
        pass    
    

def betting():
    
    global funds
    global players_bet
    global player_standing
    
    
    if player_standing == "WIN":

        funds = (funds - players_bet) + (players_bet * 2)
        player_standing = ""
        players_bet = 0
        game_play()
        

    elif player_standing == "LOSS":
        
        funds = funds - players_bet
        player_standing = ""
        players_bet = 0
        game_play()
        
    elif player_standing == "BUST":
        
        funds = funds - players_bet
        player_standing = ""
        players_bet = 0
        game_play()

    elif player_standing == "BLACKJACK":
        
        funds = (funds - players_bet) + (players_bet * 1.5)
        player_standing = ""
        players_bet = 0
        game_play()

    elif player_standing == "INSURANCE":
        
        funds = (funds - (0.5 * players_bet)) * 1.5
        player_standing = ""
        players_bet = 0
        game_play()

    elif player_standing == "TIE":
        
        funds = funds
        player_standing = ""
        players_bet = 0
        game_play()
        
    else:
        game_play()   
        
def game_play():
    
    global funds 

    game_on = True
    
    if funds == 0:
        print("\n")
        print("You lost all your money!!")
        play_again = input("Would you like to play again? YES or NO \n")
        play_again = play_again.upper()
    else:
        play_again = input("Would you like to play again? YES or NO \n")
        play_again = play_again.upper()
    
    while game_on == True:
        
        if play_again == "YES" and funds == 0:
            print (f"Our loan Shark has agree to loan you a small amount of money {player_one_name}")
            sleep(5)
            bet = random.randrange(100,5000,100)
            funds = bet

        elif play_again == "YES":
            start()
        elif play_again == "NO":
            game = False
            os._exit(00)
        elif play_again != "YES" or play_again != "NO":
            play_again = input("I don't understand that answer please answer with a YES or NO:\n")
            play_again = play_again.upper()
        else:
            game_on = False        



                   
def start():
    
    clear()
    #clear_output()
    
    global player_deal
    global house_deal
    global house_value
    global player_value
    global insurance_standing

    player()
    deal()
    
    int_var()
    bet_var()
    
        
    player_deal = (player_one.all_cards[0].value + player_one.all_cards[1].value)
    player_value = [player_one.all_cards[0].value,player_one.all_cards[1].value]
    ace_player(player_value)
    
    house_deal = (house.all_cards[0].value + house.all_cards[1].value)
    house_value = [house.all_cards[0].value,house.all_cards[1].value]
    ace_house(house_value)
    
    player_one_hand = (player_one)

    print (f"\n{player_one_name}'s card total is {player_deal}\n")

    print (house)
    if house.all_cards[0].value == 11:
        insurance()
        if house_value == 21:
            insurance_standing == "YES"
        else:
            insurance_standing == "NO"
                
    else:
        pass
    
    player_cards(player_deal)
    hit()
    dealers_cards(house_deal)
    winner()
    betting()
    game_play()

start()






