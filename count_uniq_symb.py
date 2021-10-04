import collections
from functools import lru_cache


def is_error(input_data):
    return isinstance(input_data, str) and len(input_data) <= 10


@lru_cache()
def unique_symbols(text):
    if not is_error(text):
        return False
    return len(collections.Counter(text))


if __name__ == '__main__':
    print(unique_symbols(input()))

