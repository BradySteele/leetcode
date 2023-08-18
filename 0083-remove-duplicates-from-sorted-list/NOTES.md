Initialization: The current pointer is initialized to the head of the linked list. Think of it as a "cursor" that helps us traverse the list node by node.

Traverse the Linked List: A while loop starts, and it keeps running as long as both the current node and its next node are not None. This ensures that we stop when we reach the end of the linked list.

Duplicate Detection: Inside the loop, we compare the value of the current node (current.val) with the value of the next node (current.next.val). This helps us identify whether the two consecutive nodes contain the same value.

Duplicate Removal: If the values are equal, it means a duplicate element has been found. In this case, we need to remove the duplicate node. To do this, we change the next pointer of the current node (current) to point directly to the node after the next node (current.next.next). This effectively skips over the duplicate node and removes it from the linked list.

Distinct Element: If the values of the current and next nodes are not equal, it indicates a distinct element. In this case, we don't need to remove anything. We simply move the current pointer to the next node in the linked list to continue our traversal.

Loop Continuation: The loop keeps running, repeating the process of duplicate detection and removal (if necessary) until we reach the end of the linked list.

Returning the Result: Once the loop completes, we return the head of the linked list. This is the reference to the first node of the modified linked list, which has had duplicates removed.

Summary: The provided code offers a method to remove duplicate elements from a sorted linked list. It uses a pointer (current) to traverse the list. When duplicates are found, it adjusts the pointers to skip over those nodes. The resulting linked list maintains its sorted order, and the modified head is returned as the output.​
