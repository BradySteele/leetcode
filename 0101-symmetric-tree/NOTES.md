​1. Main Function Entry (isSymmetric):

The method isSymmetric(self, root: Optional[TreeNode]) -> bool serves as the main entry point for determining the symmetry of the binary tree. It takes the root node of the binary tree as an argument and returns a boolean value that signifies whether the tree is symmetric.

2. Handling the Base Case - Empty Tree:

The code commences by addressing the case where the root node is None. This condition implies that the binary tree is empty, which inherently makes it symmetric. Therefore, the method returns True to handle this base case.

3. Recursively Check Symmetry:
   
If the root node is not None, the code proceeds to the core process of checking symmetry, performed by invoking the helper function checkSymmetry.

4. Helper Function for Symmetry Check (checkSymmetry):
   
The checkSymmetry method undertakes the actual task of determining the symmetry of subtrees. This method compares two subtrees: the left subtree and the right subtree. It receives two parameters, left and right, which represent the corresponding subtrees of the binary tree.

5. Handling Base Cases for Subtrees (checkSymmetry):
   
Within the checkSymmetry method, two crucial scenarios are addressed:

If both left and right subtrees are None, it indicates that both subtrees are empty, making them symmetric. Thus, the method returns True.
If one subtree is None while the other isn't, an asymmetry exists. As a result, the method returns False to signify this lack of symmetry.

6. Recursive Comparison (checkSymmetry):
   
Upon fulfilling the base case checks, the method proceeds to compare the values of the current nodes in the left and right subtrees. If these values match, the method proceeds with the recursive process of assessing the symmetry of the subtrees:

The left subtree of the left node is compared with the right subtree of the right node.

Similarly, the right subtree of the left node is compared with the left subtree of the right node.

The overall outcome of these comparisons and recursive checks determines whether the subtrees are symmetric.
