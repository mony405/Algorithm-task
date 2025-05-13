# Distinct Values in Array - Python Algorithms

This repository contains different algorithms to count the number of distinct values in an array. Below are the three different approaches implemented:

---

## Algorithm 1: Bubble Sort with Distinct Count (`distinct_first`)

This algorithm first sorts the array using the Bubble Sort technique and then counts the number of distinct elements by comparing adjacent elements.

### Algorithm Steps:

1. Perform **Bubble Sort** on the array to sort it.
2. Loop through the sorted array and compare each element with the next one.  
3. If the elements are different, increment the distinct counter.
4. Return the final count of distinct elements.

### Time Complexity:

- **Time Complexity:** O(n²) – Due to Bubble Sort.  
- **Space Complexity:** O(1) – In-place sorting and constant space usage.

### Example Usage:

```python
def distinct_first(array):
    if not array:
        return 0
    # first we sort the array with bubble sort
    length = len(array)
    for i in range(length):
        swap = False
        for j in range(0, length - i - 1):  # -1 to avoid index out of range
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap = True
        if not swap:
            break
    # loop to count the distinct elements
    count = 1
    for i in range(length - 1):
        if array[i] != array[i + 1]:
            count += 1
    return count

# Test the algorithm
nums = [1, 2, 2, 3, 4, 4, 5]
print("Distinct values (Bubble Sort):", distinct_first(nums))
```

---

## Algorithm 2: Recursion with Dictionary (`distinct_recursion_second`)

This algorithm uses recursion and a dictionary to count the number of distinct values in the array.

### Algorithm Steps:

1. Start from the last element of the array and traverse backward.
2. Use a dictionary (`dicto`) to store the elements that have already been seen.
3. If the element is not in the dictionary, add it.
4. Once the recursion reaches the base case (first element), return the length of the dictionary.

### Time Complexity:

- **Time Complexity:** O(n) – Each element is visited once.  
- **Space Complexity:** O(n) – The dictionary stores up to `n` elements.

### Example Usage:

```python
def distinct_recursion_second(array, index=None, dicto=None):
    if index is None:
        index = len(array) - 1

    if dicto is None:
        dicto = {}

    if index < 0:  # Base case
        return len(dicto)

    if array[index] not in dicto:
        dicto[array[index]] = index

    return distinct_recursion_second(array, index - 1, dicto)

# Test the algorithm
nums = [1, 2, 2, 3, 4, 4, 5]
print("Distinct values (Recursion with Dictionary):", distinct_recursion_second(nums))
```

---

## Algorithm 3: List with Append (`distinct_third`)

This algorithm uses a list to store distinct elements by checking if each element is already present before appending it.

### Algorithm Steps:

1. Initialize an empty list `listo` to store distinct elements.
2. Iterate over each element in the array.
3. If the element is not already in the list, append it to the list.
4. Return the length of the list, which will contain only distinct values.

### Time Complexity:

- **Time Complexity:** O(n²) – Due to the check `item not in listo` for each element.  
- **Space Complexity:** O(n) – The list stores distinct elements.

### Example Usage:

```python
def distinct_third(array):
    listo = []
    for item in array:
        if item not in listo:
            listo.append(item)
    return len(listo)

# Test the algorithm
nums = [1, 2, 2, 3, 4, 4, 5]
print("Distinct values (List Append):", distinct_third(nums))
```

---

## Pseudo Code

### Algorithm 1: Bubble Sort with Distinct Count
```
function distinct_first(array):
    if array is empty:
        return 0
    sort array using bubble sort
    count = 1
    for i = 0 to length of array - 2:
        if array[i] != array[i + 1]:
            increment count
    return count
```

### Algorithm 2: Recursion with Dictionary
```
function distinct_recursion_second(array, index, dicto):
    if index < 0:
        return length of dicto
    if array[index] not in dicto:
        dicto[array[index]] = index
    return distinct_recursion_second(array, index - 1, dicto)
```

### Algorithm 3: List with Append
```
function distinct_third(array):
    create empty list listo
    for each item in array:
        if item not in listo:
            append item to listo
    return length of listo
```

---

## Comparison of Algorithm Time Complexity:

| Algorithm                           | Time Complexity | Description                                                             |
|-------------------------------------|-----------------|-------------------------------------------------------------------------|
| **Bubble Sort with Distinct Count** | O(n²)           | Sorting array with Bubble Sort and then counting distinct elements.    |
| **Recursion with Dictionary**       | O(n)            | Recursively traversing array and using dictionary for uniqueness.      |
| **List with Append**                | O(n²)           | Checking and appending distinct elements using a list.                  |

**Best Algorithm:** The **Recursion with Dictionary** approach is the most efficient with a time complexity of O(n).
