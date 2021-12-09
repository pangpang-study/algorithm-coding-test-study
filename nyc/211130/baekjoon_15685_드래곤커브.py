import sys


def get_path(d, g):
    path = [d]
    for _ in range(g):
        for i in range(len(path)-1, -1, -1):
            path.append((path[i] + 1) % 4)
    return path


def get_coord(x, y, path):
    coords = [(x, y)]
    for d in path:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= 101 or ny >= 101:
            return []
        coords.append((nx, ny))
        x, y = nx, ny
    return coords


def draw(coords, visited):
    for x, y in coords:
        visited[x][y] = True
    return visited


def count_square(visited):
    count = 0
    for i in range(len(visited)-1):
        for j in range(len(visited)-1):
            if visited[i][j] and visited[i][j+1] and visited[i+1][j] and visited[i+1][j+1]:
                count += 1
    return count


def solution():
    visited = [[False] * 101 for _ in range(101)]
    for y, x, d, g in curves:
        path = get_path(d, g)
        coords = get_coord(x, y, path)
        visited = draw(coords, visited)
    return count_square(visited)


if __name__ == "__main__":
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    N = int(sys.stdin.readline().rstrip())
    curves = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solution())
