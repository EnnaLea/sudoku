def is_valid_sudoku(sudoku):
    # Funzione per verificare una riga, colonna o sottogriglia
    def is_valid_group(group):
        return sorted(group) == list("123456789")

    # Verifica righe
    for row in sudoku:
        if not is_valid_group(row):
            return "No"

    # Verifica colonne
    for col in range(9):
        column = [sudoku[row][col] for row in range(9)]
        if not is_valid_group(column):
            return "No"

    # Verifica sottogriglie 3x3
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [
                sudoku[row][col]
                for row in range(box_row, box_row + 3)
                for col in range(box_col, box_col + 3)
            ]
            if not is_valid_group(box):
                return "No"

    return "Yes"


# Lettura input
sudoku = []
for _ in range(9):
    row = input("Enter a row of 9 digits: ")
    if len(row) != 9 or not row.isdigit():
        print("Invalid input. Each row must contain exactly 9 digits.")
        exit()
    sudoku.append(row)

# Validazione Sudoku
result = is_valid_sudoku(sudoku)
print(result)
