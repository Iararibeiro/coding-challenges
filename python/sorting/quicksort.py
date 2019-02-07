def partition(arr, left, right):
    i = left - 1
    #pivot is the last element
    pivot = arr[right]
    for j in range(left, right):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i+1


def quicksort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quicksort(arr, left, pivot - 1)
        quicksort(arr, pivot + 1, right)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr,0,n-1)
