"""Examples of one_dimensional_minimzer.

Attempts to find the index of a minimum value in a list of integers.
"""

import random

from rothko.anneal import one_dimensional_minimizer


def simple_example():
    hills = [5, 4, 3, 2, 0, -1, 3, 4, -2]
    print(f"Input list is {hills}")

    s = one_dimensional_minimizer(hills)
    print(
        f"Got results {s}, which is {'correct' if s == 8 else 'incorrect'}."
    )


def medium_example():
    hill_size = 100
    hills = list(range(hill_size))
    random.shuffle(hills)
    print(f"Input list is {hills}")

    correct_s = hills.index(0)
    s = one_dimensional_minimizer(hills)

    print(
        f"Got results {s}, which is {'correct' if s == correct_s else 'incorrect'}."
    )


if __name__ == "__main__":
    print("Simple Test")
    simple_example()

    print("\nMedium Test")
    medium_example()
