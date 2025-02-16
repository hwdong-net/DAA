def solve_maze(maze, start, end):
    rows = len(maze)
    cols = len(maze[0]) if rows > 0 else 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []

    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0 and not visited[row][col]

    def backtrack(row, col):
        # 到达终点
        if (row, col) == end:
            path.append((row, col))
            return True
        # 标记当前位置已访问
        visited[row][col] = True
        path.append((row, col))
        # 尝试所有方向
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            if is_valid(new_row, new_col):
                if backtrack(new_row, new_col):
                    return True
                # 注意：此处不再需要 path.pop()，递归内部已处理回溯
        # 所有方向均失败，回溯
        visited[row][col] = False
        path.pop()
        return False

    # 从起点开始回溯
    if backtrack(start[0], start[1]):
        return path
    else:
        return []

# 测试示例
if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0]
    ]
    start = (0, 0)
    end = (4, 4)
    solution = solve_maze(maze, start, end)
    if solution:
        print("Path found:")
        for step in solution:
            print(f"→ ({step[0]}, {step[1]})", end=" ")
    else:
        print("No path exists.")
