# ID# 3130873
# Lab 8
fancy_unicode_suits = {"C": "♣", "D": "♦", "H": "♥", "S": "♠"}
values = "23456789TJQKA"
suits = "CDHS"
import random

class Card:
    """
    A class representing a standard playing card.

    Parameter:
        value: The card's face value, which can be '2' to 'A'.
        suit : The card's suit, which can be 'C' for Clubs, 'D' for Diamonds, 'H' for Hearts, or 'S' for Spades.

    Methods:
        __init__(self, value, suit): Initializes a new Card instance with the specified value and suit.
        __str__(self): Returns a string representation of the card, including its value and suit.
        __repr__(self): Returns a string representation of the card, including its value and suit.
        __gt__(self, other): Compares the card's value and suit to another card and returns True if greater.
        __lt__(self, other): Compares the card's value and suit to another card and returns True if smaller.
        __eq__(self, other): Checks if the card has the same value and suit as another card.
        __ne__(self, other): Checks if the card is not equal to another card.
        __ge__(self, other): Checks if the card is greater than or equal to another card.
        __le__(self, other): Checks if the card is smaller than or equal to another card.
    """

    def __init__(self, value, suit):
        """
        Initialize a new Card instance with the specified value and suit.

        Parameters:
            value: The face value of the card ('2' to 'A').
            suit: The suit of the card ('C' for Clubs, 'D' for Diamonds, 'H' for Hearts, 'S' for Spades).
        """

        self.value = value
        self.suit = suit

    def __str__(self):
        """
        Return a string representation of the card, including its value and suit.

        Returns:
            A string representing the card, e.g., '2C' for 2 of Clubs.
        """

        return f"{self.value}{self.suit}"

    def __repr__(self):
        """
        Return a string representation of the card, including its value and suit.

        Returns:
            A string representing the card, e.g., '2C' for 2 of Clubs.
        """

        return self.__str__()

    def __gt__(self, other):
        """
        Compare the card's value and suit to another card and return True if the card is greater.

        Parameters:
            other: Another Card object to compare.

        Returns:
            bool: True if the card is greater than the other card, based on value and suit.
        """

        values_order = '23456789TJQKA'
        suits_order = 'CDHS'

        if self.value == other.value:
            return suits_order.index(self.suit) > suits_order.index(other.suit)
        else:
            return values_order.index(self.value) > values_order.index(other.value)

    def __lt__(self, other):
        """
        Compare the card's value and suit to another card and return True if the card is smaller.

        Parameters:
            other: Another Card object to compare.

        Returns:
            bool: True if the card is smaller than the other card, based on value and suit.
        """

        values_order = '23456789TJQKA'
        suits_order = 'CDHS'

        if self.value == other.value:
            return suits_order.index(self.suit) < suits_order.index(other.suit)
        else:
            return values_order.index(self.value) < values_order.index(other.value)

    def __eq__(self, other):
        """
        Check if the card has the same value and suit as another card.

        Parameters:
            other: Another Card object to compare.

        Returns:
            bool: True if the card has the same value and suit as the other card.
        """

        return self.value == other.value and self.suit == other.suit

    def __ne__(self, other):
        """
        Check if the card is not equal to another card.

        Parameters:
            other: Another Card object to compare.

        Returns:
            bool: True if the card is not equal to the other card.
        """

        return not self.__eq__(other)

    def __ge__(self, other):
        """
        Check if the card is greater than or equal to another card.

        Parameters:
            other: Another Card object to compare.

        Returns:
            bool: True if the card is greater than or equal to the other card.
        """

        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other):
        """
        Check if the card is smaller than or equal to another card.

        Parameters:
            other: Another Card object to compare.

        Returns:
            bool: True if the card is smaller than or equal to the other card.
        """

        return self.__lt__(other) or self.__eq__(other)


class Deck:
    def draw(self):
        """
    A class representing a deck of playing cards.

    Attributes:
        cards (list): A list of Card objects representing the deck.

    Methods:
        __init__(self): Initializes a new Deck instance with a shuffled list of Card objects.
        __len__(self): Returns the number of cards left in the deck.
        __str__(self): Returns a string representation of the deck.
        draw(self): Draws a single card from the top of the deck, removing it from the deck.
    """

    def __init__(self):
        """
        Initialize a new Deck instance with a shuffled list of Card objects.
        """

        values = '23456789TJQKA'
        suits = 'CDHS'
        self.cards = [Card(value, suit) for value in values for suit in suits]
        random.shuffle(self.cards)

    def __len__(self):
        """
        Returns the number of cards left in the deck.

        Returns:
            int: The number of cards remaining in the deck.
        """

        return len(self.cards)

    def __str__(self):
        """
        Returns a string representation of the deck.

        Returns:
            str: A string representing the deck with each card separated by a space.
        """

        return ' '.join(str(card) for card in self.cards)

    def draw(self):
        """
        Draws a single card from the top of the deck, removing it from the deck.

        Returns:
            Card: The card drawn from the deck.
        """

        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return None


def print_header(details, symbol="="):
    """
    Purpose: prints out a header wrapped with symbol chars on each side
    Parameters:
    details: str the text that appears in the header
    symbol:  str the symbol that surrounts the text
    Returns: None
    """
    print(f" {details} ".center(80, symbol))
    print()


def compare_identical(card1: Card, card2: Card):
    """Purpose: Compares identical cards
        Uses the assert statement to raise an error if any of the following comparisons are not as expected.
    Parameters:
        card1 - a Card class object
        card2 - a Card class object, identical to card1
    Returns: None
    """
    print(f"Card 1: {repr(card1)} Card 2: {repr(card2)}")
    print(f"{card1} vs {card2}")
    assert card2 >= card1
    assert card1 <= card2
    assert card1 == card2
    assert not card1 != card2
    print("-" * 25)


def compare_left_smaller_than_right(smaller_card: Card, bigger_card: Card):
    """Purpose: Compares smaller_card to bigger_card
        Uses the assert statement to raise an error if any of the following comparision are not as expected.
        bigger_card is always expected to be bigger than smaller card.
        The two cards are not expected to be equal.
    Parameters:
        smaller_card - a Card class object of lower value/suit than bigger_card
        bigger_card - a Card class object of higher value/suit than smaller_card
    Returns: None
    """
    print(f"Card 1: {repr(smaller_card)} Card 2: {repr(bigger_card)}")
    print(f"{smaller_card} vs {bigger_card}")
    assert isinstance(smaller_card, Card)
    assert isinstance(bigger_card, Card)
    assert smaller_card < bigger_card
    assert bigger_card > smaller_card
    assert bigger_card >= smaller_card
    assert smaller_card <= bigger_card
    assert smaller_card != bigger_card
    assert not smaller_card == bigger_card
    print("-" * 25)


class ShouldntBeHere(Exception):
    pass


if __name__ == "__main__":
    print_header("Testing Identical Cards")
    for value in values:
        card_1 = Card(value, suits[values.index(value) % 4])
        card_2 = Card(value, suits[values.index(value) % 4])
        compare_identical(card_1, card_2)
    print_header("Done testing identical cards!", "-")

    print_header("Testing Value Functions")
    for value in values[:-1]:
        card_1 = Card(value, "C")
        card_2 = Card(values[values.index(value) + 1], "C")
        compare_left_smaller_than_right(card_1, card_2)
    print_header("Done testing values!", "-")

    print_header("Testing Suit Comparisons!")
    for value in values:
        for i, suit in enumerate(suits):
            card_1 = Card(value, suit)
            card_2 = Card(value, suits[(i + 1) % len(suits)])
            if i == 3:
                compare_left_smaller_than_right(card_2, card_1)
            else:
                compare_left_smaller_than_right(card_1, card_2)
    print_header("Done testing suits!", "-")

    print_header("Testing Deck Functions")
    test_deck = Deck()
    for i in range(1, 53):
        print(test_deck)
        card = test_deck.draw()
        print(f"drew: {card}")
        assert isinstance(card, Card)
        print(f"{len(test_deck)} cards left")
        assert len(test_deck) == 52 - i
        print("-" * 35)
    print(test_deck)

    try:
        test_deck.draw()
        raise ShouldntBeHere("RuhRoh, you should raise an error when the deck is empty")
    except ValueError:
        print("Tried to draw, deck was empty! Good work!")

    print_header("Done testing CONGRATULATIONS!", "-")
