import sys

input = sys.stdin.readline

n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

#드래곤 커브들이 모일 배열 1이면 드래곤 커브의 일부
arr = [[0] * 101 for _ in range(101)]

for _ in range(n):
    #x, y: 드래곤 커브 시작점, d: 시작 방향, g: 세대
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1

    move = [d]
    #g세대 만큼 반복
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)

    #드래곤 커브에 해당하는 좌표 arr에 추가
    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = 1
        x, y = nx, ny

#모든 꼭짓점이 드래곤 커브의 일부인 정사각형 개수 구하기
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            ans += 1

print(ans)