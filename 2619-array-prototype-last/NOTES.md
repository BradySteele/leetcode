if (this.length === 0): This line checks if the length of the array (referred to as this) is equal to 0. In JavaScript, the length property of an array indicates how many elements are in it.

return -1: If the array is empty (length is 0), the function returns -1. This is the specified behavior when there are no elements in the array.

else: If the array is not empty (length is not 0), the code inside the else block is executed.

return this[this.length - 1]: This line returns the last element of the array. Here's how it works:

this.length gets the length of the array.

this.length - 1 calculates the index of the last element since array indices are 0-based.

this[this.length - 1] accesses the element at the calculated index and returns it as the result of the last function.

So, to summarize, this code adds a last method to all JavaScript arrays. When you call array.last(), it checks if the array is empty and returns -1 if it is. Otherwise, it returns the last element of the array.
