print("This is the homework for 2/14/2021 class")
print("Linear Search: Start from the 1st element to the last element until it finds the value looking for ")

def lSearch(num, list1):
    for elem in range(len(list1)):
        if (list1[elem] == num):return elem
    return -1

list1 = [1,2,4,5,6]
print(lSearch(5,list1))