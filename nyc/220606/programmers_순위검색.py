from bisect import bisect_left

lang = {"java": "1", "cpp": "2", "python": "3"}
job = {"backend": "1", "frontend": "2"}
year = {"junior": "1", "senior": "2"}
food = {"pizza": "1", "chicken": "2"}
info_dict = {}


def convert_string_to_code(dash, seq, string):
    if dash:
        if seq == 0:
            return ["1", "2", "3"]
        return ["1", "2"]
    if seq == 0:
        return [lang[string]]
    elif seq == 1:
        return [job[string]]
    elif seq == 2:
        return [year[string]]
    return [food[string]]


def solution(info, query):
    for i1 in ["1", "2", "3"]:
        for i2 in ["1", "2"]:
            for i3 in ["1", "2"]:
                for i4 in ["1", "2"]:
                    info_dict[i1+i2+i3+i4] = []
    for applicant in info:
        l, j, y, f, score = applicant.split()
        code = lang[l] + job[j] + year[y] + food[f]
        if code in info_dict:
            info_dict[code].append(int(score))

    for key, value in info_dict.items():
        value.sort()

    answer = []
    for q in query:
        l, j, y, tmp = q.split(" and ")
        f, score = tmp.split(" ")

        count = 0
        for i1 in convert_string_to_code(l == "-", 0, l):
            for i2 in convert_string_to_code(j == "-", 1, j):
                for i3 in convert_string_to_code(y == "-", 2, y):
                    for i4 in convert_string_to_code(f == "-", 3, f):
                        code = i1+i2+i3+i4
                        idx = bisect_left(info_dict[code], int(score))
                        count += (len(info_dict[code]) - idx)
        answer.append(count)
    return answer
