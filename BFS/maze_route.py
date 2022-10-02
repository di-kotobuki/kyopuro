from collections import deque
from sys import stdin

# R: 行数
# C: 列数
# sy, sx: スタート座標（1 <= sy <= R, 1 <= sx <= C）
# gy, gx: ゴール座標（1 <= gy <= R, 1 <= gx <= C）
# nodes: 各座標の状態（壁: "#", 道: "."）
R, C = [int(x) for x in stdin.readline().strip().split()]
sy, sx = [int(x) for x in stdin.readline().strip().split()]
gy, gx = [int(x) for x in stdin.readline().strip().split()]
nodes = [stdin.readline().strip() for _ in range(R)]

sy -= 1
sx -= 1
gy -= 1
gx -= 1

adj = [[1, 0], [0, 1], [-1, 0], [0, -1]]
Q = deque()
Q.append([sy, sx])

# 一つ前のnodeを保存
F = [[[-1, -1] for _ in range(C)] for _ in range(R)]
F[sy][sx] = ["start", "start"]

# 計算量: node数 * 道数
while len(Q) > 0:
    v = Q.popleft()
    y, x = v
    for u in adj:
        dy, dx = u
        _y = y + dy
        _x = x + dx
        if not (0 <= _y < R and 0 <= _x < C):
            continue
        if nodes[_y][_x] == "#":
            continue
        if F[_y][_x] == [-1, -1]:
            F[_y][_x] = v
            Q.append([_y, _x])

route = []
prev = [gy, gx]
while prev != ["start", "start"]:
    route.append(prev)
    py, px = prev
    prev = F[py][px]
for r in reversed(route):
    print(r)