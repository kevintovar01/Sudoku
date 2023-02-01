#functions 
from sudoku_proyect import solve, matrix, print_sudoku, check_space
from interface import delete_nums, add, check_numbers, delete_all, entry_values, clear_frame, request_number

#Python
from colorama import Fore
import os
from tkinter import *
from tkinter import ttk


def menu():
    root = Tk()
    global frame

    frame = ttk.Frame(root, padding=100)
    frame.grid()
    Label(frame, text="""

               ▒█▀▀▀█ █░░█ █▀▀▄ █▀▀█ █░█ █░░█ 
               ░▀▀▀▄▄ █░░█ █░░█ █░░█ █▀▄ █░░█ 
               ▒█▄▄▄█ ░▀▀▀ ▀▀▀░ ▀▀▀▀ ▀░▀ ░▀▀▀
              
                  𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙩𝙝𝙚 𝙖𝙢𝙖𝙯𝙞𝙣𝙜 𝙜𝙖𝙢𝙚
         𝙜𝙖𝙢𝙚 𝙩𝙝𝙖𝙩 𝙮𝙤𝙪 𝙝𝙖𝙫𝙚 𝙣𝙚𝙫𝙚𝙧 𝙨𝙚𝙚𝙣 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙬𝙝𝙤𝙡𝙚 𝙡𝙞𝙫𝙚

   """).grid(column=0,row=0)

    Button(frame, text="Play", command=play).grid(column=0,row=1)
    Button(frame, text="Quit", command=root.destroy).grid(column=0,row=4)
    root.mainloop()

  
def play():
    clear_frame(frame)
    sudoku = matrix(frame) 
    solve(sudoku)
    entry_values(frame)
    number = request_number(frame)
    # print(number)
    # interface(sudoku, number)


def interface(sudoku):
    delete_nums(sudoku)
    os.system('clear')
    options(sudoku)


def options(sudoku):
    print(Fore.MAGENTA+"""
  [A]- Fill suduku
  [C]- Check sudoku 
  [S]- Solve sudoku
  [N]- New sudoku
  [E]- Exit
  """)
    print_sudoku(sudoku)
    data2 = input("Enter an option: ").upper()
    choose(data2, sudoku)


def choose(data2, sudoku):
    if data2 == 'A':
        if not add(sudoku):
            os.system('clear')
            options(sudoku)

    elif data2 == 'C':
        check_numbers(sudoku)
        os.system('clear')
        find = check_space(sudoku)
        if not find:
          print("""
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
""")
        
          print_sudoku(sudoku)
        else:
          options(sudoku)

    elif data2 == 'S':
        os.system('clear')
        check_numbers(sudoku)
        solve(sudoku)
        find = check_space(sudoku)
        if not find:
          print(solu)
          print_sudoku(sudoku)
        else:
          delete_all(sudoku) 
          solve(sudoku)
          print(solu)
          print_sudoku(sudoku)

    elif data2 == 'N':
        print("NEW SUDOKU")
        play('1')

    elif data2 == 'E':
        os.system('clear')
        print("""
⠀⡰⠉⠑⠊⠱⡀⠀⠀⢰⡶⣤⡀⠀⢰⣦⠀⠀⢰⡆⠀⣶⡀⣶⠀⢀⣤⢦⡄ 
⡎⠀⢉⠝⠁⠫⡁⠀⠀⢸⡷⠾⠃⢀⣿⣿⡆⠀⢸⡇⠀⣿⢷⣿⠀⠈⠻⢶⣄ 
⠣⢄⣔⣖⣲⣲⠞⠀⠀⠘⠃⠀⠀⠘⠃⠈⠛⠀⠘⠃⠀⠛⠈⠛⠀⠘⠛⠚⠃
    """)
        print("Exit successful")
    else:
        os.system("clear")
        print("ERROR plese digit a valid option")
        options(sudoku)


solu = """

      █▀ █▀█ █░░ █░█ ▀█▀ █ █▀█ █▄░█
      ▄█ █▄█ █▄▄ █▄█ ░█░ █ █▄█ █░▀█

"""


if __name__ == '__main__':
    menu()