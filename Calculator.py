import tkinter as tk

selected = []
current_result = 0
last_operation = None
equation = ""

def button_clicked(input):
    global current_result, last_operation, equation
    if isinstance(input, int) and 0 <= input <= 9:
        selected.append(input)
        equation += str(input)
        display_label.config(text=equation)

    if input in ["+", "-", "*", "/"]:
        if selected:
            combined_number = sum(d * (10 ** i) for i, d in enumerate(reversed(selected)))
            if last_operation is None:
                current_result = combined_number
            else:
                if last_operation == "+":
                    current_result += combined_number
                elif last_operation == "-":
                    current_result -= combined_number
                elif last_operation == "*":
                    current_result *= combined_number
                elif last_operation == "/":
                    if combined_number != 0:
                        current_result /= combined_number

            selected.clear()
            equation += f" {input} "
            display_label.config(text=equation)
            last_operation = input

def equal_button_clicked():
    global current_result, equation, last_operation
    if selected:
        combined_number = sum(d * (10 ** i) for i, d in enumerate(reversed(selected)))
        if last_operation is not None:
            if last_operation == "+":
                current_result += combined_number
            elif last_operation == "-":
                current_result -= combined_number
            elif last_operation == "*":
                current_result *= combined_number
            elif last_operation == "/":
                if combined_number != 0:
                    current_result /= combined_number

        equation += f" = {current_result}"
        display_label.config(text=equation)
        selected.clear()
        equation = ""
        last_operation = None

root = tk.Tk()
root.geometry('250x400')
root.title("Calculator")

display_frame = tk.Frame(root)
display_frame.pack(pady=10)

display_label = tk.Label(display_frame, text="Result: 0", font=("Arial", 16))
display_label.pack()

button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.5, anchor='center')

for i in range(10):
    button = tk.Button(button_frame, text=f"{i}", command=lambda num=i: button_clicked(num))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)


tk.Frame(root).place(relx=1.0, rely=1.0, anchor='se')

operations = ["+", "-", "*", "/"]
for i, op in enumerate(operations):
    button = tk.Button(tk.Frame(root), text=op, command=lambda oper=op: button_clicked(oper))
    button.grid(row=0, column=i, padx=5, pady=5)

equal_button = tk.Button(tk.Frame(root), text="=", command=equal_button_clicked)
equal_button.grid(row=0, column=len(operations), padx=5, pady=5)

root.mainloop()
