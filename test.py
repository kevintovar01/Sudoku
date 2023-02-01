from tkinter import *
window = Tk()
window.title("Matrix")
window.geometry("650x500+120+120")
window.configure(bg='bisque2')
window.resizable(False, False)
m1 = StringVar()

Label(window, text="Enter matrix :", font=('arial', 10, 'bold'), 
bg="bisque2").grid(row=0, column=0)

rows, cols = (10,10)
for i in range(1, rows):
  for j in range(1, cols):
        entry = Entry(window, textvariable ="",width=3)
        entry.grid(row=i, column=j)
   
# button= Button(window,text="Submit", bg='bisque3', width=15)
# button.grid(row=10, column=5)
window.mainloop()