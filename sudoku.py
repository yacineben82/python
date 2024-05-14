"""
number_lines = 10
for i in range(0 , number_lines + 1):
    for j in range(i + 1 , number_lines + 1):
        print( j , end = " ")
    print("")
"""
"""
for i in range(1, 11):  # boucle pour chaque ligne
    for j in range(1, 11):  # boucle pour chaque nombre dans la ligne
        print(j, end='\t')  # affiche le nombre suivi d'une tabulation
    print()  # passe à la ligne suivante
"""
"""
def afficher_grille_sudoku(grille):
    for i in range(len(grille)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(grille[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if grille[i][j] == 0:
                print(". ", end="")
            else:
                print(str(grille[i][j]) + " ", end="")
            if j == 8:
                print()

# Exemple de grille de Sudoku
grille_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

afficher_grille_sudoku(grille_sudoku)
"""
import random


def generate_sudoku_grid():
    grid = [[0] * 9 for _ in range(9)]  # Crée une grille vide

    # Remplir la grille avec des nombres aléatoires
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in range(9):
        random.shuffle(numbers)  # Mélange les nombres pour chaque ligne
        for col in range(9):
            grid[row][col] = numbers[col]

    return grid


def display_sudoku_grid(grid):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("| ", end="")
            print(grid[row][col], end=" ")
        print()


# Générer une nouvelle grille de Sudoku
grid = generate_sudoku_grid()

# Afficher la grille
display_sudoku_grid(grid)
