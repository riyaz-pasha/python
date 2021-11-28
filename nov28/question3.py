def getNewPos(positions,last_positions):
    new_positions=last_positions.copy()
    for i in range(len(positions)):
       new_positions[positions[i]-1]= last_positions[i]
    return new_positions

def isSame(a,b):
    return all(x == y for x,y in zip(a,b))

def calculateTimeOfSamePositions(no_friends,positions):
    t=0
    initial_positions=[i for i in range(no_friends)]
    latest_positions=initial_positions.copy()
    while(1):
        t+=1
        latest_positions=getNewPos(positions,latest_positions)
        if(isSame(initial_positions,latest_positions)):
            break
    return t

tc=int(input())
for i in range(tc):
    no_friends=int(input())
    positions =list(map(int, input().split(' ')))
    print(calculateTimeOfSamePositions(no_friends,positions))
