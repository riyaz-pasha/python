[num,lowest_factor_pos] =list(map(int, input().split(' ')))

factors=[]
for i in range(1,num+1):
        if num%i==0:
            factors.append(i)

if(len(factors)>=lowest_factor_pos):
    print(factors[lowest_factor_pos-1])
else:
    print(-1)
