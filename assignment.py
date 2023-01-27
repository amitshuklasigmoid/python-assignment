"""
    My approach :
        1. Finding all border 'O' s and chaging them into 'T' , for this purpose , i have used DFS 
        2. Changing all other 'O' s because they are in surrounded region so changing them into 'X'
        3. Changing all 'T' s into 'O' s back

"""



#Helper function
def solve(board):

    #getting rows and columns size 
    ROWS, COLS = len(board), len(board[0])

    #function for converting 'O' into 'T'
    def capture(r, c):
        if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
            return
        board[r][c] = "T"
        capture(r + 1, c)
        capture(r - 1, c)
        capture(r, c + 1)
        capture(r, c - 1)
    
    # 1. (DFS) Accessing all border 'O' and convert them into 'T' by calling capture function
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                capture(r, c)

    # 2. Capture surrounded regions -> changing 'O' into 'X'
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"

    # 3. Changing all 'T' into 'O'
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "T":
                board[r][c] = "O"


#Main Function
def main():
    rows = int(input("Enter number of rows :"))
    cols = int(input("Enter number of columns :"))

    """Sample Input :

        board = [ [ 'X', 'O', 'X', 'O', 'X', 'X' ],
            [ 'X', 'O', 'X', 'X', 'O', 'X' ],
            [ 'X', 'X', 'X', 'O', 'X', 'X' ],
            [ 'O', 'X', 'X', 'X', 'O', 'X' ],
            [ 'X', 'X', 'X', 'O', 'X', 'O' ],
            [ 'O', 'O', 'X', 'O', 'O', 'O' ] ]
    """
    

    board = []

    print("Enter values row by row")

    for i in range(0,rows):
        temp = input()
        x = temp.split()
        board.append(x)

  

    solve(board)

    print()
    for i in range(rows):
        print(*board[i])

main()