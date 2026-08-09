import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

start_time = time.perf_counter()

insertion_sort(arr)

end_time = time.perf_counter()

print("\nSorted Array:")
print(arr)

execution_time = end_time - start_time
print(f"\nExecution Time: {execution_time:.10f} seconds")

print("\nTime Complexity:")
print("Best Case    : O(n)")
print("Average Case : O(n^2)")
print("Worst Case   : O(n^2)")
print("Space Complexity: O(1)")
