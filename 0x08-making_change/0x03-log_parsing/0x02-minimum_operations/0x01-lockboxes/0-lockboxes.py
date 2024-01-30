#!/usr/bin/python3
def canUnlockAll(boxes):
    # Set to store the indices of boxes that can be visited
    visited = set()

    # Queue for BFS traversal
    queue = [0]

    # Mark the first box as visited
    visited.add(0)

    while queue:
        current_box = queue.pop(0)

        # Check the keys in the current box
        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                # If the key corresponds to a valid box and the box is not visited, mark it as visited
                visited.add(key)
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)

# Example usage:
boxes1 = [[1], [2], [3], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 2], [3], [4], [], []]
print(canUnlockAll(boxes2))  # Output: False