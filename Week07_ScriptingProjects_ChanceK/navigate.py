# navigate.py

def main():
    # Prompt the user for a filename
    filename = input("Enter the filename: ")
    
    try:
        # Read all lines from the file into a list
        with open(filename, "r") as file:
            lines = file.readlines()
            
        # Strip newline characters from each line
        lines = [line.rstrip("\n") for line in lines]

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return

    # Inform the user about the number of lines
    print(f"The file has {len(lines)} lines.")

    while True:
        # Prompt the user for a line number
        try:
            line_num = int(input(f"Enter a line number (1-{len(lines)}), or 0 to quit: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if line_num == 0:
            print("Exiting program.")
            break
        elif 1 <= line_num <= len(lines):
            # Print the requested line
            print(f"Line {line_num}: {lines[line_num - 1]}")
        else:
            print(f"Invalid line number. Please enter a number between 1 and {len(lines)}.")

if __name__ == "__main__":
    main()