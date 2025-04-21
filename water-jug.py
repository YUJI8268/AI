from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    queue = deque()
    visited = set()

    # Initial state (0, 0)
    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()
        print(f"Current state: ({jug1}, {jug2})")

        # Check if we have reached the target
        if jug1 == target or jug2 == target:
            print(f"Solution found: ({jug1}, {jug2})")
            return

        # Generate all possible next states
        possible_states = [
            (jug1_capacity, jug2),  # Fill Jug1
            (jug1, jug2_capacity),  # Fill Jug2
            (0, jug2),              # Empty Jug1
            (jug1, 0),              # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No solution found.")

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_problem(jug1_capacity, jug2_capacity, target)

