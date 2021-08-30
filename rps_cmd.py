import random
import time
class Player:
    def __init__(self, name,chip):
        self.name = name
        self.card_onhand = []
        self.chip=chip
        self.ready=False
        self.main_card=""
        

class RPS:
    def __init__(self,players):
        self.round = 1
        self.card_deck = ['scissors'] * 21 + ['paper'] * 21 + ['rock'] * 21
        self.players= players
        self.win=""
    def poker_mode(self):
        occurence_checker=[]
        for each_player in self.players:
            count_card=each_player.card_onhand.count(each_player.main_card)
            occurence_checker.append(count_card)
        if occurence_checker[0]>occurence_checker[1]:
            self.win=self.players[0].name
        elif occurence_checker[0]<occurence_checker[1]:
            self.win=self.players[1].name
        elif occurence_checker[0]==occurence_checker[1]:
            self.win="TIE"

    def check_mainCards(self):
        comparison_list=[]
        
        for each_player in self.players:
            comparison_list.append(each_player.main_card)
        # O when P2 Wins, 1 when P1 Wins, 2 If Tied
        if comparison_list[0]==comparison_list[1]:
            #TIE CONDITION
            return 2
        # WINNING CONDITIONS FOR P1
        elif comparison_list[0]=="scissors" and comparison_list[1]=="paper":
            return 1
        elif comparison_list[0]=="rock" and comparison_list[1]=="scissors":
            return 1
        elif comparison_list[0]=="paper" and  comparison_list[1]=="rock":
            return 1
        # LOSING CONDITIONS FOR P1
        elif comparison_list[0]=="paper" and comparison_list[1]=="scissors":
            return 0
        elif comparison_list[0]=="rock" and comparison_list[1]=="paper":
            return 0
        elif comparison_list[0]=="scissors" and comparison_list[1]=="rock":
            return 0
        
            

    def discard_cards(self,counter):
        new_cards=[]
        my_list=self.players[counter].card_onhand
        print("Your cards: ",self.players[counter].card_onhand)
        print("Please discard cards according to their positions from 0-4")
        card_toDiscard=input("input cards: ").split(" ")
        card_toDiscard = list(map(int, card_toDiscard))
        for each_position in range(len(card_toDiscard)):
            card_positioned=card_toDiscard[each_position]
            chosen_card=random.choice(self.card_deck)
            self.card_deck.append(self.players[counter].card_onhand[card_positioned])
            new_cards.append(chosen_card)
            print(self.players[counter].name," discards: ", self.players[counter].card_onhand[card_positioned])
            my_list = my_list[:card_positioned] + ["X"]+ my_list[card_positioned+1:]

        self.players[counter].card_onhand=list(filter(("X").__ne__, my_list))
        print("OLD CARDS",self.players[counter].card_onhand)
        self.players[counter].card_onhand.extend(new_cards)
        print("UPDATED CARDS ",self.players[counter].card_onhand)


    def generatePlayerCards(self):
        counter=0
        players=self.players
        for each_player in players:
            
            rolled_cards=[]
            for i in range(5):
                chosen_card=random.choice(self.card_deck)
                rolled_cards.append(chosen_card)
                self.card_deck.remove(chosen_card)
            self.players[counter].card_onhand=rolled_cards
            counter+=1
    def begin_round(self):
        counter=0
        # THIS IS FOR DISCARD ROUND
        for each_player in self.players:
            print("[[Discard Round]] #",self.round)
            print("Player: ",each_player.name," begin.")
            time.sleep(3)
            print("Your cards:  ",each_player.card_onhand)
            operation=int(input("[1] Discard Cards /n [2] End Turn"))
            if operation==1:
                self.discard_cards(counter)
            elif operation==2:
                pass
            counter+=1
        # THIS IS FOR THE ACTUAL ROUND CHOOSING WHICH CARD TO DRAW
        counter=0
        for each_player in self.players:
            print("[[Betting Round]] #" ,self.round)
            print("Player: ",each_player.name," begin.")
            print("Your cards:  ",each_player.card_onhand)
            card_position=int(input("Which card would you like to place:[0-4] "))
            self.players[counter].main_card=each_player.card_onhand[card_position]
            print("You drew: ",each_player.main_card)
            counter+=1
        check_win=self.check_mainCards()
        if check_win==1:
            self.win=self.players[0].name
        elif check_win==2:
            self.pokermode()
        elif check_win==0:
            self.win=self.players[1].name
        self.round+=1
        print("THE WINNER FOR THIS ROUND IS ",self.win)
            


            



    

        
    
def main():
    deck_of_cards=[]
    card_suit=["scissors","paper","rock"]
    my_list = ['scissors'] * 21 + ['paper'] * 21 + ['rock'] * 21
    player_count=2
    players=[]
    run=True
    for each_player in range(player_count):
        player_name=input("Please input player "+str(each_player+1)+"'s name")
        player_chips=input("Please input player "+player_name+"'s chips")
        players.append(Player(player_name,player_chips))
    game=RPS(players)
    while run:
        print("BEFORE: ",len(game.card_deck),game.card_deck)
        game.generatePlayerCards()
        print("AFTER: ",len(game.card_deck),game.card_deck)
        game.begin_round()


        


    # for each_player in players:
    #     if each_player.card_deck==5:
    #         each_player.ready==True
    #     else:
    #         chosen_card=random.choice(my_list)
    #         if my_list.count(chosen_card)==21:
    #             my_list.remove(chosen_card)
    #         else:
    #             each_player


        
        
    # for each_blank_card in range(63):
    #     chosen_card=random.choice(my_list)
    #     if deck_of_cards.count(chosen_card)==21:

    



if __name__=="__main__":
    main()
    