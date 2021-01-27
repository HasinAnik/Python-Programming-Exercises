#1) Function to create a disctionary grouping a sequence of key-value pairs into a dictionary of lists
list1 = [('yellow',1),('blue',2),('yellow',3)]
#lkeys = [numbers[0] for numbers in list1] #seperated the keys
#values = [numbers[1] for numbers in list1] #seperated the values


#logic:
# 1. list of tuples are given. 
# 2. Iterate through the list1 to obtain keys and values
# 3. if key doesn't exist in the dictionary: 
#         we create a list and then insert it::  dict[keys] = [].append(value) 
#4. If keys exist, then we just append the value to the dict[keys] :: dict[keys].append(value)

mydict = {}
# for keys,values in list1:
#     if keys not in mydict:
#         mydict[keys] = list(str(values))    #list(str(values)) 
#     elif (keys in mydict):
#         mydict[keys].append(values)

print(mydict)

# for keys,values in list1:
#     mydict[keys] = list(str(values))         #list(str(values))
#print(mydict)

def constructDictionary(inputList):
    result = {}
    for k, v in inputList:
        #result[k] = [].append(v) if k not in result.keys() else result[k].append(v)
        result.setdefault(k, []).append(v)  
        
    return result
inputList = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
print("Original list:")
print(inputList)

print("\nOutput dictionary")
print(constructDictionary(inputList))

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
    pascalRow,y,num1,list1 = 1,1,1,[]
    while pascalRow <= rows:
        #print("printing row : " + str(pascalRow))
        while(y <= pascalRow):
            #print("printing col: " + str(y))
            #list1.append(num1)
            if(pascalRow - y == 0 or pascalRow - y == pascalRow-1):
                list1.append(str(1))
            else:    
                list1.append(str(pascalRow-1))        
            num1+=1
            y+=1
        else:
            pascalRow+=1 #determine rows
            
        print(" ".join(list1)) 
        # print(list1, end = "")    
        y=1  #this determines columns
        list1 = []
        
#pascal(5)