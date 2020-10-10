# Problem: COINS (https://algospot.com/judge/problem/read/COINS)
# Author: Jeongmin Cha (jeongmin.cha@kaist.ac.kr)
# Date: 2017.11.17


def find_cases(sum, n_coins, coins):
    table = [[0 for _ in range(n_coins)] for _ in range(sum+1)]
    for i in range(n_coins):
        table[0][i] = 1

    for sum_ in range(1, sum+1):
        for coin_idx in range(n_coins):
            if sum_ - coins[coin_idx] >= 0:
                s1 = table[sum_ - coins[coin_idx]][coin_idx]
            else:
                s1 = 0

            if coin_idx >= 1:
                s2 = table[sum_][coin_idx-1]
            else:
                s2 = 0

            table[sum_][coin_idx] = s1 + s2

    return table[sum][n_coins-1]


if __name__ == "__main__":
    n_case = int(input())
    for _ in range(n_case):
        sum, n_coins = [int(_) for _ in input().split()]
        coins = [int(_) for _ in input().split()]
        print (find_cases(sum, n_coins, coins) % 1000000007)
