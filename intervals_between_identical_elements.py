# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Author: KharelUtsav

def intervals_between_identical_elements(arr): #Argument type: list, Return type: list
    """
    Function takes in array as argument and finds the difference between sum of the 
    absolute difference of index of the identical elements. The intervals sum for 
    every element is inserted(in this case appended) at the same index in a newly 
    created local list called new_arr.
    On completion of iteration and logic, the function returns the new_arr list.

    """
    # Creates new local variable new_arr every time function is called and assigns it 
    # with an empty list.
    new_arr = []

    # Using for loop, iterate over the maximum length of for loop.
    for i in range(len(arr)):

        # Create and assign local variable sum
        sum = 0

        # Re-iterates over length of array to find other identical elements in list.
        for j in range(len(arr)):
            # Logic to check if the number at j index is same as in i index.
            # If True: add(sum, abs(i-j))
            if arr[i] == arr[j]: sum += abs(i - j) 
        
        # Append the new sum at the index i
        new_arr.append(sum)

    # Returns local variable new_arr (i.e list containing intervals between identical elements)
    return new_arr


# Test case: 1
arr_1 = [2, 1, 3, 1, 2, 3, 3]
print(intervals_between_identical_elements(arr_1))

# Test case: 2
arr_2 = [10, 5, 10, 10]
print(intervals_between_identical_elements(arr_2))

# Test case: 3
arr_3 = [5, 10, 5, 10, 10, 5]
print(intervals_between_identical_elements(arr_3))

# Test case: 4
arr_4 = [10, "hello", 10, 10, "hello"]
print(intervals_between_identical_elements(arr_4))

