# робота над помилками

def get_symbols_frequency(text):
    result_dict = {}
    text_len = len(text)
    for symbol in set(text):
        result_dict[symbol] = round((text.count(symbol) / text_len), 2)
    return result_dict


def get_ternary(x, y):
    return str(
        x + y if (x < y) else
        x - y if (x > y) else
        "game over" if (x == 0 and y == 0) else
        0
    )


if __name__ == '__main__':
    # get_ternary
    cases = (
        (1, 2, "3"),
        (3, 3, "0"),
        (5, 3, "2"),
        (0, 0, "game over"),
    )

    for x, y, result in cases:
        func_res = get_ternary(x, y)
        assert func_res == result, f"ERROR: get_ternary({x}, {y}) returned {func_res}, but expected {result}"

    # get_symbols_frequency
    print(get_symbols_frequency("q ww eee rrrr ttttt yyyyyy"))

    # print(id(get_symbols_frequency))
    # print(id(get_ternary))
