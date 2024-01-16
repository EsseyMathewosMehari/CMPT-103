# ID# 3130873
# Lab 4
from random import shuffle

def make_deck():
    """
    Create a deck of cards, shuffled.

    Returns:
    list: A shuffled list of 52 cards.
    """
    deck = []
    for suit in "SHDC":
        for value in "23456789TJQKA":
            deck.append(value + suit)

    shuffle(deck)
    return deck

def calculate_hand_value(hand):
    """
    Calculate the value of a single hand in blackjack.

    Parameters:
    hand: A list of cards representing a player's hand.

    Returns:
    int: The total value of the hand based on blackjack rules.
    """
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}
    hand_value = 0
    num_aces = 0

    for card in hand:
        value = card[0]
        hand_value += values[value]

        if value == 'A':
            num_aces += 1

    while num_aces > 0 and hand_value <= 11:
        hand_value += 10
        num_aces -= 1

    return hand_value

def deal_blackjack(deck, number_of_players):
    """
    Deal two cards for each player from the top of a provided deck.

    Parameters:
    deck: A list of cards representing a shuffled deck.
    number_of_players: The number of players to deal hands to.

    Returns:
    list A list of player hands, where each hand is represented as a list of cards.
    """
    hands = []
    for _ in range(number_of_players):
        hand = [deck.pop(0), deck.pop(0)]
        hands.append(hand)
    return hands

def print_blackjack(hands):
    """
    Print out the starting hands of cards vertically.

    Parameters:
    hands: A list of player hands, where each hand is represented as a list of cards.

    This function prints each player's hand vertically.
    """
    for i in range(len(hands[0])):
        for hand in hands:
            print(hand[i], end='\t')
        print()

def show_winner(hands):
    """
    Print out the hands and mark the winner(s) with an asterisk (*).

    Parameters:
    hands: A list of player hands, where each hand is represented as a list of cards.

    This function prints each player's hand vertically and marks the winner(s) with an asterisk (*).
    """
    max_value = max([calculate_hand_value(hand) for hand in hands])
    winners = [i for i, hand in enumerate(hands) if calculate_hand_value(hand) == max_value]

    for i in range(len(hands[0])):
        for j, hand in enumerate(hands):
            winner_marker = '*' if j in winners else ''
            print(hand[i] + winner_marker, end='\t')
        print()

def play():
    """
    Demonstrates the blackjack program by creating and shuffling the deck, dealing 5 hands,
    printing out the 5 hands, and printing out the winners for each hand.
    """
    # Create and shuffle the deck
    deck = make_deck()

    # Deal 5 hands
    number_of_players = 5
    hands = deal_blackjack(deck, number_of_players)

    # Print out the 5 hands
    print("Hands:")
    print_blackjack(hands)

    # Print out the winners for each hand
    print("\nWinners:")
    show_winner(hands)

if __name__ == '__main__':
    play()