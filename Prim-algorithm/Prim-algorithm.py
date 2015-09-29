import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'in')
file=open(filename)

N = int(file.readline())
graph = [[0]*N for _ in range(N)]

for i in range(0, len(graph)):
    children = file.readline().strip('\n').split(' ')
    for j in range(0, len(children)):
        graph[i][j] = int(children[j])

def prim(graph, N):
    used = [0 for _ in range(N)]
    min_e = [32767 for _ in range(N)]
    sel_e = [-1 for _ in range(N)]

    res = []

    min_e[0] = 0
    for i in range(N):
        v = -1
        for j in range(N):
            if used[j] == 0 and (v == -1 or min_e[j] < min_e[v]):
                v = j
        used[v] = 1
        if sel_e[v] != -1:
            res.append(sorted([str(v+1), str(sel_e[v]+1)]))

        for to in range(N):
            if graph[v][to] < min_e[to]:
                min_e[to] = graph[v][to]
                sel_e[to] = v
    return res

res = prim(graph, N)

def weight(graph, res):
    sum = 0
    for i in range(len(res)):
        sum += graph[int(res[i][0])-1][int(res[i][1])-1]
    return sum


sum_weight = weight(graph, res)

def write(res, graph, sum_weight):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'out')
    file=open(filename, 'w')
    wr = [[0]*N for _ in range(N)]
    for i in range(len(res)):
        wr[int(res[i][0])-1][int(res[i][1])-1] = 1
        wr[int(res[i][1])-1][int(res[i][0])-1] = 1
    for a in range(len(wr)):
        file.write(''.join(str(x)+' ' for x in wr[a]))
        file.write('\n')
    file.write(str(sum_weight))

write(res, graph, sum_weight)