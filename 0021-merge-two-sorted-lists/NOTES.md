Node Definition (class ListNode:):

Defines a class named ListNode.
The __init__ method is used to initialize instances of the class.
Each node has two attributes:

val: Represents the value of the node.

next: Points to the next node in the linked list.


Solution Class and Method (class Solution:):

Defines a class named Solution that will contain the method to merge two linked lists.

Method Definition (def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:):

Defines the mergeTwoLists method.
Takes two parameters: list1 and list2, which are the heads of the linked lists to be merged.
Returns the head of the merged linked list.

Create a Dummy Node:

Creates a dummy node with a value of -1. This dummy node is used to simplify the logic when building the merged list.
Initializes the current pointer to point to the dummy node.

Iterating Through Lists (while list1 and list2:):

Enters a loop that continues while both list1 and list2 have nodes.
Inside the loop, the code compares the values of the current nodes in list1 and list2.

Comparing and Appending Nodes:

If the value of the current node in list1 is less than the value of the current node in list2, it means the smallest value should be appended to the merged list.
The current.next pointer is updated to point to the current node in list1, and the list1 pointer is moved to the next node in list1.

Alternate Appending Nodes:

If the value of the current node in list2 is less than or equal to the value in list1, it means the smallest value should be appended to the merged list.
The current.next pointer is updated to point to the current node in list2, and the list2 pointer is moved to the next node in list2.

Moving the Current Pointer:

After appending a node to the merged list, the current pointer is moved forward to the appended node.

Attaching Remaining Nodes:

After the loop, if there are any remaining nodes in either list1 or list2, they are directly appended to the merged list.

Returning the Result:

Returns the head of the merged list. Since the dummy node is not needed in the final result, dummy.next is returned. This is because dummy.next points to the actual start of the merged list.

This code effectively merges two sorted linked lists while maintaining their sorted order. The use of a dummy node and the manipulation of the current pointer simplify the process of building the merged list.​
