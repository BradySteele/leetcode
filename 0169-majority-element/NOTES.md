Boyer-Moore Voting Algorithm:

Initialization:

We start by initializing two variables: candidate and count.
candidate will represent the potential majority element, and count will keep track of how many times this potential majority element has been encountered.

Step 1: Finding the Potential Candidate:

We iterate through the nums array, one element at a time.
If the count is 0, it means we have not found a potential candidate yet, so we set the current element as the candidate. This is because if there is a majority element, it will eventually outweigh the other elements.
If the current element is the same as the candidate, we increment the count. This suggests that we have found another instance of the same element.
If the current element is different from the candidate, we decrement the count. This means we have encountered a different element, and it "cancels out" one count of the potential candidate.
The goal of this step is to identify a potential majority candidate while considering the possibility of its count being canceled out by other elements.

Step 2: Verifying the Candidate:

After the first pass through the array, we may have a potential candidate, but we need to verify if it's indeed the majority element.
To do this, we reset the count to 0 and iterate through the array again.
In this second pass, we count how many times the potential candidate appears in the array.
If the count of the candidate is greater than half the length of the nums array (i.e., len(nums) // 2), then it is considered the majority element.

Step 3: Returning the Result:

If the count of the candidate is greater than len(nums) // 2, we return the candidate as the majority element.
If the count is not greater than half, we do not return anything, as the problem statement guarantees that a majority element always exists.
In essence, this algorithm efficiently identifies a potential majority candidate and then verifies its majority status in a two-pass process. It does this by maintaining a balance of counts and efficiently narrows down the potential majority element. The final result is the majority element, or None if there is no majority element. The algorithm runs in linear time (O(n)) and uses only constant space (O(1)), making it efficient.​
