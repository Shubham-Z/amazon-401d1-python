def insertShiftArray(input_array, n):
    l = len(input_array)
    if l % 2 == 0:
        index = int(l/2)
    else:
        index = int(l/2) + 1
        
    last = input_array[l-1]
        
    for i in range(l-1, -1, -1):
        if (i == index):
            input_array[i] = n
            break
        input_array[i] = input_array[i-1]
    input_array.append(last)
    
    return input_array
    

if __name__ == "__main__":
    input_array = []
    print("Enter size of array:")
    n = int(input())
    print("Enter the array:")
    for i in range(0, n):
        x = int(input())
        input_array.append(x)
    
    m = int(input("Enter the number to be inserted: "))
    print(f"array before inserting: {input_array}")
    input_array = insertShiftArray(input_array, m)
    print(f"array after inserting: {input_array}")
            