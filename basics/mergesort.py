def debug_print(debug_msg=None, **kwargs):
    if debug_msg:
        print(debug_msg)

    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


def mergesort(array):
    if len(array) <= 1:
        return array

    m = len(array) // 2

    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)


def merge(left, right):
    merged = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        merged += left
    else:
        merged += right

    return merged


if __name__ == "__main__":
    try:
        # Prompt user for input
        input_str = input("Enter numbers, separated by ',': ")

        # Process input and handle invalid input
        input_list = [int(x) for x in input_str.split(",")]

        # Call mergesort function
        sorted_list = mergesort(input_list)

        # Print the sorted list
        print(sorted_list)
    except ValueError as err:
        # Handle invalid input (non-integer values)
        print("Invalid input. Please enter integers separated by commas.")
