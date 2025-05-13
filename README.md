Algo_Task
A brief but mandatory documentation for my algo task at uni.
3rd Task: Distinct Values in Array
This task involves writing algorithms to count the number of distinct values in a zero-indexed array A consisting of N integers. Below are three different approaches to solve this problem.
1st Algorithm Explanation: Distinct Values Using Bubble Sort (#1)
This algorithm counts the number of distinct values in a zero-indexed array A by first sorting the array using bubble sort and then counting unique adjacent elements.
Algorithm Steps:

Check if the array is empty; return 0 if true.

Sort the array using bubble sort by comparing adjacent elements and swapping if they are in the wrong order.

Iterate through the sorted array, incrementing a counter when a new distinct value is encountered.

Return the total count of distinct values.


Complexity Analysis:

Time Complexity: O(n²) - Sorting with bubble sort takes O(n²), and the subsequent distinct count pass takes O(n), dominated by the sorting step.

Space Complexity: O(1) - Only a constant amount of extra space is used for variables.


Example Usage:
array = [2, 1, 1, 2, 3, 1]
result = distinct_first(array)
print("Number of distinct values:", result)  # Output: 3

2nd Algorithm Explanation: Distinct Values Using Recursion (#2)
This algorithm counts the number of distinct values in a zero-indexed array A using a recursive approach with a dictionary to track unique elements.
Algorithm Steps:

Initialize a dictionary and index (defaulting to the last element) if not provided.

Use recursion to process each element from the end to the start of the array.

Add an element to the dictionary if it’s not already present.

Return the size of the dictionary as the count of distinct values when the base case (index < 0) is reached.


Complexity Analysis:

Time Complexity: O(n) - Each element is processed once, with dictionary operations being O(1) on average.

Space Complexity: O(n) - The dictionary stores up to n distinct elements.


Example Usage:
array = [2, 1, 1, 2, 3, 1]
result = distinct_recursion_second(array)
print("Number of distinct values:", result)  # Output: 3

Algorithm Explanation: Distinct Values Using List (#3)
This algorithm counts the number of distinct values in a zero-indexed array A by building a list of unique elements.
Algorithm Steps:

Initialize an empty list to store distinct values.

Iterate through the array, adding each element to the list if it’s not already present.

Return the length of the list as the count of distinct values.


Complexity Analysis:

Time Complexity: O(n²) - Checking if an element exists in the list takes O(n) for each of the n elements.

Space Complexity: O(k) - Where k is the number of distinct elements (up to n).


Example Usage:
array = [2, 1, 1, 2, 3, 1]
result = distinct_first(array)  # Note: Function name reused, consider renaming
print("Number of distinct values:", result)  # Output: 3

Pseudo Code for 1st Algo :
algorithm distinct_first(A):
    if A is empty:
        return 0
    
    n = length of A
    for i from 0 to n-1:
        swapped = false
        for j from 0 to n-i-2:
            if A[j] > A[j+1]:
                swap A[j] with A[j+1]
                swapped = true
        if not swapped:
            break
    
    count = 1
    for i from 0 to n-2:
        if A[i] != A[i+1]:
            count = count + 1
    return count

Pseudo Code for 2nd Algo :
algorithm distinct_recursion_second(A, index, dictionary):
    if index is None:
        index = length of A - 1
    if dictionary is None:
        dictionary = empty dictionary
    
    if index < 0:
        return length of dictionary
    
    if A[index] not in dictionary:
        dictionary[A[index]] = index
    
    return distinct_recursion_second(A, index - 1, dictionary)

Pseudo Code for 3rd Algo :
algorithm distinct_first(A):
    unique_list = empty list
    for each item in A:
        if item not in unique_list:
            append item to unique_list
    return length of unique_list

Comparison between all Algo's Time Complexity :



Algorithm
Time Complexity
Description



First Algorithm (Bubble Sort)
O(n²)
Uses bubble sort for sorting, followed by a linear pass to count distinct values.


Second Algorithm (Recursion)
O(n)
Recursively processes each element with O(1) dictionary operations.


Third Algorithm (List)
O(n²)
Checks list membership for each element, leading to quadratic complexity.


Best Algorithm: Second Algorithm (O(n))
