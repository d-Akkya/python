from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, destFrom, destTo):
        print(f"The ticket is booked in train no: {self.trainNo} from {destFrom} to {destTo}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")
    
    def getFare(self, destFrom, destTo):
        print(f"Ticket fare train no: {self.trainNo} from {destFrom} to {destTo} is {randint(222, 5555)}")

t = Train(23245)
t.book("Miraj", "Pune")
t.getStatus()
t.getFare("Miraj", "Pune")