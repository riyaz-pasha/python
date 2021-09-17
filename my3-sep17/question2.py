n=int(input())

totalbill=0
if(n>300):
    totalbill+=(n-300)*15
    n=300
if(n>200):
    totalbill+=(n-200)*10
    n=200
if(n>100):
    totalbill+=(n-100)*7
    n=100
if(n>=1):
    totalbill+=n*5
    n=0
print(totalbill)