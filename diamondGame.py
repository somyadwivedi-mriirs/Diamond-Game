import random

def getThrow(H_DECK, C_DECK, REFERENCE_DECK, H_SCORE, C_SCORE):
    
    REFERENCE_THROW = random.choice(REFERENCE_DECK)
    print("THE DIAMOND CARD IS: " + str(REFERENCE_THROW))
    H_THROW = int(input("Enter your Bid :- "))
    if (H_THROW not in H_DECK):
        print( "You have already played this card!")
        exit (0)
    C_THROW = random.choice(C_DECK)
    print("Computer: " + str(C_THROW))
    H_THROW, C_THROW, REFERENCE_THROW, H_SCORE, C_SCORE = gamePlay(H_THROW, C_THROW, REFERENCE_THROW, H_SCORE, C_SCORE)
    return H_THROW, C_THROW, REFERENCE_THROW, H_SCORE, C_SCORE
    
def gamePlay(H_THROW, C_THROW, REFERENCE_THROW, H_SCORE, C_SCORE):
    if H_THROW > C_THROW:
        H_SCORE += REFERENCE_THROW
        print("You win this round")
    elif H_THROW < C_THROW:
        C_SCORE += REFERENCE_THROW
        print("Computer wins this round")
    else:
        H_SCORE += REFERENCE_THROW / 2
        C_SCORE += REFERENCE_THROW / 2
        print("DRAW")
    return H_THROW, C_THROW, REFERENCE_THROW, H_SCORE, C_SCORE

def checkWinner():  
    rounds = 13
    H_SCORE = 0
    C_SCORE = 0
    REFERENCE_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    H_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    C_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    for i in range(rounds):
        H_THROW, C_THROW, REFERENCE_THROW, H_SCORE, C_SCORE = getThrow(H_DECK, C_DECK, REFERENCE_DECK, H_SCORE, C_SCORE)
        print("Updated Score: " + str(int(H_SCORE)) + " " + str(int(C_SCORE)))
        print("---------------------------------------------------")
        H_DECK.remove(H_THROW)
        C_DECK.remove(C_THROW)
        REFERENCE_DECK.remove(REFERENCE_THROW)
        rounds -= 1

checkWinner()