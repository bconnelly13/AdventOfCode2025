import time

def DFS(v, dac, fft):
    if v == "dac":
        dac = True
    if v == "fft":
        fft = True
    if v == "out":
        if dac and fft:
            return 1
        return 0
    if (v, dac, fft) not in visited:
        count = 0
        for neighbor in nodes[v]:
            count += DFS(neighbor, dac, fft)
        paths[(v, dac, fft)] = count
        visited.add((v, dac, fft))

    return paths[(v, dac, fft)]
    
with open("input.txt") as f:
    lines = f.readlines()

nodes = {}
for line in lines:
    line = line.strip("\n")
    colonIndex = line.index(":")
    node = line[0:colonIndex]
    edges = [edge for edge in line[colonIndex+1:].strip().split(" ")]
    nodes[node] = edges

visited = set()
paths = {}

total = DFS("svr", False, False)

print("Total:", total)

