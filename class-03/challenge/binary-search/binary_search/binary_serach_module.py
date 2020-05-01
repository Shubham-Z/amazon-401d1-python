def search(input_array, n, m, x):
    if n > m:
        return -1

    mid = int((n+m)/2)
    y = input_array[mid]
    if y == x:
        return mid
    elif y > x:
        return search(input_array, n, mid-1, x)
    else:
        return search(input_array, mid+1, m, x)

def binarySearch(input_array, x):
    l = len(input_array)
    return search(input_array, 0, l-1, x)
    
if __name__ == "__main__":
    input_array = []
    print("Enter size of array:")
    n = int(input())
    print("Enter the array:")
    for i in range(0, n):
        x = int(input())
        input_array.append(x)
    
    m = int(input("Enter the number to be searched: "))
    index = binarySearch(input_array, m)
    if index == -1:
        print(f"{m} not found")
    else:
        print(f"{m} found at index: {index}")
    