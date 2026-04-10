N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
pA = pB = index = 0

merg = [0 for _ in range(N + M)]

while pA < N and pB < M :
    if A[pA] < B[pB] :
        merg[index] = A[pA]
        index += 1
        pA += 1
    elif A[pA] > B[pB] :
        merg[index] = B[pB]
        index += 1
        pB += 1
    else :
        merg[index] = A[pA]
        merg[index + 1] = A[pA]
        index += 2
        pA += 1
        pB += 1

if pA == N :
    while pB < M :
        merg[index] = B[pB]
        index += 1
        pB += 1
elif pB == M :
    while pA < N :
        merg[index] = A[pA]
        index += 1
        pA += 1
    

result = ' '.join(list(map(str, merg)))
print(result)