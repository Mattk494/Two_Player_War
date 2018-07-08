import random
import time
Deck=[{'2S':2},{'3S':3},{'4S':4},{'5S':5},{'6S':6},{'7S':7},
      {'8S':8},{'9S':9},{'10S':10},{'JS':11},{'QS':12},{'KS':13},{'AS':14},
      {'2H':2},{'3H':3},{'4H':4},{'5H':5},{'6H':6},{'7H':7},
      {'8H':8},{'9H':9},{'10H':10},{'JH':11},{'QH':12},{'KH':13},{'AH':14},
      {'2C':2},{'3C':3},{'4C':4},{'5C':5},{'6C':6},{'7C':7},
      {'8C':8},{'9C':9},{'10C':10},{'JC':11},{'QC':12},{'KC':13},{'AC':14},
      {'2D':2},{'3D':3},{'4D':4},{'5D':5},{'6D':6},{'7D':7},
      {'8D':8},{'9D':9},{'10D':10},{'JD':11},{'QD':12},{'KD':13},{'AD':14}]

class Two_Player():
    player1=[] #Empty list, will add cards to the list when the deal function is executed.
    player2=[] #Empty list, will add cards to the list when the deal function is executed.

    stored_cards=[] #Stores cards in this list when there is a tie. The winner of the tie has these cards appended to their list.


    Handwon1=0 #Keeps track of hands won by player 1
    Handwon2=0 #keeps track of hands won by player 2
    ties=0 #Keeps track of how many ties their were.

    def shuffle(Deck):
        Deck=random.sample(Deck,len(Deck)) #Shuffles the deck
        return Deck #returns the shuffled deck

    def deal(Deck):
        counter=1 #keeps track of how many cards have been dealt out
        while counter<=52:
            if counter%2!=0: #if the counter is not divisible by 2 the card is dealt to player 1.
                Two_Player.player1.insert(0,Deck[counter-1])
                counter+=1
            elif counter%2==0: #if the counter is divisible by 2 the card is dealt to player 2.
                Two_Player.player2.insert(0,Deck[counter-1])
                counter+=1

    def declare_war(self):

        while len(Two_Player.player1)>0 and len(Two_Player.player2)>0:

            Player1_Cardplayed=Two_Player.player1[0] #The card played is the first in player1's deck.

            for key,value in Player1_Cardplayed.items(): #Obtain the key and value for the first card.
                Player1_CardValue= value
                Player1_Card= key
                print("Player 1 plays a",Player1_Card)
                time.sleep(1)


            Player2_Cardplayed=Two_Player.player2[0] #The card played is the first in player2's deck.

            for key,value in Player2_Cardplayed.items(): #Obtain the key and value for the first card.
                Player2_CardValue=value
                Player2_Card= key
                print("Player 2 plays a",Player2_Card)
                time.sleep(1)


            if Player1_CardValue > Player2_CardValue: # Checks to see if player 1 card is greater than player 2.
                Two_Player.Handwon1+=1 #increases the hands one by 1.
                Two_Player.player1.remove(Player1_Cardplayed) # Remove player 1 card from their deck
                Two_Player.player2.remove(Player2_Cardplayed) #Remove player 2 card from their deck

                if len(Two_Player.stored_cards)==0:#check to see if there was a tiebreaker as cards from tiebreaker are stored in stored cards
                    Two_Player.player1.append(Player2_Cardplayed) #adds card to player 1 deck
                    Two_Player.player1.append(Player1_Cardplayed) #adds card to player 1 deck
                    print("Player 1 won the hand")
                    time.sleep(1)

                if len(Two_Player.stored_cards)>0: #check to see if there was a tiebreaker as cards from tiebreaker are stored in stored cards
                    print("Player 1 won the tie breaker")
                    time.sleep(1)
                    Two_Player.player1.extend(Two_Player.stored_cards)  #adds cards to player 1 deck won from tiebreaker
                    Two_Player.stored_cards=[] #Empties list


            elif Player2_CardValue > Player1_CardValue: #Checks to see if player 2 card is greater than player 1 card
                Two_Player.Handwon2+=1 #increases hands won by one.
                Two_Player.player1.remove(Player1_Cardplayed) #removes player 1 card from their deck
                Two_Player.player2.remove(Player2_Cardplayed) #removes player 2 card from their deck

                if len(Two_Player.stored_cards)==0:#check to see if there was a tiebreaker as cards from tiebreaker are stored in stored cards
                    Two_Player.player2.append(Player1_Cardplayed) #adds card to player 2 deck
                    Two_Player.player2.append(Player2_Cardplayed) #adds card to player 2 deck
                    print("Player 2 won the hand")
                    time.sleep(1)

                if len(Two_Player.stored_cards)>0: #check to see if there was a tiebreaker as cards from tiebreaker are stored in stored cards
                    print("Player 2 won the tie breaker")
                    time.sleep(1)
                    Two_Player.player2.extend(Two_Player.stored_cards) #adds cards to player 2 deck won from tiebreaker

                    Two_Player.stored_cards=[] #Empties list


            elif Player1_CardValue== Player2_CardValue: #Checks to see if tiebreaker
                Two_Player.ties=+1

                if len(Two_Player.player1)>1 and len(Two_Player.player2)>1:
                    print("The hand was a tie, each player must play another card")
                    time.sleep(1)
                    Two_Player.stored_cards.append(Player1_Cardplayed) #appends the player 1 tiebreaker cards to stored cards
                    Two_Player.stored_cards.append(Player2_Cardplayed) #appends the player 2 tiebreaker cards to stored cards
                    Two_Player.player1.remove(Player1_Cardplayed) #removes the player 1 card
                    Two_Player.player2.remove(Player2_Cardplayed) # removes the player 2 card
                elif len(Two_Player.player1)==1 and len(Two_Player.playe2)==1:# checkes to see if draw game
                    print("Draw Game")
                    time.sleep(1)
                elif len(Two_Player.player1)==1: #checks to see if player 1 ran out of cards
                    print("It was a tie but player one ran out of cards")
                    time.sleep(1)
                    break
                elif len(Two_Player.player2)==1:# checks to see if player 2 ran out of cards
                    print("It was a tie but player two ran out of cards")
                    time.sleep(1)
                    break






        print("Player 1 won", Two_Player.Handwon1, "Hands")
        print("Player 2 won",Two_Player.Handwon2,"Hands")
        print("There was", Two_Player.ties,"Tie Breakers")


shuffle_the_deck=Two_Player.shuffle(Deck)
Deal_the_deck=Two_Player.deal(shuffle_the_deck)
Declare_war_Two_Player=Two_Player.declare_war(Deal_the_deck)
