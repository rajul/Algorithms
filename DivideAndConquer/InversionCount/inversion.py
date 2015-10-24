def merge_and_count_split_inv(A, B):
	C = []

	len_A = len(A)
	len_B = len(B)

	i = 0
	j = 0
	count_inv = 0

	while i < len_A and j < len_B:
		if A[i] <= B[j]:
			C.append(A[i])
			i = i + 1
		else:
			C.append(B[j])
			j = j + 1

			count_inv = count_inv + (len_A - i)

	if i == len(A):
		C.extend(B[j:])

	if j == len(B):
		C.extend(A[i:])

	return C, count_inv


def sort_and_count_inversions(A):
	l = len(A) 

	if l <= 1:
		return A, 0

	B, left_inv = sort_and_count_inversions(A[:l/2])
	C, right_inv = sort_and_count_inversions(A[l/2:])
	D, split_inv = merge_and_count_split_inv(B, C)

	return D, (left_inv + right_inv + split_inv)

if __name__ == '__main__':
	numbers = [1,3,5,2,4,6]

	print sort_and_count_inversions(numbers)[1]
