import random
import sys
from colorama import Fore, Style, Back  # import for colored output
import os
import time
from game_description import game_caption, game_desc  # import game descriptions

# color definitions
fore_color_yellow_bright = Fore.YELLOW + Style.BRIGHT
fore_color_yellow = Fore.YELLOW
fore_color_black_bright = Fore.BLACK + Style.BRIGHT
fore_color_red_bright = Fore.RED + Style.BRIGHT
back_color_white = Back.WHITE


def typewriter(message, time_, colorama_opt):
    for char in message:
        # Apply desired color before writing the character
        sys.stdout.write(colorama_opt + char)  # Example: Red color
        sys.stdout.flush()
        time.sleep(time_)

    # Reset color after the message
    sys.stdout.write(Style.RESET_ALL)  # Reset back to default style
    time.sleep(1)
    os.system("clear")


class Card:
    SUITS = "♠ ♥ ♦ ♣".split()
    RANKS = [
        "2 ",
        "3 ",
        "4 ",
        "5 ",
        "6 ",
        "7 ",
        "8 ",
        "9 ",
        "10",
        "J ",
        "Q ",
        "K ",
        "A ",
    ]

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        suit_color = {
            "♠": fore_color_black_bright,
            "♥": fore_color_red_bright,
            "♦": fore_color_red_bright,
            "♣": fore_color_black_bright,
        }
        return f"{suit_color[self.suit]}{self.suit}{self.rank}{Style.RESET_ALL}"

    @property
    def value(self) -> int:
        """The value of a card is rank a number."""
        return self.RANKS.index(self.rank)

    @property
    def points(self) -> int:
        """Points this cart is worth."""
        if self.suit == "♠" and self.rank == "Q":
            return 13
        if self.suit == "♥":
            return 1
        return 0

    def __eq__(self, other: "Card") -> bool:
        if not isinstance(other, Card):
            raise TypeError("Comparison only allowed between Card objects.")
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other: "Card") -> bool:
        if not isinstance(other, Card):
            raise TypeError("Comparison only allowed between Card objects.")
        return self.value < other.value


class Deck:
    def __init__(self, cards):
        self.cards = cards

    @classmethod
    def create(cls, shuffle=False):
        """Create a new deck of 52 cards"""
        cards = [Card(s, r) for r in Card.RANKS for s in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)

    def deal(self, num_hands: int):
        """Deal the cards in the deck into num_hands."""
        cls = self.__class__
        return tuple(cls(self.cards[i::num_hands]) for i in range(num_hands))


class Player:
    def __init__(self, name: str, hand: Deck) -> None:
        self.name = name
        self.hand = hand

    def play_card(self) -> Card:
        """Play a card from the player's hand."""
        card = random.choice(self.hand.cards)
        print(back_color_white, end="")
        self.hand.cards.remove(card)
        name_color = fore_color_yellow
        print(f"{name_color}{self.name}:{card!r:<3}", end="")


class Game:
    def __init__(self, *names: str) -> None:
        deck = Deck.create(shuffle=True)
        self.names = (
            (list(names) + "P1 P2 P3 P4".split())[:4]
            if names
            else "P1 P2 P3 P4".split()[:4]
        )
        self.hands = {n: Player(n, h) for n, h in zip(self.names, deck.deal(4))}

    def player_order(self, start=None):
        if start is None:
            start = random.choice(self.names)
        start_idx = self.names.index(start)
        return self.names[start_idx:] + self.names[:start_idx]

    def play(self) -> None:
        """Play a card game."""

        typewriter(game_caption, 0.01, fore_color_red_bright)
        typewriter(game_desc, 0.01, fore_color_yellow_bright)

        start_player = random.choice(self.names)
        turn_order = self.player_order(start=start_player)

        while self.hands[start_player].hand.cards:
            for name in turn_order:
                self.hands[name].play_card()
            print()


if __name__ == "__main__":
    player_names = sys.argv[1:]
    game = Game(*player_names)
    game.play()
