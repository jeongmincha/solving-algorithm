# http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
def convert_number(num, n):
    ch = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    chs = [] 

    while num / n != 0:
        chs.insert(0, ch[num % n])
        num /= n
    chs.insert(0, ch[num])

    result = ""
    for c in chs:
        result += c

    return str(result)


def tube_problem(n, t, m, p):
    s = ""
    for i in range(t*m):
        s += convert_number(i, n)

    solution = ""
    for i in range(t):
        solution += s[i * m + p-1]

    return solution

print(tube_problem(2,4,2,1))
print(tube_problem(16,16,2,1))
print(tube_problem(16,16,2,2))

