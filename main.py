import tkinter as tk

calculation=" "

#add numbers or symbols to calculation
def add_to_calculation(symbol):
   global calculation
   calculation+=str(symbol)
   t_result.delete(1.0, "end")
   t_result.insert(1.0, calculation)

#figure out the calculation
def evaluate_calculation():
   global calculation
   try:
      result=str(eval(calculation))
      calculation=" "
      t_result.delete(1.0, "end")
      t_result.insert(1.0, result)
   except:
      clear_field()
      t_result.insert(1.0, "Error")


#clearing the numbers in the calculation
def clear_field():
   global calculation
   calculation=" "
   t_result.delete(1.0, "end")


#gui settings
root=tk.Tk()
root.geometry('265x275+450+40')

#text box for result
t_result=tk.Text(root, fg='#ffffff', bg='#00c9c9',height=2, width=17, font=("Roboto-Medium.ttf", 24))
t_result.grid(columnspan=5)

#buttons used in calculator
btn=tk.Button(root, text="1",fg='#00c9c9' , command=lambda: add_to_calculation(1), width=2, font=("Roboto-Medium.ttf", 24))
btn.grid(row=2, column=1)

btn2=tk.Button(root, text="2",fg='#00c9c9' , command=lambda: add_to_calculation(2), width=2, font=("Roboto-Medium.ttf", 24))
btn2.grid(row=2, column=2)

btn3=tk.Button(root, text="3",fg='#00c9c9' , command=lambda: add_to_calculation(3), width=2, font=("Roboto-Medium.ttf", 24))
btn3.grid(row=2, column=3)

btn4=tk.Button(root, text="4",fg='#00c9c9' , command=lambda: add_to_calculation(4), width=2, font=("Roboto-Medium.ttf", 24))
btn4.grid(row=3, column=1)

btn5=tk.Button(root, text="5",fg='#00c9c9' , command=lambda: add_to_calculation(5), width=2, font=("Roboto-Medium.ttf", 24))
btn5.grid(row=3, column=2)

btn6=tk.Button(root, text="6",fg='#00c9c9' , command=lambda: add_to_calculation(6), width=2, font=("Roboto-Medium.ttf", 24))
btn6.grid(row=3, column=3)

btn7=tk.Button(root, text="7",fg='#00c9c9' , command=lambda: add_to_calculation(7), width=2, font=("Roboto-Medium.ttf", 24))
btn7.grid(row=4, column=1)

btn8=tk.Button(root, text="8",fg='#00c9c9' , command=lambda: add_to_calculation(8), width=2, font=("Roboto-Medium.ttf", 24))
btn8.grid(row=4, column=2)

btn9=tk.Button(root, text="9",fg='#00c9c9' , command=lambda: add_to_calculation(9), width=2, font=("Roboto-Medium.ttf", 24))
btn9.grid(row=4, column=3)

btn0=tk.Button(root, text="0",fg='#00c9c9' , command=lambda: add_to_calculation(0), width=2, font=("Roboto-Medium.ttf", 24))
btn0.grid(row=5, column=1)

btnPlus=tk.Button(root, text="+",fg='#00c9c9' , command=lambda: add_to_calculation("+"), width=2, font=("Roboto-Medium.ttf", 24))
btnPlus.grid(row=2, column=4)

btnMinus=tk.Button(root, text="-",fg='#00c9c9' , command=lambda: add_to_calculation("-"), width=2, font=("Roboto-Medium.ttf", 24))
btnMinus.grid(row=3, column=4)

btnTimes=tk.Button(root, text="*",fg='#00c9c9' , command=lambda: add_to_calculation("*"), width=2, font=("Roboto-Medium.ttf", 24))
btnTimes.grid(row=4, column=4)

btnDiv=tk.Button(root, text="/",fg='#00c9c9' , command=lambda: add_to_calculation("/"), width=2, font=("Roboto-Medium.ttf", 24))
btnDiv.grid(row=5, column=4)

btnOpen=tk.Button(root, text="(",fg='#00c9c9' , command=lambda: add_to_calculation("("), width=2, font=("Roboto-Medium.ttf", 24))
btnOpen.grid(row=5, column=2)

btnClose=tk.Button(root, text=")",fg='#00c9c9' , command=lambda: add_to_calculation(")"), width=2, font=("Roboto-Medium.ttf", 24))
btnClose.grid(row=5, column=3)

btnDiv=tk.Button(root, text="/",fg='#00c9c9' , command=lambda: add_to_calculation("/"), width=2, font=("Roboto-Medium.ttf", 24))
btnDiv.grid(row=5, column=4)

btnClear=tk.Button(root, text="C",fg='#00c9c9', command=clear_field, width=7, font=("Roboto-Medium.ttf", 24))
btnClear.grid(row=6, column=1, columnspan=3, sticky="W")

btnEqual=tk.Button(root, text="=",fg='#00c9c9' , command=evaluate_calculation, width=7, font=("Roboto-Medium.ttf", 24))
btnEqual.grid(row=6, column=2, columnspan=7, sticky="E")

#loop of gui
root.mainloop()
