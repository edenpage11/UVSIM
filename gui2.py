import customtkinter as ctk
import main

class Editor(ctk.CTk):
    #editor window class
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.geometry("600x400")
        self.title("UVSIM code editor")
        self.configure(fg_color= "lightblue")

        # add widgets to app

        #number buttons
        for i in range(10):
            button = ctk.CTkButton(self, height=50, width=85, text=i, font=("Arial", 18),
                                    command=lambda v=i: self.num_button_click(v))
            col = 0
            if i%3 == 1 or i == 9:
                col = 1
            elif i%3 == 2:
                col = 2
            button.grid(row=(i//3)+1, column=col, padx=6, pady=10)

        #edit page function buttons
        edit_buttons = {"Run":(5, 2), "Clear":(5, 1), "Delete":(5, 0), "Help":(4, 0), "Newline":(4, 2)} # dict key = name value = (r, c)

        for button_name in edit_buttons.keys():
            button = ctk.CTkButton(self, height=50, width=85, text=button_name, font=("Arial", 18), 
                                   command=lambda v=button_name: self.edit_button_click(v))
            button.grid(row=edit_buttons[button_name][0], column=edit_buttons[button_name][1], padx=6, pady=10)

        #text box for commands to go in
        label = ctk.CTkLabel(self, text="keypad", fg_color="transparent", font=("Arial", 18), pady=15)
        label.grid(row=0, column=1)

    # add methods to app
    def num_button_click(self, num):
        self.inputs.append(num)
        print(num)
        # textbox.insert("end", str(num))

    def edit_button_click(self, value):
        if value == "Run":
            self.button_run()
        elif value == "Clear":
            print(value)
            #button_clr()
        elif value == "Delete":
            print(value)
            #button_del()
        elif value == "Help":
            print(value)
            #button_help()
        elif value == "Newline":
            print(value)
            #button_newline()
    
    def button_run(self):   
        self.iconify()     
        display = Runner(self)
        display.mainloop()
        commands = []
        for i in range(0, len(self.inputs), 4):
            input = self.inputs[i:i+4]
            command = ""
            for num in input:
                command += str(num)
            commands.append(command)
        main.load_commands(commands)

    def button_clr(self):
        self.inputs = []


class Runner(ctk.CTk):
    #run code window class 
    def __init__(self, editor):
        super().__init__()
        self.geometry("600x350")
        self.title("UVSIM")
        self.configure(fg_color= "lightblue")

        # add widgets to app

        #memory
        #accumulator and program counter
        #buttons
        button = ctk.CTkButton(self, height=50, width=85, text="edit", font=("Arial", 18), 
                                   command=lambda: self.show_editor(editor))
        button.pack()
        

    def show_editor(self, editor):
        # This method is called when the Runner window is closed
        editor.deiconify()
        self.withdraw()


app = Editor()
app.mainloop()