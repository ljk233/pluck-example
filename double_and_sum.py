# double_and_sum.py


def double_and_sum():
    data = [1, 2, 3, 4, 5]
    print("data =", data)

    doubled = [2 * x for x in data]
    print("doubled =", doubled)

    total = sum(doubled)
    print("total =", total)


if __name__ == "__main__":
    double_and_sum()
