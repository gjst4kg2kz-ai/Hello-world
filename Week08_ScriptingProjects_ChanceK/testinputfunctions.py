def inputInt(prompt):
    while True:
        userInput = input(prompt)
        if userInput.isdigit():
            return int(userInput)
        else:
            print("Error: please enter a valid integer.")


def inputFloat(prompt):
    while True:
        userInput = input(prompt)

        # Allow digits only OR digits with one decimal point
        if userInput.count(".") <= 1:
            temp = userInput.replace(".", "")
            if temp.isdigit() and userInput != ".":
                return float(userInput)

        print("Error: please enter a valid floating-point number.")


def main():
    value1 = inputInt("Enter an integer: ")
    print("You entered integer:", value1)

    value2 = inputFloat("Enter a floating-point number: ")
    print("You entered float:", value2)


if __name__ == "__main__":
    main()