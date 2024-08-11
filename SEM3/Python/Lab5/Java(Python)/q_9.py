def merge_sorted_arrays(A, B):
    i, j = 0, 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1
    return C
try:
    input_A = input("Enter the elements of array A separated by spaces: ")
    A = list(map(int, input_A.split()))
    input_B = input("Enter the elements of array B separated by spaces: ")
    B = list(map(int, input_B.split()))
    C = merge_sorted_arrays(A, B)
    print("Merged sorted array C:")
    print(C)
except ValueError:
    print("Invalid input. Please enter a list of integers separated by spaces.")
