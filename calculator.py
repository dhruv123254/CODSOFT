import tkinter as tk

calculation = ""



def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def backspace_button():
    global calculation
    calculation = calculation[:-1]
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
    
root = tk.Tk()
root.title("Calculator")
root.geometry("295x300")
root.config(bg="#000000")

text_result = tk.Text(root, height=2, width=15, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial",14),bg="#808080")
btn_1.grid(row=2, column=0)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial",14),bg="#808080")
btn_2.grid(row=2, column=1)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial",14),bg="#808080")
btn_3.grid(row=2, column=2)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial",14),bg="#808080")
btn_4.grid(row=3, column=0)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial",14),bg="#808080")
btn_5.grid(row=3, column=1)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial",14),bg="#808080")
btn_6.grid(row=3, column=2)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial",14),bg="#808080")
btn_7.grid(row=4, column=0)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial",14),bg="#808080")
btn_8.grid(row=4, column=1)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial",14),bg="#808080")
btn_9.grid(row=4, column=2)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial",14),bg="#808080")
btn_0.grid(row=5, column=1)

btn_add = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial",14),bg="#808080")
btn_add.grid(row=2, column=3)

btn_sub = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial",14),bg="#808080")
btn_sub.grid(row=3, column=3)

btn_mul = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial",14),bg="#808080")
btn_mul.grid(row=4, column=3)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial",14),bg="#808080")
btn_div.grid(row=5, column=3)

btn_brk1 = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial",14),bg="#808080")
btn_brk1.grid(row=5, column=0)

btn_brk2 = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial",14),bg="#808080")
btn_brk2.grid(row=5, column=2)

btn_clr = tk.Button(root, text="C", command=clear_field, width=5, font=("Arial",14),bg="#3782cb")
btn_clr.grid(row=6, column=3)

btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial",14),bg="#ff8b3d")
btn_equal.grid(row=6, column=0, columnspan=2)

btn_bkspc = tk.Button(root, text="B", command=backspace_button, width=5, font=("Arial",14),bg="#808080")
btn_bkspc.grid(row=6, column=2, columnspan=1)

root.mainloop()