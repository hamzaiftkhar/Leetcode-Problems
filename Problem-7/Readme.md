
# Merge Sorted Array

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to 0 and should be ignored. `nums2` has a length of `n`.

## Example 1:

**Input:**
```python
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
```
**Output:**
```python
[1,2,2,3,5,6]
```
**Explanation:**
The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from `nums1`.

## Example 2:

**Input:**
```python
nums1 = [1]
m = 1
nums2 = []
n = 0
```
**Output:**
```python
[1]
```
**Explanation:**
The arrays we are merging are [1] and []. The result of the merge is [1].

## Example 3:

**Input:**
```python
nums1 = [0]
m = 0
nums2 = [1]
n = 1
```
**Output:**
```python
[1]
```
**Explanation:**
The arrays we are merging are [] and [1]. The result of the merge is [1]. Note that because `m = 0`, there are no elements in `nums1`. The 0 is only there to ensure the merge result can fit in `nums1`.

## Constraints:

- `nums1.length == m + n`
- `nums2.length == n`
- `0 <= m, n <= 200`
- `1 <= m + n <= 200`
- `-10^9 <= nums1[i], nums2[j] <= 10^9`

## Follow up:
Can you come up with an algorithm that runs in O(m + n) time?

# Solution
## Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The code aims to merge two sorted arrays, `nums1` and `nums2`, into a single sorted array in-place. It leverages the `sorted` function in Python to create a sorted array from the concatenation of the relevant portions of `nums1` and `nums2`. The result is then assigned back to `nums1`, effectively merging the two arrays.

The sorted function is used here to simplify the merging process, as it automatically handles the sorting of the combined elements. However, it's important to note that this approach has a time complexity of O((m + n) * log(m + n)), where `m` is the length of `nums1`, and `n` is the length of `nums2`, due to the sorting operation. While this is a straightforward and concise solution, an alternative optimized approach could achieve the same goal with a time complexity of O(m + n) by merging the arrays in-place without the need for additional space.

## Approach
<!-- Describe your approach to solving the problem. -->
The approach in this code involves merging two sorted arrays, `nums1` and `nums2`, by creating a sorted array from their concatenation. The key steps are as follows:

1. Concatenate the relevant portions of `nums1` and `nums2`: The code uses slicing to extract the first `m` elements from `nums1` and the first `n` elements from `nums2`.

    ```python
    nums1[:m] + nums2[:n]
    ```

2. Sort the concatenated array: The `sorted` function is applied to the concatenated array to create a new array with all elements sorted in non-decreasing order.

    ```python
    sorted(nums1[:m] + nums2[:n])
    ```

3. Update `nums1` in-place: The sorted array is assigned back to the first `m + n` elements of `nums1`, effectively merging the two arrays.

    ```python
    nums1[:m + n] = sorted(nums1[:m] + nums2[:n])
    ```

While this approach is straightforward, it has a time complexity of O((m + n) * log(m + n)), where `m` is the length of `nums1`, and `n` is the length of `nums2`. An alternative optimized approach could achieve the same goal with a time complexity of O(m + n) by merging the arrays in-place without the need for additional space.

## Complexity


### Time Complexity
The time complexity of the code is dominated by the sorting operation performed using the `sorted` function. The concatenation of the two arrays, `nums1[:m] + nums2[:n]`, takes O(m + n) time. Sorting an array of length m + n using the `sorted` function has a time complexity of O((m + n) * log(m + n)). Therefore, the overall time complexity is O((m + n) * log(m + n)).

### Space Complexity
The space complexity is determined by the space required for the sorted array created during the concatenation and sorting. The `sorted(nums1[:m] + nums2[:n])` expression creates a new array to store the sorted result. This additional space is O(m + n). The code modifies `nums1` in-place, so the space used for `nums1` is not counted in the space complexity. Therefore, the overall space complexity is O(m + n).
