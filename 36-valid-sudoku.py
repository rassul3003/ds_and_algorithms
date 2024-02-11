"""
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
-----
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:
---------
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
---------
Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:
-----------
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# Time Complexity O(n^2)
from collections import defaultdict
def isValidSudoku(board):
    # Create dictionaries to keep track of numbers in rows, columns, and sub-boxes
    rows = defaultdict(set)
    columns = defaultdict(set)
    sub_boxes = defaultdict(set)

    # Iterate through each cell in the 9x9 Sudoku board
    for row in range(9):
        for col in range(9):
            num = board[row][col]

            # Skip empty cells represented by "."
            if num == ".":
                continue

            # Check if the current number violates Sudoku rules
            if (num in rows[row] or 
                num in columns[col] or 
                num in sub_boxes[(row // 3, col // 3)]):
                return False

            # Update sets to keep track of encountered numbers
            rows[row].add(num)
            columns[col].add(num)
            sub_boxes[(row // 3, col // 3)].add(num)

    # If all cells satisfy Sudoku rules, the board is valid
    return True
    

print(isValidSudoku(board))