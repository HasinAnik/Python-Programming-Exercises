print("This is the homework for 2/14/2021 class")
print("Linear Search: Start from the 1st element to the last element until it finds the value looking for ")

def intSearch(num, list1):
    list1 = users.split(",") #Here I am splitting all the commas to just get the elements.
    list2 = [int(num) for num in list1]
    for elem in range(len(list2)):
        if (int(list2[elem]) == num):return elem
            #return "Invalid input"
    return -1

num = int(input("Entr a number: "))
users = input("Enter a integer list seperated by a comma: ")
print("First Occurence of the num is " + str(intSearch(num,users)))


def charSearch(char, list1):
    list1 = users.split(",")
    for elem in range(len(list1)):
        if (list1[elem] == char):return elem
    return -1

char = input("Entr a char: ")
users = input("Enter a char list seperated by a comma: ")
print("First Occurence of the num is " + str(charSearch(char,users)))
