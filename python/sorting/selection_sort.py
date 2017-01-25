def selection_sort(A):
	for i in range(0,len(A)):
		minimal = i
		for j in range(i+1,len(A)):
			if A[j] < A[minimal]:
				minimal = j
		aux = A[minimal]
		A[minimal] = A[i]
		A[i] = aux
	return A

print(selection_sort([1,3,2]))
print(selection_sort([3,2,1,5,6]))
print(selection_sort([1,2,3]))
