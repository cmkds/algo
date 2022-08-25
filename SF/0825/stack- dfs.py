stack = []
stack.append(s)

visited = set()

#중복방문 x
while 1:
    value = stack[-1]

    for next in Graph(value):
        if next not in visited:
            stack.append(next)
            visited.add(next)
            break #완전 탐색 필요 X /  dfs필요있다
    else:
        stack.pop()

def dfs(value):
    for next in Graph(value):
        if next not in visited:
            visited.add(next)
            dfs(next)
    return