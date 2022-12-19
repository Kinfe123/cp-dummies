# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input().split()
M = input().split()
A = set(input().split())
B = set(input().split())

countforhappiness = 0

for i in M:
    if i in A:
        countforhappiness+=1
    elif i in B:
        countforhappiness-=1

    else:
        countforhappiness+=0
print(countforhappiness)
