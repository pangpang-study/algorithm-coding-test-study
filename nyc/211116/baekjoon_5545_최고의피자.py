import sys


def solution(dough_price, topping_price, dough_kal):
    topping_kal.sort(reverse=True)
    total_kal = dough_kal
    total_price = dough_price
    rate = total_kal / total_price
    for each_kal in topping_kal:
        total_kal += each_kal
        total_price += topping_price
        if rate > total_kal / total_price:
            break
        rate = total_kal / total_price
    return int(rate)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    A, B = map(int, sys.stdin.readline().split())
    C = int(sys.stdin.readline().rstrip())
    topping_kal = [int(sys.stdin.readline().rstrip()) for i in range(N)]
    print(solution(A, B, C))
