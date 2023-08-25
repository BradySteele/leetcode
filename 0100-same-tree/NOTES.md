Step 1: Handle the base cases:

If both p and q are None, it means you've reached the leaf nodes of both trees, and they are structurally identical. Return True.
If one of the trees is None and the other is not, the trees cannot be the same. Return False.

Step 2: Compare node values and recurse:

If none of the base cases is met, compare the values of the current nodes in trees p and q using p.val and q.val.
If the node values are not equal, the trees are not the same. Return False.
If the node values are equal, continue the comparison by recursively calling isSameTree on the left subtrees (p.left and q.left) and the right subtrees (p.right and q.right).
Combine the results of these recursive calls using the logical and operator:
If both left subtrees and right subtrees are structurally identical and have the same node values, the entire trees are the same. Return True.
If any of the recursive calls returns False, indicating a mismatch, the entire trees are not the same. Return False.​
