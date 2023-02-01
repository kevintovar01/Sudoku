#functions
from sudoku_proyect import print_sudoku, check_nums



#tkinter
from tkinter import *

#python
import random
import os

positions = []
user_coord = []

def clear_frame(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()


def request_number(frame):
    number = entry.get()
    clear_frame(frame)
    return int(number)


def entry_values(frame):
    global label
    global entry
    label=Label(frame, text="test")
    label.pack()
    
    entry = Entry(frame, width=40)
    entry.get()
    entry.focus_set()
    entry.pack()  
    quit_frame = Button(frame, text="next", command=lambda:request_number(frame))
    quit_frame.pack()

  
def delete_nums(sudoku, number):
    global user_coord, positions
    user_coord = []
    positions = []
    try:  #controlar Errores
        positions = [(i,j) for i in range(9) for j in range(9)]

        for i in range(number):
            delete = random.randint(0, len(positions)-1)
            row, column = positions[delete]
            sudoku[row][column] = " "
            positions.remove((row, column))

    except ValueError:
        os.system("clear")
        print("Please enter a valid number")
        delete_nums(sudoku)
    return sudoku


def add(sudoku):
    os.system('clear')
    print_sudoku(sudoku)
    print("""
        [A]- Add
        [D]- Delete
        [M]- Modify 
        [R]- Return
    """)
    enter = input("Enter an option: ").upper()

    if enter == 'R':
        return False

    try:  #controla errores
        if enter == 'A' or enter == 'M':
            row, column = map(int, input("Enter coords: ").split())
            row, column = check(row, column)
            num = int(input("input the number you want put there: "))
            while num not in range(1, 10):
                num = int(input("ONLY NUMBERS FOR 1 TO 16: "))
            sudoku[row][column] = num
            add(sudoku)
        elif enter == 'D':
            row, column = map(int,input("Enter coords to delete a number: ").split())
            row, column = check(row, column)
            sudoku[row][column] = " "
            add(sudoku)
        else:
            add(sudoku)
    except ValueError:
        add(sudoku)


def check(row, column):
    while row not in range(9) or column not in range(9):
        row, column = map(int, input("Enter a valid coords: ").split())

    while (row, column) in positions:
        print("This coords can't be alterated")
        row, column = map(int, input("Enter coords: ").split())

    if (row, column) not in user_coord:
        user_coord.append((row, column))
    return (row, column)


def check_numbers(sudoku):
    for tupla in user_coord:
        row, column = tupla
        num = sudoku[row][column]
        sudoku[row][column] = " "
        col = [colum[column] for colum in sudoku]

        if check_nums(sudoku, num, (row, column), col):
            sudoku[row][column] = num
         
        else:
            sudoku[row][column] = ' ' 


def delete_all(sudoku):
    global user_coord

    for tupla in user_coord:
      row, column = tupla
      sudoku[row][column] = " "