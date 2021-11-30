
def printElement(arr, n):
    for i in range(1, n - 1, 1):
        if(arr[i] >= arr[i-1] and arr[i] >= arr[i +1]):
            print(arr[i], end = " ")
    if arr[-1] >= arr[-2]:
        print(arr[-1], end = " ")



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,100,99, 100]
    n = len(arr)
    printElement(arr, len(arr))