import random

computer =[i for i in range(2,15)]
human =[i for i in range(2,15)]
diamond =[i for i in range(2,15)]

def check_winner():
    human_score = 0
    computer_score = 0
    while len(diamond) != 0:
        
        diamond_card = random.choice(diamond)
        print('bid for {}'.format(diamond_card) )
        human_throw = int(input("enter your bid"))
        if human_throw not in human:
            print("game over ..you have already played this card")
            break
        computer_throw = random.choice(computer) 
        print('computer move {}'.format(computer_throw) )
        score1,score2 = compare_score(human_throw,computer_throw,diamond_card)
        print('score_for_this_round {} {}'.format(score1,score2))
        human_score = human_score + score1
        
        computer_score = computer_score + score2
        print(human_score)
        print(computer_score)
        human.remove(human_throw)
        computer.remove(computer_throw)
    return human_score,computer_score

def compare_score(human_throw, computer_throw, diamond_card):
    d_card = diamond_card
    diamond.remove(diamond_card)
    if human_throw > computer_throw:
        return d_card,0
    if human_throw < computer_throw:
        return 0,d_card
    if human_throw  == computer_throw:
        return d_card/2,d_card/2
        
        
h,c = check_winner()
print('final score : you{} computer {}'.format(h,c))
if h > c:
    print('win')
elif h == c:
    print('tie')
else:
    print('lose')

