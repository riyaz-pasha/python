noOfRods = int(input())
rodsLength = []

for i in range(noOfRods):
    rodLen = int(input())
    rodsLength.append(rodLen)

rodsLength.sort(reverse=True)
samScore = 0
bamScore = 0

isSamsTurn = True

while(len(rodsLength)):
    currentRodLength = rodsLength.pop(0)
    if isSamsTurn:
        samScore = samScore+currentRodLength
        isSamsTurn = False
    else:
        bamScore = bamScore+currentRodLength
        isSamsTurn = True

    if(currentRodLength > 1):
        rodsLength.append(currentRodLength//2)
        rodsLength.sort(reverse=True)

print(samScore)
