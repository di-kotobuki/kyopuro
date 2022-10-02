from sys import stdin

# N: ビット数
# S: 総和
# AB: 各ビットが取る値
N, S = [int(x) for x in stdin.readline().strip().split()]
AB = [[int(x) for x in stdin.readline().strip().split()] for _ in range(N)]

# 先頭からiビットの合計がS以下の値となりうるか
dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1
comb = [[""] * (S + 1) for _ in range(N + 1)]
for i in range(N):
    a, b = AB[i]
    for j in range(S + 1):
        if dp[i][j]:
            if j + a <= S:
                dp[i + 1][j + a] = 1
                comb[i + 1][j + a] = f"{comb[i][j]}H"
            if j + b <= S:
                dp[i + 1][j + b] = 1
                comb[i + 1][j + b] = f"{comb[i][j]}T"

# if dp[N][S]:
#     print("Yes")
#     print(comb[N][S])
# else:
#     print("No")

print(f"総和がSになるABのパターン: {comb[N][S]}")
[print(x) for x in comb]
