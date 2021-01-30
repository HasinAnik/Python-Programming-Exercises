class Calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    
    def getInput(self):
        self.num1 = int(input("Enter a first number: "))
        self.num2 = int(input("Enter a second number: "))
    
    def add(self):
        return self.num1 + self.num2
    
    def subtraction(self):
        return self.num1 - self.num2
    
    def multiplication(self):
        return self.num1*self.num2
    
    def division(self): 
        try:
            return self.num1/self.num2
        except ZeroDivisionError:
            print("Error: Zero can not be at the denominator")
            self.getInput()

myCalc = Calculator()
#myCalc.getInput()

while(True):
    myCalc.getInput()
    input1 = input("Press 1: to add, Press 2: to subtract, Press 3: to multiply & Press 4: to divide, Press 5: to exit: ")
    if(int(input1) == 1):
        print(myCalc.add())
    elif(int(input1) == 2):
        print(myCalc.subtraction())
    elif(int(input1) == 3):
        print(myCalc.multiplication())
    elif(int(input1) == 4):
        print(myCalc.division())
    elif(int(input1) == 5):
        print("Goodbye!")
        break
