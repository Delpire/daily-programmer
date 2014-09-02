from random import randint

def quicksort(array):
	pivot = randint(0, len(array)-1)

	S = []
	G = []

	for i in range(0, len(array)):
		if i != pivot:
			if array[i] < array[pivot]:
				S.append(array[i])
			else:
				G.append(array[i])

	if len(S) == 2:
		if S[1] < S[0]:
			S[0], S[1] = S[1], S[0]
	elif len(S) > 1:
		S = quicksort(S)
	
	if len(G) == 2:
		if G[1] < G[0]:
			G[0], G[1] = G[1], G[0]
	elif len(G) > 1:
		G = quicksort(G)

	S.append(array[pivot])

	return S + G

a = [1,5,2,45,6,7,23,4,6,3,4,5,7,2,34,7,45,3,2,1,3,4,56]

print(len(a))
print(a)

a = quicksort(a)
	
print(len(a))
print(a)