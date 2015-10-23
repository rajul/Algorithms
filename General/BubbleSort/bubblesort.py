def bubble_sort(A):
	l = len(A)

	for i in range(l):
		for j in range(l-i-1):
			if A[j] > A[j+1]:
				t = A[j]
				A[j] = A[j+1]
				A[j+1] = t

	return A


if __name__ == '__main__':
	print bubble_sort([2,3,5,1,2,4,2,1])
