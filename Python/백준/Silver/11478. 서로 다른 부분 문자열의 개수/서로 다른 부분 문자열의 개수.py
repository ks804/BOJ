S = input().strip()
res = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        sub_str = S[i:j+1]
        res.add(sub_str)

print(len(res))