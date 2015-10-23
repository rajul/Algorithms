def merge(A, B):
	l1 = len(A)
	l2 = len(B)

	i = 0
	j = 0

	r = []

	while i < l1 and j < l2:
		if A[i] < B[j]:
			r.append(A[i])
			i = i + 1
		else:
			r.append(B[j])
			j = j + 1

	if i < l1:
		r.extend(A[i:])
	elif j < l2:
		r.extend(B[j:])

	return r

def mergesort(M):
	l = len(M)

	if l <= 1:
		return M

	A = mergesort(M[:l/2])
	B = mergesort(M[l/2:])

	return merge(A, B)

if __name__ == '__main__':
	print mergesort([2,32,111,23,12,4])
	print mergesort([2, 2,111,23,2,4])