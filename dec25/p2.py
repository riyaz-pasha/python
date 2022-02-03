n = int(input())
arr=[]
for i in range(0,n):
    arr.append(int(input()))
arr.sort()
sum_of_idexes=0
for i in range(1,n+1):
    sum_of_idexes+=i
j=0
while(sum_of_idexes>0):
    sum_of_idexes-=arr[j]
    j+=1
print(j)

