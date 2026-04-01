def main():
    filename = input("Enter the file name: ")

    with open(filename, "r") as file:
        numbers = list(map(float, file.read().split()))

    total = sum(numbers)
    count = len(numbers)

    if count == 0:
        print("The file contains no numbers.")
    else:
        average = total / count
        print("Average:", average)


if __name__ == "__main__":
    main()