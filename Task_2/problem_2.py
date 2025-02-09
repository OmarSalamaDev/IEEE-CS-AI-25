
n = int(input())
scores = []

scores = list(map(int, input().split()))

scores = sorted(scores, reverse=True)
max = scores[0]
secondMax = scores[0]

for i in range(1, n):
    if scores[i] < max:
        secondMax = scores[i] 
        break

print(secondMax)
    