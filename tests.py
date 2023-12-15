from statistics import mean
import timeit
import random

from generator import generate_board


def timer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        elapsed_time = (
            mean(timeit.repeat(lambda: func(*args, **kwargs), number=1, repeat=1))
            * 1000
        )

        print(f"{func.__name__} took {elapsed_time:.2f} ms to execute")
        return result

    return wrapper


@timer
def main():
    random.seed(1)
    size = 100
    print("Starting!")

    generate_board(size)
    print("Done!")


if __name__ == "__main__":
    main()
