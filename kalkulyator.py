import tkinter as tk


def get_values():
    nam1 = int(namber1_entry.get())
    nam2 = int(namber2_entry.get())
    return nam1, nam2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    nam1, nam2 = get_values()
    res = nam1 + nam2
    insert_values(res)


def sab():
    nam1, nam2 = get_values()
    res = nam1 - nam2
    insert_values(res)


def mul():
    nam1, nam2 = get_values()
    res = nam1 * nam2
    insert_values(res)


def div():
    nam1, nam2 = get_values()
    res = nam1 / nam2
    insert_values(res)


window = tk.Tk()
window.title('Калькулятор')
window.geometry("800x500")
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=3, height=3, command=add)
button_add.place(x=100, y=400)
button_sab = tk.Button(window, text='-', width=3, height=3, command=sab)
button_sab.place(x=200, y=400)
button_mul = tk.Button(window, text='*', width=3, height=3, command=mul)
button_mul.place(x=300, y=400)
button_div = tk.Button(window, text='/', width=3, height=3, command=div)
button_div.place(x=400, y=400)
namber1_entry = tk.Entry(window, width=100)
namber1_entry.place(x=100, y=100)
namber2_entry = tk.Entry(window, width=100)
namber2_entry.place(x=100, y=200)
answer_entry = tk.Entry(window, width=100)
answer_entry.place(x=100, y=300)
namber1 = tk.Label(window, text='Введите первое число:')
namber1.place(x=100, y=75)
namber2 = tk.Label(window, text='Введите второе число:')
namber2.place(x=100, y=175)
answer = tk.Label(window, text='Ответ:')
answer.place(x=100, y=275)
window.mainloop()
