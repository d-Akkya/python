from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(akkya, destFrom, destTo):
        print(f"The ticket is booked in train no: {akkya.trainNo} from {destFrom} to {destTo}")

    def getStatus(akkya):
        print(f"Train no: {akkya.trainNo} is running on time")
    
    def getFare(self, destFrom, destTo):
        print(f"Ticket fare train no: {self.trainNo} from {destFrom} to {destTo} is {randint(222, 5555)}")

t = Train(23245)
t.book("Miraj", "Pune")
t.getStatus()
t.getFare("Miraj", "Pune")