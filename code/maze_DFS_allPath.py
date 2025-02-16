def find_paths(maze, x, y, path, visited, all_paths):
    rows, cols = len(maze), len(maze[0])
    
    # 检查是否越界或遇到障碍物或已经访问过
    if x < 0 or y < 0 or x >= rows or y >= cols or maze[x][y] == 1 or visited[x][y]:
        return
    
    # 记录当前路径
    path.append((x, y))
    
    # 如果到达终点，将路径存入结果列表
    if (x, y) == (rows - 1, cols - 1):
        all_paths.append(path[:])
        path.pop()
        return
    
    # 标记当前点为已访问
    visited[x][y] = True
    
    # 递归探索四个方向
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        find_paths(maze, x + dx, y + dy, path, visited, all_paths)
    
    # 回溯
    path.pop()
    visited[x][y] = False

def solve_maze(maze):
    if not maze or not maze[0]:
        return []
    
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    all_paths = []
    
    find_paths(maze, 0, 0, [], visited, all_paths)
    return all_paths

# 示例迷宫（0 表示可通行，1 表示障碍物）
maze = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
]

paths = solve_maze(maze)
print("所有可能的路径:")
for path in paths:
    print(path)
