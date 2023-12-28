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


"""
Task #2
За допомогою тернарного оператора релізувати логіку:
    - є параметри x та у,
    - якщо x < y - друкуємо x + y,
    - якщо x == y - друкуємо 0,
    - якщо x > y - друкуємо x - y,
    - якщо x == 0 та y == 0 друкуємо "game over"
"""


def return_ternary(x, y):
    """
    Created for fun
    """
    return (
        "game over"
        if (x == 0 and y == 0)
        else (x - y)
        if (x > y)
        else 0
        if x == y
        else x + y
    )


if __name__ == "__main__":
    # Task #1
    print("""
Task #1
    Написати функцію яка приймає рядок і повертає словник у якому:
       - ключами є всі символи, які зустрічаються в цьому рядку,
       а значення - відповідні вірогідності зустріти цей символ в цьому рядку.
       - Код повинен бути структурований за допомогою конструкції if name == "main":,
       - всі аргументи і значення що функція повертає повинні бути типізовані,
       - функція має рядок документації
    """)
    text = input("Enter your text to calculate the probability of encountering a character in it: ")
    symbol_probs = symbol_probability(text)

    for k, v in symbol_probs.items():
        print(k, '-->', v, '%')

    # Task #2
    print("""
Task #2
    За допомогою тернарного оператора релізувати логіку:
        - є параметри x та у,
        - якщо x < y - друкуємо x + y,
        - якщо x == y - друкуємо 0,
        - якщо x > y - друкуємо x - y,
        - якщо x == 0 та y == 0 друкуємо 'game over'
    """)
    return_list = ((1, 2), (4, 4), (5, 3), (0, 0))

    for i in return_list:
        print(f" x = {i[0]}, y = {i[1]}. Result: {return_ternary(i[0], i[1])}")
