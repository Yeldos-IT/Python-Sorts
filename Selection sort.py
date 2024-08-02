A = [64, 25, 12, 22, 11]

# Traverse through all elements in the list
for i in range(len(A)):
    # Assume the current element is the minimum
    min_idx = i
    # Iterate through the unsorted portion of the list
    for j in range(i + 1, len(A)):
        # If a smaller element is found, update the index of the minimum
        if A[min_idx] > A[j]:
            min_idx = j
    # Swap the minimum element with the first unsorted element
    A[min_idx], A[i] = A[i], A[min_idx]

# Print the sorted array
print("Sorted array:")
for i in range(len(A)):
    # Printing each element with a comma and space, except for the last one
    print("%d" % A[i], end=", " if i < len(A) - 1 else "")