class Stacks():

    def __init__(self): #constructor
        self.items = []
        self.base = 0
        self.top = 0

    def printStack (self):  #print the elements in the Stacks(array)
        print ("Printing the Stacks")
        for i in range (self.top):
            print(self.items[i])
    
    def empty (self):   #if base and top is same then its empty and return true or else false
        print("Is your Stack empty?: ")
        if (self.base == self.top):
            return True
        else:
            return False
    
    def size (self):
        print("Size is: ")
        return self.top
    
    def push (self,value):   #here we are adding the value in the right using the append
        self.items.append(value)
        self.top = self.top + 1
    
    def pop (self):   #"""here we will print the last value and decerement b"""
        self.top = self.top - 1
        print("We poped: " + str(self.items[len(self.items) - 1]))
        return self.items.pop()

    def peek (self): #prints the top element which is the element in b
        if (len(self.items) > 0):
            return (self.items[len(self.items)-1])
        else:
            return None
    

if __name__ == "__main__":
    myStack = Stacks()
    print ("Welcome to small stack program: ")
    print (" ")

    while True:
        input1 = input("Press: 1 to stop, 2 to push, 3 to pop, 4 to print, 5 to check if its empty, 6 for size, 7 for peek")
        if (input1 == '1'):
            print("Good bye")  
            break
        elif (input1 == '2'):
            input2 = input("Enter a number")
            value = int(input2)
            myStack.push(value)
        elif (input1 == '3'):
            myStack.pop()
        elif (input1 == '4'):
            myStack.printStack()
        elif(input1 == '5'):
            print(myStack.empty())
        elif(input1 == '6'):
            print(myStack.size())
        elif(input1 == '7'):
            print(myStack.peek())


   # myStack = Stacks()
   # myStack.push(1)
   # myStack.push(2)
   # myStack.push(3)
   # print(myStack.size())
   # myStack.printStack()
   # print(myStack.empty())
   # myStack.pop()
   # myStack.printStack()
   # print(myStack.size())
   # print(myStack.peek())