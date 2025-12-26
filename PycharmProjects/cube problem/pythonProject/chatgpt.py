from collections import deque


# Function to apply the transformation based on the chosen square
def transform(square, choice):
    a, b, c, d = square
    if choice == 'a':
        return [a, d, b, c]
    elif choice == 'b':
        return [d, b, a, c]
    elif choice == 'c':
        return [b, d, c, a]
    elif choice == 'd':
        return [b, c, a, d]


# Function to find the sequence of moves to reach the target state
def find_transformation_sequence(start, target):
    # Queue for BFS
    queue = deque([(start, [])])
    visited = set()
    visited.add(tuple(start))

    while queue:
        current, moves = queue.popleft()

        # Check if we've reached the target
        if current == target:
            return len(moves), moves

        # Try all possible moves
        for choice in ['a', 'b', 'c', 'd']:
            next_state = transform(current, choice)
            if tuple(next_state) not in visited:
                visited.add(tuple(next_state))
                queue.append((next_state, moves + [choice]))

    return -1, []  # If no solution is found


# Input configuration
initial_square = ['a', 'b', 'c', 'd']  # Starting configuration

raw_target_square = input('Configuration desired: ')

target_square = list(raw_target_square)  # Desired configuration

# Find the sequence of moves
num_moves, move_sequence = find_transformation_sequence(initial_square, target_square)

print(f'Takes {num_moves} moves')
print(move_sequence)
