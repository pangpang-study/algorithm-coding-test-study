import sys
from collections import deque


def step1(a, robots):
    first_b = a.pop()
    a = a.appendleft(first_b)
    first_r = robots.pop()
    robots = robots.appendleft(first_r)
    return


def step2(a, robots):
    copy_robots = robots
    for i in range(n - 1):
        if robots[i]:
            if a[i + 1] != 0 and robots[i + 1] == False:
                copy_robots[i] = False
                copy_robots[i + 1] = True
                a[i + 1] -= 1
    robots = copy_robots
    return


def step3(a, robots):
    if a[0] != 0:
        robots[0] = True
        a[0] -= 1
    return


def step4(a, flag):
    if a.count(0) == k:
        flag = False 
    print(a)
    return flag


def solution(a, robots):
    total_step = 0
    flag = True
    while flag:
        step1(a, robots)
        step2(a, robots)
        for i in range(n, 2 * n):
            robots[i] = False
        step3(a, robots)
        flag = step4(a, flag)
        total_step += 1
    print(total_step)
    return


n, k = map(int, input().split())
a = deque(map(int, input().split()))
robots = deque([False] * 2 * n)

solution(a, robots)