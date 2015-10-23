def insertion_sort(A):
	l = len(A)

	for i in range(1, l):
		key = A[i]
		j = i - 1

		while j >= 0 and A[j] >= key:
			A[j+1] = A[j]
			j = j - 1

		A[j+1] = key

	return A

if __name__ == '__main__':
	print insertion_sort([4,5,6,3,1,2])
