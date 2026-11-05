# Assessment 3.2: Queue (FIFO) Implementation
# Name: CANONIGO, ALEXIS KENNETH (BSIT 2A)

from collections import deque


def main():
    # Step 1: Create an empty queue
    queue = deque()

    # Step 2: Enqueue C, A, N, O, N, I, G, O in that order
    letters = ['C', 'A', 'N', 'O', 'N', 'I', 'G', 'O']
    for letter in letters:
        queue.append(letter)

    # Step 3: Display the queue from front to rear
    print(" ".join(queue))

    # Step 4: While the queue is not empty, dequeue the front letter and display the remaining queue
    while len(queue) > 0:
        queue.popleft()  # Removes from the front (FIFO)
        if len(queue) > 0:
            print(" ".join(queue))
        else:
            print("Empty")


if __name__ == "__main__":
    main()