import os
from tkinter import *

main = Tk()

base_dir = os.path.dirname(os.path.abspath(__file__))
scripts_dir = os.path.join(base_dir, "TKINTERAPP", "Include", "scripts")
scripts_list = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]

left_frame = Frame(main)
left_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")

listbox = Listbox(left_frame)
listbox.pack(fill="both", expand=True)
for script in scripts_list:
    listbox.insert(END, script)

input_frame = Frame(left_frame, pady=10)
input_frame.pack(side="bottom", fill="x")

input_field = Entry(input_frame)
input_field.pack(fill="x", padx=10)

right_frame = Frame(main)
right_frame.grid(row=0, column=1, sticky="nsew")

run_button = Button(right_frame, text="Run", bg="green", fg="white")
run_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

stop_button = Button(right_frame, text="Stop", bg="red", fg="white")
stop_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

console_log = Text(right_frame)
console_log.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

main.mainloop()
