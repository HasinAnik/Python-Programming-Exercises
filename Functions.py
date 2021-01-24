#1) Function to create a disctionary grouping a sequence of key-value pairs into a dictionary of lists
List1 = [('yellow',1),('blue',2),('yellow',3)]
print(List1[0][0])

#2) Remove duplicates from a list while preserving order:

def noDuplicates(List1):
    newList = []
    for elements in List1:
       newList.append(elements) if(elements not in newList) else ""
    return newList
#print(noDuplicates(["hasin", "anik", "Jason","hasin","Darulo", "hasin"]))

#3) Using list number of line of code print Floyd's Triangle:
def floyd(rows):
    x,y,num1,list1 = 1,1,1,[]
    while x <= rows:
        #print("printing: " + str(num))
        while(y <= x):
            #list1.append(num1)
            list1.append(str(num1))        
            num1+=1
            y+=1
        else:
            x+=1 #determine rows
            #ans.join(list1)
        print(" ".join(list1)) 
        # print(list1, end = "")    
        y=1  #this determines columns
        list1 = []
        
#floyd(3)

#4) Function to check whethered the entered password is valid:
    #i)Have to be atleast 8 character long
    #ii)Should contain atleast one upper case letter
    #iii) Should contain one special character
    #iv) Min # one number should be present

def valid(password):
    upper,special,number = 0,0,0
    for character in range (len(password)):
        if(password[character].isupper() == True):upper+=1
        if(password[character].isalnum() != True):special+=1
        if(password[character].isnumeric() == True):number+=1
    
    return True if(upper>0 and special > 0 and number > 0 and len(password) >= 8) else False

#print(valid("Hasin$2020"))


#5: Print first n rows of Pascal Triangle
def pascal(rows):
    x,y,num1,list1,ans = 1,1,1,[]," "
    while x <= rows:
        #print("printing: " + str(num))
        while(y <= x):
            #print(str(num1) + " ")
            list1.append(num1)        
            num1+=1
            y+=1
        else:
            print()
            x+=1 #determine rows
            #ans.join(list1)
        print(list1, end = "")    
        y=1  #this determines columns
        list1 = []