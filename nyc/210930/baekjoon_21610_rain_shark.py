import sys


def init_cloud(n):
    return [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]


def move_cloud(clouds, n, direction, distance):
    distance %= n
    new_cloud = []
    for cx, cy in clouds:
        nx = cx + dx[direction]*distance
        ny = cy + dy[direction]*distance
        if nx < 0:
            nx += n
        elif nx >= n:
            nx -= n
        if ny < 0:
            ny += n
        elif ny >= n:
            ny -= n
        new_cloud.append([nx, ny])
    return new_cloud


def make_it_rain(clouds):
    for cx, cy in clouds:
        board[cx][cy] += 1


def is_water(x, y):
    return True if board[x][y] > 0 else False


def copy_water(clouds, n):
    for cx, cy in clouds:
        for i in range(2, 9, 2):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                board[cx][cy] += 1 if is_water(nx, ny) else 0


def make_cloud(clouds, n):
    new_cloud = []
    cloud_set = set(map(tuple, clouds))
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in cloud_set:
                new_cloud.append([i, j])
                board[i][j] -= 2
    return new_cloud


def solution(n):
    # 1. 초기 상태
    clouds = init_cloud(n)
    commands.reverse()
    while commands:
        di, si = commands.pop()
        # 2. 구름 이동
        clouds = move_cloud(clouds, n, di, si)
        # 3. 비내리기
        make_it_rain(clouds)
        # 4. 물복사 버그
        copy_water(clouds, n)
        # 5. 한 턴 끝남. 새로운 구름 생성
        clouds = make_cloud(clouds, n)
    return sum(sum(board, []))


if __name__ == "__main__":
    dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

    N, M = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    commands = []
    for _ in range(M):
        commands.append(list(map(int, sys.stdin.readline().split())))
    print(solution(N))
