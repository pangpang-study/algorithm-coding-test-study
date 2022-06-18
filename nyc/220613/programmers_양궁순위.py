import copy


def get_score(ryan, a_peach):
    score = 0
    for i in range(11):
        if ryan[i] > a_peach[i]:
            score += (10 - i)
        elif ryan[i] == a_peach[i] == 0:
            continue
        else:
            score -= (10 - i)
    return score


def backtrack(max_depth, depth, a_peach, ryan_cur, answer, score, start):
    if depth == max_depth:
        if (tmp := get_score(ryan_cur, a_peach)) > score:
            score = tmp
            answer = copy.deepcopy(ryan_cur)
        return answer, score

    for i in range(10 - (10 - start), -1, -1):
        ryan_cur[i] += 1
        answer, score = backtrack(max_depth, depth + 1, a_peach, ryan_cur, answer, score, i)
        ryan_cur[i] -= 1
    return answer, score


def solution(n, info):
    answer = []
    ryan_cur = [0] * 11

    answer, _ = backtrack(n, 0, info, ryan_cur, answer, 0, 10)
    if not answer:
        return [-1]
    return answer
  

# 반례 추천
# print(solution(10, [0, 0, 0, 0, 0, 0, 0, 3, 0, 4, 3]))
