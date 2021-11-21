import random as rm

def ishexstr(str):
    if type(str) == int or len(str) < 2:
        return False
    if str[0:2]=="0x":
        return True
    else:
        return False

def comp(x1, x2):
    if (type(x1)==type(x2) and ishexstr(x1) and ishexstr(x2)) or (type(x1)==type(x2) and not ishexstr(x1) and not ishexstr(x2)):
        return x1 < x2
    if ishexstr(x1) and type(x2)==int:
        return int(x1,16) < x2
    if ishexstr(x1) and type(x2)==str:
        return int(x1,16) < int(x2)
    if type(x1)==int and ishexstr(x2):
        return x1 < int(x2,16)
    if type(x1)==int and not ishexstr(x2):
        return x1 < int(x2)
    if type(x1)==str and type(x2)==int:
        return int(x1) < x2

    return int(x1) < int(x2,16)


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if comp(L[i] , R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if comp( arr[j + 1] , arr[j]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]






list = []
for i in range(200000):
    x = rm.randint(0, 10000)
    if i%2==0:
        x = str(x)
    elif i%3==0:
        x=str(hex(x))
    list.append(x)


# x=1
# y=str(hex(10))
# z=str(hex(11))
# print(x<int(y,16))
# print(type(x)==type(y))
# print(str(10)<str(11))
def printt(list):
    for i in range(len(list)):
        if ishexstr(list[i]):
            print(list[i], "(",int(list[i],16),")")
        else:
            print(list[i])

mergeSort(list)
printt(list)