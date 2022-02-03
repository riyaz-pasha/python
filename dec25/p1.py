n=int(input())
sum=1
for i in range(1,n+1):
    sum*=i**(n+1-i)
print(sum)
