#1)Create a list of even numbers till N (N should be user input)
def even(N): #using 2 lines
    return list(filter(lambda num: num % 2 == 0, [numbers for numbers in range(N)]))

#print(even(10))

#2)Find factorial of a number using reduce:
from functools import reduce
def factorial(N):
    return (reduce(lambda num1,num2: num1*num2,[numbers for numbers in range(1,N+1)]))

#print(factorial(5))

#3)find the sum of first N integers:
def sumInt(N):
    return (reduce(lambda num1,num2: num1+num2,[numbers for numbers in range(0,N+1)]))

#print(sumInt(5))

#4)Replace all occurence of first letter with any occurence of choice while preserving the first occurence
def onlyOne(word):
    return word[0] + word[1:].replace(word[0],"")

#print(onlyOne("bababab"))

#5)Sum of digits of a number:
def sumDigits(digits): #(it worked but why do I have to have extra addition at the end)***************
    newDigits = list(str(digits))
    #return (reduce(lambda num1,num2: num1+int(newDigits[num2]),[numbers for numbers in range(0,len(newDigits))]))# + int(newDigits[0])
    return (reduce(lambda num1,num2: int(num1)+int(num2),newDigits))
#print(sumDigits(9862))

#6) Remove a character that has odd index value
def OddIndex(word):
    return "".join([word[i] for i in range(len(word)) if i%2 !=0])
    #print(newWord)
    #return "".join(newWord)
print(OddIndex("String"))

def OddIndex2 (word): 
    final = ""
    for i in range (len(word)):
       final += word[i] if(i % 2 != 0) else "" 
    return final
#print(OddIndex2("String"))

#7) Sort a list in alphabetical order
def sortedAlp(List1):
    return (",".join(sorted(List1)))

#print(sortedAlp(["Hasin","Anik","Mridula"]))

#8)Programatically generate lists or strings of all alphabets in lowercase
def lower(word):
    return list(word.lower())    #sorted(list(String.lower()))

#print(lower("ABCDhRID"))

#9) Convert each strings in a list of strings to uppercase
def Uppercase(List1):
    return list(map(lambda word: word.upper(),List1))

#print(Uppercase(["Hasin", "Anik", "Mridula"]))

#10) Check whether a given key is in dictionary and display the appropriate message:
def check(myDict,key):
    print(str(True) + ", Value: " + str(myDict[key])) if key in myDict.keys() else print(False)

#check({1:"one", 2: "Two", 3:"Three"},2)


#11) Generate a dictionary from the list of numbers with value as the squared of the list elements:

def squaredDict(List1):
    
    #for i in List1:
    #    mydict[i] = i*i
    list2 = list(map(lambda values: values**2,List1))
    mydict = dict(zip(List1,list2))

    return mydict

print(squaredDict([1,2,3,4]))

