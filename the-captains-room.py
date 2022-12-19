# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
room_list = input().split()
map_ = {}
count = len(room_list)
for i in range(len(room_list)):
    if room_list[i] in map_:
        
        map_[room_list[i]] += 1
    else:
        map_[room_list[i]] = 1

# print(map_[i] for i in map_.keys() if  i == 1 )
answer = 0
for keys , values in map_.items():
    if values == 1:
        answer = keys
print(answer)

# print(map_)
