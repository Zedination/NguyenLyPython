import numpy as np

randomArray1 = np.random.random(0,1000)

def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
 
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__":
    bubbleSort(randomArray1)
    print("sắp xếp bằng bubbleSort: ")
    for i in range(len(randomArray1)):
        print ("%d" %randomArray1[i])