import random

# process class to handle holding of tickets 
class Process:
    def __init__(self, processName, tickets):
        self.processName = processName
        self.tickets = tickets
        
    # if number in tickets return name, else return false
    def isInTickets(self, selectedNumber):
        if selectedNumber in self.tickets:
            return self.processName
        else:
            return False
        
# scheduler class to handle holding and selection of processes
class Scheduler:
    def __init__(self, maxBet):
        self.maxBet = maxBet
        self.processes = []
        
    # add to current processes
    def addProcess(self, processName, tickets):
        process = Process(processName, tickets)
        self.processes.append(process)
        
    # select next process to be run
    def selectNextProcess(self):
        randomNum = random.randint(0,self.maxBet)
        
        for c in self.processes:
            # if not false, isBet is the name of the process
            isBet = c.isInTickets(randomNum)
            
            if isBet != False:
                return isBet
                

def main():
    maxBet = 20
    schedule = Scheduler(maxBet)
    
    schedule.addProcess("1", [1,2,3,4,5])
    schedule.addProcess("2", [6,7,8,9,10])
    schedule.addProcess("3", [11,12,13,14,15])
    schedule.addProcess("4", [16,17,18,19,20])
    
    nextProcess = schedule.selectNextProcess()
    
    print("Process {} wins the lottery!".format(nextProcess))
    

if __name__ == "__main__":
    main()