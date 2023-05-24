# Read input from STDIN
N, M = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

cost = []
for i in range(M):
    temp_q = queries[i]
    total_cost = 0

    for j in range(N):
        temp = arr[j] - temp_q
        if temp < 0:
            temp = temp * -1

        total_cost = total_cost + temp

    cost.append(total_cost)
    
# Unpacking elements inside cost and printing them separated by a comma
print(*cost) 
