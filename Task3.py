import re
#This creates a new file
def createNewFile():
    name = input("Write the name of the file with .txt at the end: ")
    newFile = open(name,"x")
    return newFile
#createNewFile()

#1. Pythonn program to read a file and capitalize first letter of every words
#try this with different approach or methods (use lot of modes)

# Logic: 
# - open the file First
# - get each of the lines
# - get each of the word in a list using .split()
# - then change the word with word[0] with .upper and word[1:] (rest) 
# - then create a new file and append it using open and write

def capitalize():
    with open("File1.txt","r+") as file:
        lines = (file.readlines())
        print(lines)   #['First line\n', 'Second line']
        for eachlines in lines:
            words = eachlines.split(" ")  #words: ['First', 'line\n'].['Second', 'line']
            newWords = [word[0].upper() + word[1:] for word in words]  #['First', 'Line\n'],['Second', 'Line']
            newLines = " ".join(newWords)
        #create a list to append the lists

            with open("NewFile1.txt","a") as newFile:  #w will overwrite the data
                newFile.write(newLines)
#capitalize()


#2. Reads multiline text file and reads the number of times certain file appears
# Logic: 
# - open a File
# - read each of the line 
# - use .count to find how many "x" are there 
# - keep doing it using Loop 
# - return the number

def count(fileName,str):
    with open(fileName,"r") as file:
        return file.read().count(str)
         
    #One way by getting lines from the list 
    # print(lines)
    # count = 0
    # for line in range(len(lines)):
    #     count = count + lines[line].count("l")
    # print(count)

#print(count("Question2.txt","l"))

    
 #3. Logic: 
# Users given: text file, old character, new character and index
# - First read lines
# - create a list of Index
# -find and store all the index of "x" in the Index list
# - we know it has to be list[1]
# - lines[list[1]] replace to a "y"    


with open("Question3.txt","r+") as file:
    lines = file.read()
    idx = [i for i in range (len(lines)) if lines[i] == "e"]
    print(idx)
    #print(idx[2])
    list1 = list(lines)
    #print(list1)
    list1[idx[2]] = "j"
    newLines = "".join(list1)
    #print(newLines)

    with open("Question3Ans.txt","a") as file2:
        file2.write(newLines)