from random import randrange
# players = number of players, type = texas holdem= 2 or omaha = 4
def pokerHands (players, type):
    cards = ['2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣','A♣',
             '2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦','A♦',
             '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
             '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠']


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
