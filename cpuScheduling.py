class Schedular:
    def __init__(self,processesList, timeQuantum):
        self.timeQuantum=timeQuantum
        self.processes=processesList.copy()
        self.readyQueue=[]

    def setupInitialReadyQueue(self):
        self.readyQueue = [self.processes[0]]
        self.processes.pop(0)

    def addToTheReadyQueue(self,process):
        self.readyQueue.append(process)
    
    def updateTheReadyQueueForTheNextTimeStamp(self,currentTime):
        duplicateProcesses=self.processes.copy()
        for process in self.processes:
            if(process.arrivalTime<=currentTime):
                self.addToTheReadyQueue(process) #move the process to the ready queue
                duplicateProcesses.pop(0) # remove the process from process list
            else:
                break
        self.processes=duplicateProcesses

    def getAProcessToRun(self):
        return self.readyQueue.pop(0)
    
    def shouldRun(self,process):
        return process.burstTime>0
    
    def timeRequired(self,process):
        return self.timeQuantum if process.burstTime>=self.timeQuantum else process.burstTime

    def update(self,process,timeRequired,currentTime):
        process.burstTime=process.burstTime-timeRequired
        process.completedTime = currentTime

    def isAllProcessesAreExecuted(self):
        return len(self.readyQueue)==0

    def run(self):
        currentTime = 0
        self.setupInitialReadyQueue()
        while(1):
            if(self.isAllProcessesAreExecuted()):
                print("No process is in ready state")
                break

            currentProcess=self.getAProcessToRun()

            if(self.shouldRun(currentProcess)):
                timeRequired=self.timeRequired(currentProcess)
                currentTime=currentTime+timeRequired
                self.update(currentProcess,timeRequired,currentTime)

            self.updateTheReadyQueueForTheNextTimeStamp(currentTime)
            if(self.shouldRun(currentProcess)):
                self.addToTheReadyQueue(currentProcess)

        

def sortof(l): 
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if(l[j].arrivalTime > l[j+1].arrivalTime):
                l[j], l[j+1] = l[j+1], l[j]


class rrobj:
    def __init__(self, name, arrivalTime, burstTime, watingTime=0, completedTime=0, turnAroundTime=0, responseTime=0):
        self.name = name
        self.arrivalTime = arrivalTime
        self.burstTime = burstTime
        self.completedTime = completedTime
        self.watingTime = watingTime
        self.turnAroundTime = turnAroundTime
        self.responseTime = responseTime
        self.actualBurstTime = burstTime

    def display(self):
        print(self.name,"-arrivalTime : ", self.arrivalTime ,"-completedTime : ", self.completedTime,"-burstTime : ", self.completedTime)

    def getTurnAroundTime(self):
        return self.completedTime-self.arrivalTime

    def getWaitingTime(self):
        return self.getTurnAroundTime()-self.actualBurstTime

    def showAllLogs(self):
        print("Name             : ",self.name)
        print("Arrival Time     : ",self.arrivalTime)
        print("Completed Time   : ",self.completedTime)
        print("Turn Around Time : ",self.getTurnAroundTime())
        print("Waiting Time     : ",self.getWaitingTime())



# driver code
print("Enter the number of process you want : ")
numberOfProcesses = 3 #int(input())
print("Enter the Quantum time:")
timeQuantum = 2 # int(input())
listOfProcesses = [
    rrobj("p1",0,5),
    rrobj("p2",1,4),
    rrobj("p3",2,2),
    rrobj("p4",4,1),
]
sortof(listOfProcesses)
cpuSchedular=Schedular(listOfProcesses, timeQuantum)
cpuSchedular.run()
print("Displaying the times of all processes")
for process in listOfProcesses:
    process.showAllLogs()
    print("\n")

