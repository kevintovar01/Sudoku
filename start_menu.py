#functions 
from sudoku_proyect import solve, matrix, print_sudoku, check_space
from interface import delete_nums, add, check_numbers, delete_all

#Python
from colorama import Fore
import os


def menu():
    print(Fore.BLUE+"""

              ▒█▀▀▀█ █░░█ █▀▀▄ █▀▀█ █░█ █░░█ 
              ░▀▀▀▄▄ █░░█ █░░█ █░░█ █▀▄ █░░█ 
              ▒█▄▄▄█ ░▀▀▀ ▀▀▀░ ▀▀▀▀ ▀░▀ ░▀▀▀
              
                 𝙒𝙚𝙡𝙘𝙤𝙢𝙤 𝙩𝙤 𝙩𝙝𝙚 𝙖𝙢𝙖𝙯𝙞𝙣𝙜 𝙜𝙖𝙢𝙚
        𝙜𝙖𝙢𝙚 𝙩𝙝𝙖𝙩 𝙮𝙤𝙪 𝙝𝙖𝙫𝙚 𝙣𝙚𝙫𝙚𝙧 𝙨𝙚𝙚𝙣 𝙞𝙣 𝙮𝙤𝙪𝙧 𝙬𝙝𝙤𝙡𝙚 𝙡𝙞𝙫𝙚
                              ★
                              ★
                         [1]- Play
                         [2]- Exit

  """)
    data = (input("Enter an option: "))
    play(data)
  

def play(data):
    if data == '1':
        sudoku = matrix() 
        solve(sudoku)
        interface(sudoku)
    elif data == '2':
        os.system('clear')
        print("Exit successful")
    else:
        os.system('clear')
        print("ERROR plese digit a valid option")
        menu()


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