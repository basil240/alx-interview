def canUnlockAll(boxes):
    n = len(boxes)  # Total number of boxes
    visited = [False] * n  # Initialize visited list

    # Mark the first box as visited since it's unlocked initially
    visited[0] = True

    # Create a stack to perform DFS
    stack = [0]

    # Perform DFS to check if all boxes can be opened
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)

# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Should return True
