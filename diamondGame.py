import random

H_SCORE = 0
C_SCORE = 0

REFERENCE_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
H_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
C_DECK = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def getThrow(H_DECK, C_DECK, REFERENCE_DECK):
    
    REFERENCE_CARD = random.choice(REFERENCE_DECK)
    H_THROW = int(input("Enter your Bid :- "))
    C_THROW = random.choice(C_DECK)
    
    winnerOfBid(H_THROW, C_THROW, REFERENCE_THROW)
    
def round(H_THROW, C_THROW, REFERENCE_THROW):
    if H_THROW > C_THROW:
        H_SCORE += REFERENCE_THROW
    if H_THROW < C_THROW:
        C_SCORE += REFERENCE_THROW
    if H_THROW = C_THROW:
        H_SCORE += REFERENCE_THROW / 2
        C_SCORE += REFERENCE_THROW / 2

    H_DECK.remove(H_THROW)
    C_DECK.remove(C_THROW)
    REFERENCE_DECK.remove(REFERENCE_THROW)
    return H_DECK, C_DECK, REFERENCE_DECK
    

    
getThrow(H_DECK, C_DECK, REFERENCE_DECK):  



