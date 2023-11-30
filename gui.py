import tkinter as tk
import main
from tkinter import scrolledtext
from tkinter import messagebox

#functions of gui------------------------------------------------
showtypecode = True
inputs = []
#check functions
def check_six_word():
    current_line, _ = map(int, textbox.index(tk.INSERT).split('.'))
    line_text = textbox.get(f"{current_line}.0", f"{current_line}.end")

    if len(line_text) >= 6:
        textbox.insert(tk.INSERT, '\n')

def check_type_code():
    global showtypecode
    if showtypecode == True:
        showtypecode = False
        textbox.delete("1.0", "end")
    else:
        pass

def validate_input(event):
    # Get the pressed key
    pressed_key = event.char

    # Check if the pressed key is a digit, the Enter key, or the Backspace key
    if pressed_key.isdigit() or pressed_key == '\n':
        check_type_code()
        check_six_word()
    elif event.keysym == 'BackSpace' or event.keysym == 'Return':
        check_type_code()
    else:
        # Block the key by returning 'break'
        return 'break'

#number pad
def button_one():
    check_type_code()
    check_six_word()
    inputs.append(1)
    textbox.insert("end", "1")

def button_two():
    check_type_code()
    check_six_word()
    inputs.append(2)
    textbox.insert("end", "2")

def button_three():
    check_type_code()
    check_six_word()
    inputs.append(3)
    textbox.insert("end", "3")

def button_four():
    check_type_code()
    check_six_word()
    inputs.append(4)
    textbox.insert("end", "4")

def button_five():
    check_type_code()
    check_six_word()
    inputs.append(5)
    textbox.insert("end", "5")

def button_six():
    check_type_code()
    check_six_word()
    inputs.append(6)
    textbox.insert("end", "6")

def button_seven():
    check_type_code()
    check_six_word()
    inputs.append(7)
    textbox.insert("end", "7")

def button_eight():
    check_type_code()
    check_six_word()
    inputs.append(8)
    textbox.insert("end", "8")

def button_nine():
    check_type_code()
    check_six_word()
    inputs.append(9)
    textbox.insert("end", "9")

def button_zero():
    check_type_code()
    check_six_word()
    inputs.append(0)
    textbox.insert("end", "0")

#functional buttons
def button_help():
    output_window = tk.Toplevel(window)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = screen_width - 400  
    y_position = (screen_height - 675) // 2

    # Set the geometry of the popup window
    output_window.geometry(f"+{x_position}+{y_position}")
    output_window.title("Help")
    
    # Create a Text widget with a vertical scrollbar
    output_textbox = scrolledtext.ScrolledText(output_window, height=30, width=120, font=('Arial', 14))

    with open("Help.txt", "r") as file:
        for line in file:
            output_textbox.insert(tk.END, line + '\n')

    output_textbox.config(state='disabled')    
    output_textbox.pack()

def button_enter():
    check_type_code()
    textbox.insert("end", "\n")

def button_clear():
    textbox.delete("1.0", "end")

def button_reset():
    textbox.delete("1.0", "end")
    output_textbox.delete("1.0", tk.END)

    accvalue = tk.Label(codebox, text="null", font=('Arial', 20))
    accvalue.grid(padx=4, pady=4, row=0, column=0, sticky=tk.W+tk.E)
    lastvalue = tk.Label(codebox, text="null", font=('Arial', 20))
    lastvalue.grid(padx=4, pady=4, row=1, column=0, sticky=tk.W+tk.E)

def button_run():
    red_flag = False
    global inputs
    commands = []

    for i in range(0, len(inputs), 6):
        input = inputs[i:i+6]
        command = ""
        if not (len(inputs) == 6 or inputs == '43'):
            red_flag = True
            messagebox.showerror("Error", "Input should be 6 digits or the number 43.")
            command = ""
            break  # Exit the loop on error
        for num in input:
            command += str(num)
        commands.append(command)

    if not red_flag:
        global output_textbox
        output_window = tk.Toplevel(window)
        output_window.title("Output")
        output_textbox = tk.Text(output_window, height=10, width=50, font=('Arial', 14))
        for command in commands:
            output_textbox.insert(tk.END, f"{command}\n")

        accumulator = tk.Label(codebox, text='Accumulator', font=('Arial', 20))
        accumulator.grid(padx=4, pady=4, row=1, column=0, sticky=tk.N)
        accvalue = tk.Label(codebox, text=main.accumulator, font=('Arial', 20))
        accvalue.grid(padx=4, pady=4, row=0, column=0, sticky=tk.W+tk.E)
        lastlabel = tk.Label(codebox, text='ProgramCounter', font=('Arial', 20))
        lastlabel.grid(padx=4, pady=4, row=1, column=0, sticky=tk.N)
        lastvalue = tk.Label(codebox, text=main.program_counter, font=('Arial', 20))
        lastvalue.grid(padx=4, pady=4, row=1, column=0, sticky=tk.W+tk.E)
        output_textbox.pack()

        output_textbox.insert(tk.END, f"\nNew PC: {main.program_counter}")
        output_textbox.insert(tk.END, f"\nAccumulator: {main.accumulator}")

    # for line, value in memory: 
    #     # print line on the left side of the memmenu box
    #     if isinstance(value, command):
    #         v_str = value.operation + value.memLoc
    #         v_int = int(v_str)
    #     else:
    #         v_int = value
    #     # print v_int on the right side of the memmenu box

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x_position}+{y_position}")

window = tk.Tk() #window/root object

center_window(window, 800, 675)
window.geometry("800x675") #geometry

window.title("UV3 Simulator") #title

label = tk.Label(window, text="UV3 Simulator", font=('Arial', 18)) 
label.pack(padx=20, pady=20) #padding

#wireframe parts--------------------------------------------------------
mainframe = tk.Frame(window)
memmenu = tk.Frame(mainframe)
codebox = tk.Frame(mainframe)
controlbox = tk.Frame(mainframe)
#wireframe code and styling
mainframe.columnconfigure(0, weight=1) #mainframe 2x2 2 rows 2 columns
mainframe.columnconfigure(1, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)

memmenu.grid(column=0, rowspan=2)
codebox.grid(column=1, row=0)
controlbox.grid(column=1, row=1)

memmenu.columnconfigure(0, weight=1) #memmenu 1x1 1 column

codebox.columnconfigure(0, weight=1) #codebox 2x1 1 rows 2 columnns
codebox.columnconfigure(1, weight=1)
codebox.rowconfigure(0, weight=1)
codebox.rowconfigure(1, weight=1)

controlbox.columnconfigure(0, weight=1) #controlbox 4x4 4 rows 4 columns
controlbox.columnconfigure(1, weight=1)
controlbox.columnconfigure(2, weight=1)
controlbox.columnconfigure(3, weight=1)
controlbox.rowconfigure(0, weight=1)
controlbox.rowconfigure(1, weight=1)
controlbox.rowconfigure(2, weight=1)
controlbox.rowconfigure(3, weight=1)
controlbox.rowconfigure(4, weight=1)

#memory scroll in memmenu
def on_scroll(*args):
    text_box_list.yview(*args)

text_box_list = tk.Listbox(memmenu, selectmode="SINGLE", height=20, width=25, font=('Arial', 18))
scrollbar = tk.Scrollbar(memmenu, command=on_scroll, width=30)
scrollbar.pack(side="right", fill="y")
text_box_list.pack(side="left", padx=5)

for i in range(1, 101):
    text_box_list.insert("end", f"MemoryNull {i}")
#code boxes and acumulator in code box
textbox = tk.Text(codebox, height=10, width=15, font=('Arial', 18))
textbox.grid(padx=4, pady=4, rowspan=2, column=1, sticky=tk.W+tk.E)
textbox.insert("end", "insert code here") #insert is the function that allows us to change text of a text box
# Bind the event handler to the Text widget
textbox.bind('<KeyPress>', validate_input)

accumulator = tk.Label(codebox, text='Accumulator', font=('Arial', 20))
accumulator.grid(padx=4, pady=4, row=0, column=0, sticky=tk.N)
accvalue = tk.Label(codebox, text='null', font=('Arial', 20))
accvalue.grid(padx=4, pady=4, row=0, column=0, sticky=tk.W+tk.E)
lastlabel = tk.Label(codebox, text='ProgramCounter', font=('Arial', 20))
lastlabel.grid(padx=4, pady=4, row=1, column=0, sticky=tk.N)
lastvalue = tk.Label(codebox, text='null', font=('Arial', 20))
lastvalue.grid(padx=4, pady=4, row=1, column=0, sticky=tk.W+tk.E)
#buttons in conrol box
btn1 = tk.Button(controlbox, height=3, width=6, text="1", font=("Arial", 18), command=button_one)
btn1.grid(padx=2, pady=2, row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(controlbox, height=3, width=6, text="2", font=("Arial", 18), command=button_two)
btn2.grid(padx=2, pady=2, row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(controlbox, height=3, width=6, text="3", font=("Arial", 18), command=button_three)
btn3.grid(padx=2, pady=2, row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(controlbox, height=3, width=6, text="4", font=("Arial", 18), command=button_four)
btn4.grid(padx=2, pady=2, row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(controlbox, height=3, width=6, text="5", font=("Arial", 18), command=button_five)
btn5.grid(padx=2, pady=2, row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(controlbox, height=3, width=6, text="6", font=("Arial", 18), command=button_six)
btn6.grid(padx=2, pady=2, row=1, column=2, sticky=tk.W+tk.E)

btn7 = tk.Button(controlbox, height=3, width=6, text="7", font=("Arial", 18), command=button_seven)
btn7.grid(padx=2, pady=2, row=2, column=0, sticky=tk.W+tk.E)
btn8 = tk.Button(controlbox, height=3, width=6, text="8", font=("Arial", 18), command=button_eight)
btn8.grid(padx=2, pady=2, row=2, column=1, sticky=tk.W+tk.E)
btn9 = tk.Button(controlbox, height=3, width=6, text="9", font=("Arial", 18), command=button_nine)
btn9.grid(padx=2, pady=2, row=2, column=2, sticky=tk.W+tk.E)

btnclear = tk.Button(controlbox, height=3, width=6, text="Clear", font=("Arial", 18), command=button_clear)
btnclear.grid(padx=2, pady=2, row=0, column=3, sticky=tk.W+tk.E)
btnenter = tk.Button(controlbox, height=3, width=6, text="New\nLine", font=("Arial", 18), command=button_enter)
btnenter.grid(padx=2, pady=2, row=1, column=3, sticky=tk.W+tk.E)
btn0 = tk.Button(controlbox, height=3, width=6, text="0", font=("Arial", 18), command=button_zero)
btn0.grid(padx=2, pady=2, row=2, column=3, sticky=tk.W+tk.E)
btnrun = tk.Button(controlbox, height=3, width=6, text="Run", font=("Arial", 18), command=button_run)
btnrun.grid(padx=4, pady=2, row=0, column=4, sticky=tk.W+tk.E)
btnreset = tk.Button(controlbox, height=3, width=6, text="Reset\nMemory", font=("Arial", 18), command=button_reset)
btnreset.grid(padx=4, pady=2, row=1, column=4, sticky=tk.W+tk.E)
btnhelp= tk.Button(controlbox, height=3, width=6, text="Help", font=("Arial", 18), command=button_help)
btnhelp.grid(padx=4, pady=2, row=2, column=4, sticky=tk.W+tk.E)

mainframe.pack(fill='x')

window.mainloop()
