import sys


def dfs(start, visited):
    path = {start}
    stack = [start]
    visited.add(start)
    while stack:
        nxt = selected[stack[-1]]
        if nxt in path:
            while stack:
                top = stack.pop()
                path.remove(top)
                if top == nxt:
                    break
            break
        if nxt in visited:
            break
        path.add(nxt)
        stack.append(nxt)
        visited.add(nxt)
    return len(path)


def solution(n):
    answer = 0
    visited = set()
    for i in range(1, n+1):
        if i in visited:
            continue
        answer += dfs(i, visited)
    return answer


if __name__ == "__main__":
    # res = []
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        selected = [0] + list(map(int, sys.stdin.readline().split()))
        print(solution(N))
        # res.append(solution(N))
    # sys.stdout.write('\n'.join(map(str, res)))
