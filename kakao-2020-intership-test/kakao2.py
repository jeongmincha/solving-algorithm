def solution(expression):
    import copy
    from itertools import permutations
    answer = -1

    set_operator = set()
    stack = [""]
    # stack 은 expression을 split해서 나온 list
    # ex. "100-200*500" -> [100, "-", 200, "*", 500]
    for char in expression:
        if not char.isdigit():
            stack[-1] = int(stack[-1])
            stack.append(char)
            set_operator.add(char)
            stack.append("")
        else:
            stack[-1] += char
    stack[-1] = int(stack[-1])
    
    # operators 는 연산자 우선순위를 의미하는 연산자 tuple이 됨.
    # operators 가 만약 ("*", "-", "+") 라면 "*" > "-" > "+" 우선순위라는 뜻.
    for operators in list(permutations(set_operator, len(set_operator))):
        _stack = copy.deepcopy(stack)

        # 우선순위에 맞춰서 operators에 operator를 뽑아냄.
        for operator in operators:
            idx = 0

            # 현재 선택된 연산자가 stack (expression) 안에서 없어질 때까지 계속 반복.
            while operator in _stack or idx > len(_stack):
                # 해당 연산자에 대해서 처리하고, 해당 연산자 주변에 있던 잔재들을 제거하여 stack에 남김.
                if _stack[idx] is operator:
                    if operator == "*":
                        _stack.insert(idx-1, _stack[idx-1] * _stack[idx+1])
                    elif operator == "-":
                        _stack.insert(idx-1, _stack[idx-1] - _stack[idx+1])
                    elif operator == "+":
                        _stack.insert(idx-1, _stack[idx-1] + _stack[idx+1])        
                    _stack = _stack[:idx] + _stack[idx+3:]
                    idx = 0
                else:
                    idx += 1

        # 여태까지 계산된 값 중 가장 높은 값만 answer에 저장함.
        if (answer < abs(_stack[-1])):
            answer = abs(_stack[-1])

    return answer


if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print("answer: {}".format(solution(expression)))