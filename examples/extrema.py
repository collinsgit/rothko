"""Examples of extrema finding.

Attempts to find the index of a minimum value in a list of n-dimensional array
of integers.

Note that, for the most part, the data we are giving doesn't have any pattern. This
is especially true with the 1d examples where we use a fully random neighbor function.
In these cases, finding the minimum is mostly luck. In the 2d example, there is some
locality, but our neighbor function only visits adjacent states, such that we easily
get stuck in local minima.
"""

import random

from rothko.applications.extrema import (
    n_dimensional_minimizer,
    one_dimensional_minimizer,
)


def _print_results(s, correct_s):
    print(f"Got results {s}, which is {'correct' if s == correct_s else 'incorrect'}.")


def simple_one_dimensional_example():
    hills = [5, 4, 3, 2, 0, -1, 3, 4, -2]
    print(f"Input list is {hills}")

    s = one_dimensional_minimizer(hills)
    _print_results(s, 8)


def medium_one_dimensional_example():
    hill_size = 100
    hills = list(range(hill_size))
    random.shuffle(hills)
    print(f"Input list is {hills}")

    correct_s = hills.index(0)
    s = one_dimensional_minimizer(hills)
    _print_results(s, correct_s)


def two_dimensional_example():
    height, width = 5, 10
    hills = list(range(height * width))
    split_point = random.randint(1, len(hills))
    hills = hills[split_point:] + hills[:split_point]
    min_index = hills.index(0)
    hills = [hills[i : i + width] for i in range(0, len(hills), width)]
    print(f"Input array is {hills}")

    correct_s = [min_index // width, min_index % width]
    s = n_dimensional_minimizer(hills)
    _print_results(s, correct_s)


if __name__ == "__main__":
    print("Simple Test")
    simple_one_dimensional_example()

    print("\nMedium Test")
    medium_one_dimensional_example()

    print("\n2d Test")
    two_dimensional_example()
