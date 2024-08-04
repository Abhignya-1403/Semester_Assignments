rows = int(input("Enter how many rows: ")) 
for i in range(1, rows + 1): 
    for j in range(1, i): 
        print(" ", end=" ") 
    print(i, end=" ") 
    num_asterisks = 2 * (rows - i) - 1 
    for j in range(num_asterisks): 
        print(" ", end=" ") 
        if num_asterisks > 0: 
         print(i, end=" ") 
    print()