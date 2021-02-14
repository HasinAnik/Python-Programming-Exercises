print("This is the homework for 2/14/2021 class")
print("Linear Search: Start from the 1st element to the last element until it finds the value looking for ")

def lSearch(num, list1):
    for elem in range(len(list1)):
        if (int(list1[elem]) == num):return elem
            #return "Invalid input"
    return -1

num = int(input("Entr a number: "))
users = input("Enter a list seperated by a space: ")
list1 = users.split()
for elem in range(len(list1)):
    list1[elem] = int(list1[elem])

print("First Occurence of the num is " + str(lSearch(num,list1)))
