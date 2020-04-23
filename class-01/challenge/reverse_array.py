def reverse_array(input_array):
    l = len(input_array)
    j = l - 1
    if l == 0:
        return input_array
    else:
        for i in range(0, int(l/2)):
            x = input_array[i]
            input_array[i] = input_array[j]
            input_array[j] = x
            j -= 1

    return input_array        


if __name__ == "__main__":
    input_array = []
    print("Enter size of array:")
    n = int(input())
    print("Enter the array:")
    for i in range(0, n):
        x = int(input())
        input_array.append(x)
    print(f"array before reversing: {input_array}")
    input_array = reverse_array(input_array)
    print(f"array after reversing: {input_array}")

