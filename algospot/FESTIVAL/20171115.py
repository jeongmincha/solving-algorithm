# Author: JeongminCha (jeongmin.cha@kaist.ac.kr)
# date: 2017.11.15
def solution_festival(num_days, num_teams, costs):
    cum_sum = [0]
    assert num_days == len(costs)

    min_avg = 100
    for i in range(num_days):
        cum_sum.append(sum(costs[:i+1]))

    for start in range(1, num_days - num_teams + 2):
        for length in range(num_teams-1, num_days-start+1):
            sm = cum_sum[start+length] - cum_sum[start-1]
            avg = float(sm / (length + 1))
            if avg < min_avg:
                min_avg = avg

    return min_avg

def main():
    num_case = int(input())
    for i in range(num_case):
        num_days, num_teams = [int(_) for _ in input().split()]
        costs = [int(_) for _ in input().split()]
        ans = solution_festival(num_days, num_teams, costs)
        print (ans)

if __name__ == "__main__":
    main()