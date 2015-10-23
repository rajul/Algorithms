def selection_sort(A):
	l = len(A)

	for i in range(l):
		min_elem, min_pos = A[i], i

		for j in range(i, l):
			if A[j] < min_elem:
				min_elem = A[j]
				min_pos = j

		A[min_pos] = A[i]
		A[i] = min_elem

	return A

if __name__ == '__main__':
	print selection_sort([3,2,1,5,3])
			