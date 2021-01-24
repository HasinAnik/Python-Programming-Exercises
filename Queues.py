class My_Queue():
    def __init__(self):
        self.items = []
        self.first = 0
        self.last = 0
    
    def size (self):
        return self.last
    
    def enqueue (self, value):
        self.items.append(value)
        self.last = self.last + 1 

    def deque(self):
        if (self.last == 0):
            return None
        else:
            self.last = self.last - 1
            return self.items.pop(0) 

    def isEmpty(self):
        if(self.last == self.first):
            return True
        else: 
            return False
    
    def printQueue(self):
        for i in range (self.last):
            print(self.items[i])
    
if __name__ == "__main__":
    myQueue = My_Queue()
    print("Welcome to short Queue class")
    print(" ")

    while True:
        input1 = input("1 to stop, 2 to enqueue, 3 to dequeue, 4 to print, 5 to see the size & 6 to see if the Queue is Empty: ") 
        if(int(input1) == 1):
            print("Goodbye")
            break
        elif (int(input1) == 2):
            input2 = input("Enter a number to Enqueue: ")
            print("Enquing: " + input2)
            myQueue.enqueue(int(input2))
        
        elif(int(input1) == 3):
            #print("Dequing: ")
            print("Dequing: " + str(myQueue.deque()))

        elif(int(input1) == 4):
            print("Printing the Queue: ")
            myQueue.printQueue()
        
        elif(int(input1) == 5):
            print("Size: " + str(myQueue.size()))

        elif(int(input1) == 6):
            print("isEmpty: " + str(myQueue.isEmpty()))

    #myQueue.enqueue(1)
    #myQueue.enqueue(5)
    #myQueue.enqueue(7)
    #myQueue.enqueue(3)
    #myQueue.enqueue(2)
    #myQueue.printQueue()
    #print(" ")
    #print(myQueue.deque())
    #print(" ")
    #myQueue.printQueue()
    #print("size: "  + str(myQueue.size()))
    #print("isEmpty: " + str(myQueue.isEmpty()))
    #print(myQueue.deque())
    #print(myQueue.deque())
    #print(myQueue.deque())
    #print(myQueue.deque())
    #myQueue.printQueue()
    #print(myQueue.deque())
    #print("size: "  + str(myQueue.size()))
    #print("isEmpty: " + str(myQueue.isEmpty()))