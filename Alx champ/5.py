with open("connect.in") as f:
    n, m = map(int, f.readline().split())
    graph = {}
    for i in range(n):
        graph[i] = []