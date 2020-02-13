from random import randrange
# players = number of players, type = texas holdem= 2 or omaha = 4
def pokerHands (players, type):
    cards = ['2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC',
             '2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD',
             '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
             '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']


    for i in range (0,players):
        playerCards = []
        for j  in range (0, type):
            numOfCards = len(cards)
            randomCardIndex = randrange(numOfCards)
            playerCards.append(cards[randomCardIndex])
            cards.remove(cards[randomCardIndex])
        print (playerCards)

#     print the 5 cards on the table
    playerCards = []
    for i in range(0,5):
        numOfCards = len(cards)
        randomCardIndex = randrange(numOfCards)
        playerCards.append(cards[randomCardIndex])
        cards.remove(cards[randomCardIndex])
    print(playerCards)

if __name__ == '__main__':
    pokerHands(9,2)
