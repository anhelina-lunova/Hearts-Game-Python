# HomeWork 1
"""
Task #1
Написати функцію яка приймає рядок і повертає словник у якому:
   - ключами є всі символи, які зустрічаються в цьому рядку,
   а значення - відповідні вірогідності зустріти цей символ в цьому рядку.
   - Код повинен бути структурований за допомогою конструкції if name == "main":,
   - всі аргументи і значення що функція повертає повинні бути типізовані,
   - функція має рядок документації
"""


def symbol_probability(text: str) -> dict[str, float]:
    """
    Calculates the probability of each symbol occurring in a given string.

    Args:
        text: The string to analyze.

    Returns:
        A dictionary where keys are symbols in the string and values are their corresponding probabilities.
    """

    symbol_counts = {}
    total_symbols = len(text)

    for symbol in text:
        symbol_counts[symbol] = round((text.count(symbol) / total_symbols) * 100, 2)

    return symbol_counts


if __name__ == "__main__":
    #
    text = input("Enter your text to calculate the probability of encountering a character in it: ")
    symbol_probs = symbol_probability(text)

    for k, v in symbol_probs.items():
        print(k, '-->', v, '%')
