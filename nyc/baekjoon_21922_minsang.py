import sys


def find_aircon(n, m):
    aircons = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 9:
                aircons.append([i, j])
    return aircons


def change_direction(cur_dir, stuff):
    return direction_mapped[stuff][cur_dir]


def search(x, y, direc, visited, n, m):
    while True:
        nx = x + dx[direc]
        ny = y + dy[direc]
        # 보드 밖으로 나가면
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        # 이미 지나갔던 경로면
        if visited[direc][nx][ny]:
            break
        visited[direc][nx][ny] = True
        direc = change_direction(direc, board[nx][ny])
        if direc == -1:
            break
        x, y = nx, ny


def solution(n, m):
    # 1. 에어컨 위치 받기
    aircons = find_aircon(n, m)
    # visited 를 방향도 포함시켜서 이미 지나간 경로면 안가게 해줌 -> 시간 단축
    visited = [[[False] * m for _ in range(n)] for _ in range(4)]

    for air_x, air_y in aircons:
        if air_x < 0 and air_y < 0:
            continue
        # 2. 4방향 탐색
        for i in range(4):
            visited[i][air_x][air_y] = True
            search(air_x, air_y, i, visited, n, m)
    # 3. 결과 탐색

    count = 0
    for i in range(n):
        for j in range(m):
            if visited[0][i][j] or visited[1][i][j] or visited[2][i][j] or visited[3][i][j]:
                count += 1
    return count


if __name__ == "__main__":
    # 전역 변수 세팅
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    direction_mapped = {
        0: {0: 0, 1: 1, 2: 2, 3: 3},
        1: {0: 0, 1: -1, 2: 2, 3: -1},
        2: {0: -1, 1: 1, 2: -1, 3: 3},
        3: {0: 1, 1: 0, 2: 3, 3: 2},
        4: {0: 3, 1: 2, 2: 1, 3: 0},
        9: {0: 0, 1: 1, 2: 2, 3: 3},
    }
    # 입력 받기
    N, M = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    # 프로그래머스처럼 풀기
    print(solution(N, M))
