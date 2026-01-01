
def DFS(v):
    if v == "out":
        return 1
    if v not in visited:
        count = 0
        for neighbor in nodes[v]:
            count += DFS(neighbor)
        paths[v] = count

    return paths[v]
    

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

total = DFS("you")

print("Total:", total)
