Recursive Height Function: The get_height function is defined within the isBalanced method. This function calculates the height of a subtree while also checking the balance condition.

Base Case for Height Calculation: Inside the get_height function, the first thing checked is if the current node is None. If it is, the subtree has a height of 0.

Recursive Height Calculation: If the node is not None, the function recursively calculates the height of the left subtree (left_height) and the right subtree (right_height) by calling get_height on each subtree's root.

Balance Condition Check: After calculating the heights of the left and right subtrees, the code checks three conditions:

If either the left_height or right_height is -1, it means that one of the subtrees is already unbalanced, so the function returns -1 to indicate this.
If the absolute difference between left_height and right_height is greater than 1, it means the current subtree is unbalanced, so the function returns -1.

Height Calculation and Return: If none of the unbalanced conditions are met, the function returns the maximum of left_height and right_height plus 1, which is the height of the current subtree.

Final Result: In the main isBalanced method, it calls the get_height function on the input root node. If the result of this call is not equal to -1, it means the tree is balanced, and the method returns True. Otherwise, it returns False.

The code employs a bottom-up approach by calculating the height of each subtree and simultaneously checking the balance condition.​
