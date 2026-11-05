# Assessment 3.2: Array Implementation
# Name: CANONIGO, ALEXIS KENNETH (BSIT 2A)

def main():
    # Step 1: Create an empty array
    arr = []

    # Step 2: Add the letters C, A, N, O, N, I, G, O to the array
    letters = ['C', 'A', 'N', 'O', 'N', 'I', 'G', 'O']
    for letter in letters:
        arr.append(letter)

    # Step 3: Display the array
    print(" ".join(arr))

    # Step 4: While the array is not empty, remove the last letter and display the remaining array
    while len(arr) > 0:
        arr.pop()
        if len(arr) > 0:
            print(" ".join(arr))
        else:
            print("Empty")


if __name__ == "__main__":
    main()