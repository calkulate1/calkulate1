n = int(input())
k = int(input())-1
people = list(range(1,n+1))
while len(people) !=1:
    k = k % len(people)
    del people[k]
    k += 2
print(people)
