from tkinter import *

main = Tk()

main.geometry("500x500")

left_frame = Frame(main)
left_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")

listbox = Listbox(left_frame)
listbox.pack(fill="both", expand=True)
for item in ["Item 1", "Item 2", "Item 3"]:
    listbox.insert(END, item)

input_frame = Frame(left_frame, pady=10)
input_frame.pack(side="bottom", fill="x")

input_field = Entry(input_frame)
input_field.pack(fill="x", padx=10)

right_frame = Frame(main)
right_frame.grid(row=0, column=1, sticky="nsew")

for i in range(4):
    button = Button(right_frame, text=f"Button {i+1}")
    button.grid(row=0, column=i, padx=10, pady=10)

console_log = Text(right_frame)
console_log.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

main.mainloop()
