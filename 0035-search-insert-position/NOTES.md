## Binary Search Algorithm Explanation

### Inputs:
- `nums`: A sorted array of distinct integers.
- `target`: The target value to search for or insert.

### Output:
- If the `target` is found in the `nums` array, return its index.
- If the `target` is not found, return the index where it would be inserted.

### Algorithm Steps:

1. Initialize two pointers:
   - `left` = 0, pointing to the first element of the array.
   - `right` = length of `nums` - 1, pointing to the last element of the array.

2. Enter a loop while `left` is less than or equal to `right`:
   - Calculate the middle index as `mid = left + (right - left) // 2`.

3. Check the value at the middle index `nums[mid]`:
   - If `nums[mid]` is equal to `target`, return `mid` as the index where `target` is found.

4. If `nums[mid]` is less than `target`, update `left = mid + 1` to search in the right half of the remaining array.
   - This is because we have already checked `mid`, so we can exclude it from further consideration.

5. If `nums[mid]` is greater than `target`, update `right = mid - 1` to search in the left half of the remaining array.
   - Similarly, we exclude `mid` from further consideration.

6. Repeat steps 2-5 until `left` becomes greater than `right`.

7. When the loop ends, return `left` as the index where `target` would be inserted.
   - This is because `left` now points to the smallest element in the remaining range that is greater than `target`.

### Runtime Complexity:
- The algorithm reduces the search range by half with each iteration, resulting in a logarithmic growth rate.
- Therefore, the runtime complexity of this algorithm is O(log n), where `n` is the length of the `nums` array.
​
