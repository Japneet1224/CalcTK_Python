import tkinter as tk

root = tk.Tk()
root.title('Calculator')
entry = tk.Entry(root, width=20, font=('Lucida Calligraphy', 20), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


button_numbers = []
for i in range(9):
    button = tk.Button(root, text=str(i+1), width=5, font=('Cambria', 14), command=lambda num=i+1: button_click(num))
    button_numbers.append(button)

button_numbers[0].grid(row=3, column=1, pady=5)
button_numbers[1].grid(row=1, column=0, pady=5)
button_numbers[2].grid(row=1, column=1, pady=5)
button_numbers[3].grid(row=1, column=2, pady=5)
button_numbers[4].grid(row=1, column=3, pady=5)
button_numbers[5].grid(row=2, column=0, pady=5)
button_numbers[6].grid(row=2, column=1, pady=5)
button_numbers[7].grid(row=2, column=2, pady=5)
button_numbers[8].grid(row=2, column=3, pady=5)



def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, 'Error')


button_equal = tk.Button(root, text='=', width=5, font=('Cambria', 14), command=calculate)
button_equal.grid(row=6, column=1, pady=5)
button_clear = tk.Button(root, text='C', width=5, font=('Cambria', 14), command=lambda: entry.delete(0, tk.END))
button_clear.grid(row=6, column=2, pady=5)
button_add = tk.Button(root, text='+', width=5, font=('Cambria', 14), command=lambda: button_click('+'))
button_add.grid(row=3, column=2, pady=5)
button_subtract = tk.Button(root, text='-', width=5, font=('Cambria', 14), command=lambda: button_click('-'))
button_subtract.grid(row=3, column=3, pady=5)
button_multiply = tk.Button(root, text='*', width=5, font=('Cambria', 14), command=lambda: button_click('*'))
button_multiply.grid(row=4, column=0, pady=5)
button_divide = tk.Button(root, text='/', width=5, font=('Cambria', 14), command=lambda: button_click('/'))
button_divide.grid(row=4, column=1, pady=5)
button_less = tk.Button(root, text='<', width=5, font=('Cambria', 14), command=lambda: button_click('<'))
button_less.grid(row=5, column=3, pady=5)
button_greater = tk.Button(root, text='>', width=5, font=('Cambria', 14), command=lambda: button_click('>'))
button_greater.grid(row=5, column=2, pady=5)
button_equalto = tk.Button(root, text='==', width=5, font=('Cambria', 14), command=lambda: button_click('=='))
button_equalto.grid(row=5, column=0, pady=5)
button_notequalto = tk.Button(root, text='!=', width=5, font=('Cambria', 14), command=lambda: button_click('!='))
button_notequalto.grid(row=5, column=1, pady=5)
button_lessequal = tk.Button(root, text='<=', width=5, font=('Cambria', 14), command=lambda: button_click('<='))
button_lessequal.grid(row=7, column=2, pady=5)
button_greaterequal = tk.Button(root, text='>=', width=5, font=('Cambria', 14), command=lambda: button_click('>='))
button_greaterequal.grid(row=7, column=1, pady=5)
button_modulo = tk.Button(root, text='%', width=5, font=('Cambria', 14), command=lambda: button_click('%'))
button_modulo.grid(row=4, column=3, pady=5)
button_floor = tk.Button(root, text='//', width=5, font=('Cambria', 14), command=lambda: button_click('//'))
button_floor.grid(row=7, column=0, pady=5)
button_power = tk.Button(root, text='**', width=5, font=('Cambria', 14), command=lambda: button_click('**'))
button_power.grid(row=4, column=2, pady=5)
button_point = tk.Button(root, text='.', width=5, font=('Cambria', 14), command=lambda: button_click('.'))
button_point.grid(row=8, column=0, pady=5)
root.mainloop()