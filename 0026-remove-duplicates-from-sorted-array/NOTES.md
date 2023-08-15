Initialization: A variable k is initialized to 0. This variable will be used to keep track of the position up to which the unique elements are placed.

Iteration: The code enters a loop that iterates through the array nums starting from the second element (index 1). This loop is used to compare each element with the previous one to find duplicates.

Comparison: At each step of the loop, the current element nums[i] is compared with the element at the current unique position nums[k].

Checking for Uniqueness: If the current element nums[i] is not equal to the element at nums[k], it means a new unique element is encountered.

Updating Counter and Array: The counter k is incremented to indicate that a new unique element has been found. The value of the new unique element, nums[i], is then placed at the position indicated by the counter k. This step ensures that the array maintains the order of unique elements.

Iteration Continues: The loop continues to iterate through the array, checking and updating for uniqueness for each element.

Count and Length: After the loop finishes, the counter k holds the count of unique elements encountered in the array.

Returning Length: The function returns k + 1, where k is the count of unique elements. By adding 1 to k, the function returns the length of the modified array that contains only unique elements. This is the expected result as required by the problem statement.

In summary, the code effectively removes duplicates in-place from the nums array while maintaining the relative order of unique elements. The approach leverages the k counter to keep track of the position where unique elements should be placed. This solution is efficient as it traverses the array only once and achieves the desired outcome according to the problem's specifications.​
