import sys
from itertools import permutations


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    best = 0
    innings = []
    for _ in range(N):
        innings.append(list(map(int, sys.stdin.readline().split())))

    for order in permutations(range(1, 9), 8):
        score, player_idx = 0, 0
        lineup = order[:3] + (0,) + order[3:]
        for inning in innings:
            out, base = 0, 0
            while out < 3:
                if inning[lineup[player_idx]] != 0:
                    base = (base << inning[lineup[player_idx]]) | (1 << inning[lineup[player_idx]] - 1)
                    score += (base >> 3 & 1) + (base >> 4 & 1) + (base >> 5 & 1) + (base >> 6 & 1)
                    # for s in range(3, 7):  -> 포문이 많이 느린가. 시간초과 발생코드
                    #     score += (base >> s) & 1
                    base &= 7
                else:
                    out += 1
                player_idx = (player_idx + 1) % 9
        best = max(best, score)
    print(best)
