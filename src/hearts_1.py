import random
from typing import List, Tuple, Sequence, TypeVar, Optional

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


def player_order(names: List[str], start: Optional[str] = None) -> List[str]:
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
    deck = get_deck(shuffle=True)  # роздали колоду
    names = "P1 P2 P3 P4".split()  # сформували імена гравців
    hands: dict[str, Deck] = {
        n: h for n, h in zip(names, deal_hands(deck))
    }  # здали карти на руки
    start_player = choose(
        names
    )  # get a name of player who will go first (випадково визначили імʼя першого гравця)
    turn_order = player_order(
        names, start=start_player
    )  # сформували чергу від першого гравця і далі

    while hands[start_player]:  # до моменту поки у першого гравця не закінчаться карти
        for name in turn_order:
            card = choose(
                hands[name]
            )  # поки в нього є карти ми випадково беремо карту для того, чий зараз хід
            hands[name].remove(
                card
            )  # він взяв її, ми видаляємо карту щоб гравець знову її не взяв
            print(f"{name}: {card[0] + card[1]:<3} ", end="")  # і після цього друкуємо
        print()

    # for name, cards in hands.items():
    #     card_str = " ".join(f"{s}{r}" for (s, r) in cards)
    #     print(f"{name}: {card_str}")


if __name__ == "__main__":
    play()
