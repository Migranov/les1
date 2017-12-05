N = 9
listN = []
for i in range(0,N) :
    listN.append(0)

sum=0
list = [7,4,9,1,8,1,3,1,3,2,6,7,5]
print(list)
for i in range(0, len(list)) :
    listN[list[i]-1]+=1

for i in range(0,N) :
    if listN[i] != 0 :
        sum += 1

print(sum)