import random
from colorama import Fore

n = 9


def matrix():
    sudoku = [[" " for i in range(n)] for i in range(n)]  #list comprehention
    mylist = [i for i in range(1, n+1)]
    for i in range(1):  #row 0
        for j in range(n):
            randoms = random.choice(mylist)
            mylist.remove(randoms)
            sudoku[i][j] = randoms
    return sudoku


def solve(sudoku):
    find = check_space(sudoku)
    if not find:
        return True
    else:
        row, column = find  #find = (1, 0) of type tupla

    col = [objects[column] for objects in sudoku]

    for num in range(1, n+1):  #this range is 1 to 9.
        if check_nums(sudoku, num, (row, column), col):  #of type bool
            sudoku[row][column] = num

            if solve(sudoku): #llamado anterior de la funcion , en caso de que sea falso
                return True
            sudoku[row][column] = " "
    return False


def check_nums(sudoku, num, coords, col):  #coords = (1,0) coords = (fila,columna)
    if num in sudoku[coords[0]] or num in col:
        return False

    box = 3

    box_x = coords[1] // box  #coords= (1, 0)
    box_y = coords[0] // box

    for i in range(box_y * box, box_y * box + box):  #0, 4
        for j in range(box_x * box, box_x * box + box):  #0, 4
            if sudoku[i][j] == num:
                return False
    return True


def check_space(matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == " ":
                return (i, j)
    return None
  

def print_sudoku(sudoku):
    nums = [str(i) for i in range(n)]
    print(Fore.MAGENTA + f"    {'   '.join(nums)} ")
    for i in range(n):
        if i % 3 == 0:
            print(Fore.BLUE + "   +", "-" * 9, "+", "-" * 9, "+", "-" * 9, "+")
        print(Fore.MAGENTA + f"{i}", Fore.BLUE + " |", Fore.WHITE + ' | '.join(map(str, sudoku[i])), Fore.BLUE + "|")
    print(Fore.BLUE + "   +", "-" * 9, "+", "-" * 9, "+", "-" * 9, "+")