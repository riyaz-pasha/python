class Schedular:
    def __init__(self, processesList, timeQuantum):
        self.timeQuantum = timeQuantum
        self.processes = processesList.copy()
        self.readyQueue = []
        self.runningQueue = []
        self.currentTime = 0

    def setupInitialReadyQueue(self):
        self.readyQueue = [self.processes[0]]
        self.processes.pop(0)

    def addToTheReadyQueue(self, process):
        self.readyQueue.append(process)

    def updateTheReadyQueueForTheNextTimeStamp(self):
        duplicateProcesses = self.processes.copy()
        for process in self.processes:
            if(process.arrivalTime <= self.currentTime):
                # move the process to the ready queue
                self.addToTheReadyQueue(process)
                # remove the process from process list
                duplicateProcesses.pop(0)
            else:
                break
        self.processes = duplicateProcesses

    def saveTheRunningProcessContextAndPushItToTheReadyQueue(self):
        if(self.isAllExecutedFromRunningQueue()):
            return
        currentRunningProcess = self.runningQueue.pop(0)
        if(self.shouldRun(currentRunningProcess)):
            self.addToTheReadyQueue(currentRunningProcess)
    
    def runProcessFromReadyQueue(self):
        if(self.isAllExecutedFromReadyQueue()):
            return
        currentProcess = self.getAProcessToRun()
        self.runningQueue.append(currentProcess)
        if(self.shouldRun(currentProcess)):
            timeRequired = self.timeRequired(currentProcess)
            self.currentTime = self.currentTime+timeRequired
            self.update(currentProcess, timeRequired, self.currentTime)

    def getAProcessToRun(self):
        return self.readyQueue.pop(0)

    def shouldRun(self, process):
        return process.burstTime > 0

    def timeRequired(self, process):
        if(process.burstTime >= self.timeQuantum):
            timeRequiredToRunCurrentProcess = self.timeQuantum
        else:
            timeRequiredToRunCurrentProcess = process.burstTime
        return timeRequiredToRunCurrentProcess

    def update(self, process, timeRequired, currentTime):
        process.burstTime = process.burstTime-timeRequired
        process.completedTime = currentTime

    def isAllProcessesAreExecuted(self):
        return len(self.processes) == 0

    def isAllExecutedFromReadyQueue(self):
        return len(self.readyQueue) == 0

    def isAllExecutedFromRunningQueue(self):
        return len(self.runningQueue) == 0

    def isAnyProcessLeftToRun(self):
        return (not self.isAllProcessesAreExecuted()) or (not self.isAllExecutedFromReadyQueue()) or (not self.isAllExecutedFromRunningQueue())

    def run(self):
        while(self.isAnyProcessLeftToRun()):
            self.updateTheReadyQueueForTheNextTimeStamp()
            self.saveTheRunningProcessContextAndPushItToTheReadyQueue()
            self.runProcessFromReadyQueue()

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
        print(self.name, "-arrivalTime : ", self.arrivalTime, "-completedTime : ",
              self.completedTime, "-burstTime : ", self.completedTime)

    def getTurnAroundTime(self):
        return self.completedTime-self.arrivalTime

    def getWaitingTime(self):
        return self.getTurnAroundTime()-self.actualBurstTime

    def showAllLogs(self):
        print("Name             : ", self.name)
        print("Arrival Time     : ", self.arrivalTime)
        print("Completed Time   : ", self.completedTime)
        print("Turn Around Time : ", self.getTurnAroundTime())
        print("Waiting Time     : ", self.getWaitingTime())


# driver code
print("Enter the number of process you want : ")
numberOfProcesses = 3  # int(input())
print("Enter the Quantum time:")
timeQuantum = 2  # int(input())
listOfProcesses = [
    rrobj("p1", 0, 5),
    rrobj("p2", 1, 4),
    rrobj("p3", 2, 2),
    rrobj("p4", 4, 1),
]
sortof(listOfProcesses)
cpuSchedular = Schedular(listOfProcesses, timeQuantum)
cpuSchedular.run()
print("Displaying the times of all processes")
for process in listOfProcesses:
    process.showAllLogs()
    print("\n")
