# Assessment 3.2: Stack (LIFO) Implementation
# Name: CANONIGO, ALEXIS KENNETH (BSIT 2A)

def main():
    # Step 1: Create an empty stack
    stack = []

    # Step 2: Push C, A, N, O, N, I, G, O onto the stack in that order
    letters = ['C', 'A', 'N', 'O', 'N', 'I', 'G', 'O']
    for letter in letters:
        stack.append(letter)

    # Step 3: Display the stack from bottom to top
    print(" ".join(stack))

    # Step 4: While the stack is not empty, pop the top letter and display the remaining stack
    while len(stack) > 0:
        stack.pop()
        if len(stack) > 0:
            print(" ".join(stack))
        else:
            print("Empty")


if __name__ == "__main__":
    main()