def insertion_sort(A):
	for j in range(1,len(A)):
		key = A[j]
		i = j-1
		while i >= 0 and A[i] > key:
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
	return A

print(insertion_sort([1,3,2]))
print(insertion_sort([3,2,1,5,6]))
print(insertion_sort([1,2,3]))
