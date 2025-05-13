# Algo_Task: Distinct Values in Array  
A brief but mandatory documentation for my algo task at uni.

---

## 1st Algorithm Explanation: Brute Force Comparison (#1)

This algorithm counts the number of distinct elements in an array using a basic brute-force approach.

### Algorithm Steps:

1. Initialize a counter `distinctCount` to zero.  
2. Loop through each element `i` in the array.  
3. For each `i`, check whether it has appeared before by looping from `0` to `i-1`.  
4. If it has not appeared before, increment `distinctCount`.  
5. Continue this process for all elements in the array.  
6. Return `distinctCount` at the end.

### Complexity Analysis:

- **Time Complexity:** O(n²) – Two nested loops are used, where each element is compared with all previous elements.  
- **Space Complexity:** O(1) – No extra space is used apart from a few variables.

### Example Usage:

```cpp
#include <iostream>
#include <vector>
using namespace std;

int countDistinctBruteForce(const vector<int>& v) {
    int distinctCount = 0;
    for (int i = 0; i < v.size(); ++i) {
        bool isNew = true;
        for (int j = 0; j < i; ++j) {
            if (v[i] == v[j]) {
                isNew = false;
                break;
            }
        }
        if (isNew) {
            ++distinctCount;
        }
    }
    return distinctCount;
}

int main() {
    vector<int> nums = {1, 2, 2, 3, 4, 4, 5};
    cout << "Distinct values (Brute Force): " << countDistinctBruteForce(nums) << endl;
    return 0;
}
```

---

## 2nd Algorithm Explanation: Sorting-Based Counting (#2)

This algorithm first sorts the array and then counts distinct values by checking adjacent elements.

### Algorithm Steps:

1. Sort the input array using Bubble Sort.  
2. Initialize a counter `distinctCount` to 1.  
3. Iterate through the sorted array starting from the second element.  
4. If the current element is different from the previous one, increment `distinctCount`.  
5. Return `distinctCount`.

### Complexity Analysis:

- **Time Complexity:** O(n²) – Due to Bubble Sort being used.  
- **Space Complexity:** O(1) – Sorting is done in-place.

### Example Usage:

```cpp
#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& v) {
    int n = v.size();
    for (int i = 0; i < n - 1; ++i) {
        for (int j = 0; j < n - i - 1; ++j) {
            if (v[j] > v[j + 1]) {
                swap(v[j], v[j + 1]);
            }
        }
    }
}

int countDistinctSorted(vector<int> v) {
    bubbleSort(v);
    int distinctCount = 1;
    for (int i = 1; i < v.size(); ++i) {
        if (v[i] != v[i - 1]) {
            ++distinctCount;
        }
    }
    return distinctCount;
}

int main() {
    vector<int> nums = {1, 2, 2, 3, 4, 4, 5};
    cout << "Distinct values (Sorted): " << countDistinctSorted(nums) << endl;
    return 0;
}
```

---

## 3rd Algorithm Explanation: Hash Map (Using Set) (#3)

This algorithm uses a set to automatically eliminate duplicates and count distinct values.

### Algorithm Steps:

1. Initialize an empty set `s`.  
2. Iterate through each element of the array.  
3. Insert each element into the set.  
4. After all insertions, return the size of the set.

### Complexity Analysis:

- **Time Complexity:** O(n) – Average-case complexity with `unordered_set`.  
- **Space Complexity:** O(n) – To store the elements in the set.

### Example Usage:

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int countDistinctSet(const vector<int>& v) {
    unordered_set<int> s;
    for (int val : v) {
        s.insert(val);
    }
    return s.size();
}

int main() {
    vector<int> nums = {1, 2, 2, 3, 4, 4, 5};
    cout << "Distinct values (Set): " << countDistinctSet(nums) << endl;
    return 0;
}
```

---

## Pseudo Code for 1st Algo:

```
algorithm count_distinct_brute_force(v):
    distinctCount = 0
    for i from 0 to v.size() - 1:
        isNew = true
        for j from 0 to i - 1:
            if v[i] == v[j]:
                isNew = false
                break
        if isNew:
            distinctCount += 1
    return distinctCount
```

---

## Pseudo Code for 2nd Algo:

```
algorithm count_distinct_sorted(v):
    bubble_sort(v)
    distinctCount = 1
    for i from 1 to v.size() - 1:
        if v[i] != v[i - 1]:
            distinctCount += 1
    return distinctCount
```

---

## Pseudo Code for 3rd Algo:

```
algorithm count_distinct_set(v):
    s = empty set
    for i from 0 to v.size() - 1:
        insert v[i] into s
    return size of s
```

---

## Comparison between all Algo's Time Complexity:

| Algorithm         | Time Complexity | Description                                                                 |
|-------------------|------------------|-----------------------------------------------------------------------------|
| First Algorithm    | O(n²)           | Brute-force approach comparing each element with all previous ones.        |
| Second Algorithm   | O(n²)           | Uses Bubble Sort. Can be reduced to O(n log n) with faster sorting method. |
| Third Algorithm    | O(n)            | Uses `unordered_set` for fast lookups and insertions.                      |

**Best Algorithm:** ✅ Third Algorithm (O(n))

---
