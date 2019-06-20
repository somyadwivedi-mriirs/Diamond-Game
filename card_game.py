#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
computer =[i for i in range(2,15)]
human =[i for i in range(2,15)]
diamond =[i for i in range(2,15)]

def check_winner():
    total_score1 = 0
    total_score2 = 0
    while len(diamond) != 0:
        
        diamond_card = random.choice(diamond)
        print('bid for {}'.format(diamond_card) )
        move1 = int(input("enter your bid"))
        if move1 not in human:
            print("game over ..you have already played this card")
            break
        move2 = random.choice(computer) 
        print('computer move {}'.format(move2) )
        score1,score2 = compare_score(move1,move2,diamond_card)
        print('score_for_this_round {} {}'.format(score1,score2))
        total_score1 = total_score1 + score1
        
        total_score2 = total_score2 + score2
        print(total_score1)
        print(total_score2)
        human.remove(move1)
        computer.remove(move2)
    return total_score1,total_score2

def compare_score(move1,move2,diamond_card):
    d_card = diamond_card
    diamond.remove(diamond_card)
    if move1 > move2:
        return d_card,0
    if move1 < move2:
        return 0,d_card
    if move1  == move2:
        return d_card/2,d_card/2
        
        
h,c = check_winner()
print('final score : you{} computer {}'.format(h,c))
if h > c:
    print('win')
elif h == c:
    print('tie')
else:
    print('lose')

