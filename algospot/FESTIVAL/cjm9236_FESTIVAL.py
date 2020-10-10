# FESTIVAL problem (https://algospot.com/judge/problem/read/FESTIVAL)
# Author: JeongminCha (cjm9236@me.com)

MAX_INTEGER = 987654321

def minimum_average_cost(total_days, n_team, costs):
    partsum = 0
    partsum_list = [0]
    for cost in costs:
        partsum += cost
        partsum_list.append(partsum)

    min_value = partsum_list[-1]
    for lend_days in range(n_team, total_days+1):
        min_sum = partsum_list[-1]
        for start_day in range(total_days-lend_days+1):
            # sum of costs in lend_days after start_day
            sm = partsum_list[start_day+lend_days] - partsum_list[start_day]
            if sm < min_sum:
                min_sum = sm
        cost = float(min_sum) / lend_days
        if min_value > cost:
            min_value = cost
    return min_value

if __name__ == "__main__":
    test_case = int(raw_input())

    for case in range(test_case):
        # number of days, number of teams
        [n_days, n_team] = [e for e in map(int, raw_input().split(' '))]
        costs = map(int, raw_input().split(' '))

        # Print answer
        ans = minimum_average_cost(n_days, n_team, costs)
        print("%.10f" % ans)