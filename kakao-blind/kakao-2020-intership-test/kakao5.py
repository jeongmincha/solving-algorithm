#-*- coding: utf-8 -*-

# from collections import deque
# import sys
# sys.setrecursionlimit(10**6)

def is_cyclic(graph):
    n = len(graph)
    visited = [False] * n
    on_stack = [False] * n
    stack = []

    for w in range(n):
        if visited[w]:
            continue

        stack.append(w)

        while len(stack) is not 0:
            top = stack[-1]

            if not visited[top]:
                visited[top] = True
                on_stack[top] = True
            else:
                on_stack[top] = False
                stack.pop()

            for v in graph[top]:
                if not visited[v]:
                    stack.append(v)
                elif on_stack[v]:
                    return True

    return False


def solution(n, path, order):
    from collections import deque
    undirected_graph = {e: [] for e in range(n)}
    directed_graph = {e: [] for e in range(n)}
    for p in path:
        undirected_graph[p[0]].append(p[1])
        undirected_graph[p[1]].append(p[0])

    visited = [False] * n
    visited[0] = True
    q = deque()
    q.append(0)
    while len(q) is not 0:
        cur = q.popleft()
        for n in undirected_graph[cur]:
            if visited[n]:
                continue

            visited[n] = True
            q.append(n)
            directed_graph[n].append(cur)

    for o in order:
        directed_graph[o[1]].append(o[0])

    return not is_cyclic(directed_graph)


if __name__ == "__main__":
    tests = [
        {
            "n": 9,
            "path": [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],
            "order": [[8,5],[6,7],[4,1]],
            "answer": True
        },
        {
            "n": 9,
            "path": [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],
            "order": [[4,1],[5,2]],
            "answer": True
        },
        {
            "n": 9,
            "path": [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],
            "order": [[4,1],[8,7],[6,5]],
            "answer": False
        },
    ]

    for test in tests:
        n, path, order = test["n"], test["path"], test["order"]
        result = solution(n, path, order)
        print("result: {}".format(result))
        assert result == test["answer"]
