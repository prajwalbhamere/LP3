import random 
import time

def deterministic_partition(arr, low, high):
    pivot = arr[(low + high)//2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot_index)
        deterministic_quicksort(arr, pivot_index + 1, high)
    print("Output of Deterministic Quick Sort : ", arr)

def randomised_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[(low + high)//2] = arr[(low+high)//2], arr[pivot_index]
    pivot = arr[(low + high)//2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1    
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def randomised_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomised_partition(arr, low, high)
        randomised_quicksort(arr, low, pivot_index)
        randomised_quicksort(arr, pivot_index + 1, high)
    print("Output of Randomized Quick Sort : ", arr)

n = int(input("Enter the number of elements to be entered in the array: "))
user_input = input("Enter the elements separated by a space: ")
user_array = list(map(int, user_input.split()))

deterministic_array = user_array.copy()
randomised_array = user_array.copy()

start_time = time.time()
deterministic_quicksort(deterministic_array, 0, n-1)
deterministic_time = time.time() - start_time

start_time = time.time()
randomised_quicksort(randomised_array, 0, n-1)
randomised_time = time.time() - start_time

print("Deterministic quick sort time: ", deterministic_time)
print("Randomised quick sort time: ", randomised_time)
