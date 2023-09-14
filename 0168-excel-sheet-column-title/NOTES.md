Initialization:

Start by initializing an empty string called result. This string will eventually store the Excel column title.

While Loop:

Enter a while loop that continues as long as columnNumber is greater than 0.

Calculate Remainder:

Calculate the remainder when (columnNumber - 1) is divided by 26. The -1 is used to adjust for Excel column numbering, which starts at 1 (A=1, B=2, ...).
This remainder represents the index of the letter in the alphabet for the current position. For example, if the remainder is 0, it corresponds to 'A'. If the remainder is 1, it corresponds to 'B', and so on.

Convert Remainder to Character:

The line char = chr(ord('A') + remainder) is used to convert the remainder to its corresponding character (letter).
ord('A') gives the ASCII value of 'A', which is 65.
Adding remainder to this ASCII value produces a new ASCII value that corresponds to the desired character.
The chr() function is then used to convert this ASCII value back into a character. So, char now holds the character corresponding to the current position in the Excel column title.

Prepend Character to Result:

The character char is prepended (added to the beginning) of the result string.
This is done because Excel column titles are constructed from right to left. The rightmost character corresponds to the least significant part of the column number.

Update columnNumber:

Update columnNumber by subtracting 1 (to account for Excel's 1-based indexing) and then performing integer division by 26.
This step is crucial for two reasons:
To handle cases where the remainder is 0: When the remainder is 0, it means the letter at the current position should be 'Z'. Subtracting 1 ensures this behavior.
To continue processing the next position: After processing the current character, we move to the next character to the left in the Excel column title.

Repeat Until columnNumber Becomes 0:

The loop continues until columnNumber becomes 0. During each iteration, a character is determined, and the result string is built by prepending characters in the correct order.

Return the Result:

Finally, when the loop completes, the result string contains the Excel column title, and it is returned as the output of the function.
In essence, this code works by repeatedly calculating the character for each position in the Excel column title, starting from the rightmost position and moving left. It uses the remainder of the division to determine the character and updates columnNumber to move to the next position. This process continues until columnNumber becomes 0, resulting in the full Excel column title in the result string.​
