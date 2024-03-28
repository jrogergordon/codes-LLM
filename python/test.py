

def n_knights(n):
        

    def place_knights():
        col = 0
        while col < n:
            # Fill every third column using pattern A
            for row in range(0, n, 2):
                chessboard[row][col] = 1
            col += 3

            if col < n:  # Fill every third column using pattern B
                for row in range(1, n, 2):
                    chessboard[row][col] = 1
            col += 3

    chessboard = [[0] * n for _ in range(n)]
    place_knights()
    return chessboard

solution = n_knights(4)  # Example for an 8x8 board
for row in solution:
    print(row)