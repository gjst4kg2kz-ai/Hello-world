def isSorted(items):

    if len(items) < 2:
        return True

    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False

    return True


def main():
    test_lists = [
        [],
        [5],
        [1, 2, 2, 3, 4],
        [3, 1, 2],
        [10, 20, 30],
        [5, 4, 3]
    ]

    for lst in test_lists:
        print(f"{lst} -> {isSorted(lst)}")


if __name__ == "__main__":
    main()