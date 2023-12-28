import random
from typing import List, Tuple, Sequence, Any, TypeVar

SUITS = "♠ ♥ ♦ ♣".split()
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

Card = Tuple[str, str]  # tuple[str, str]
Deck = List[Card]  # list[tuple[str, str]

Choosable = TypeVar("Choosable")


def get_deck(shuffle: bool = False) -> Deck:
    """Get a new deck of 52 cards."""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck


def choose(items: Sequence[Choosable]) -> Choosable:
    """Choose and return random item."""
    return random.choice(items)


def player_order(names, start=None):
    """Rotate plyer order so that start goes first."""
    if start is None:
        start = choose(names)
    start_index = names.index(start)
    return names[start_index:] + names[:start_index]


def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return deck[0::4], deck[1::4], deck[2::4], deck[3::4]


def play() -> None:
    """Play a 4-player card game"""
    deck = get_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}

    for name, cards in hands.items():
        card_str = " ".join(f"{s}{r}" for (s, r) in cards)
        print(f"{name}: {card_str}")


if __name__ == "__main__":
    play()
