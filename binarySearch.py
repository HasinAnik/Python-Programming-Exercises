
print("Welcome to sorting program")
input1 = input("Type the list you want to sort: ")
input2 = input("Enter a number you want to find: ") 

# ----------------------------------- Changing to a int list -----------------------------------------------------------------------------

def intList (input1):
    userList = input1.split(",")
    for i in range (len(userList)):
        userList[i] = int(userList[i])
    return userList

userList = intList (input1)
print(userList)

# -----------------------------------------------------------Selection Sort -------------------------------------------------------

def selectionSort(list1):

    for i in range (len(list1)):
        min = i
        for j in range (i+1,len(list1)):
            if (list1[j] < list1[min]):
                min = j

        if (min != i):
            list1[min], list1[i] = list1[i], list1[min]
    return list1

sortedList = selectionSort(userList)  # 1,2,4,7,7,9,12
print(sortedList)

# ---------------------------------------------------Binary Search --------------------------------------------------------------------

target = int(input2)
def binarySearch(list1, low, high):

    mid = (high + low)//2   #Floor division we use two back slashes    

    # print("high = " + str(high) + " low = " + str(low) + " mid = " + str(mid))

    if (low <= high):
        if target == list1[mid]:
            print("Found in position: " + str(mid))
            return mid

        elif target < list1[mid]:    #Left sub-list/array
            high = mid-1
            binarySearch(list1, low, high)

        elif target > list1[mid]:    #right sub-list/array
            low = mid+1
            binarySearch(list1, low, high)

    else:
        print("-1")
        return -1

    
newBinary = binarySearch(sortedList, 0, len(userList)-1)
# newBinary = binarySearch([1,5,7,10,15], 0, 4)
print(newBinary)

    




