import customtkinter as ctk
import main

class Editor(ctk.CTk):
    #editor window class
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.geometry("600x410")
        self.title("UVSIM code editor")
        self.configure(fg_color= "lightblue")

        # add widgets to app
        #label for page
        label = ctk.CTkLabel(self, text="UVSIM Code Editor", fg_color="transparent", text_color="#3B8ED0", font=("Bahnschrift", 24), pady=15)
        label.grid(row=0, column=0, columnspan=2, sticky="nsew")

        #number buttons       
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=1, column=0, padx=10, pady=0)

        for i in range(10):
            button = ctk.CTkButton(button_frame, height=50, width=85, text=i, font=("Bahnschrift", 18),
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
            button = ctk.CTkButton(button_frame, height=50, width=85, text=button_name, text_color="#DBDBDB", font=("Bahnschrift", 18), 
                                   command=lambda v=button_name: self.edit_button_click(v))
            button.grid(row=edit_buttons[button_name][0], column=edit_buttons[button_name][1], padx=6, pady=10)

        self.textbox = ctk.CTkTextbox(self, width=275, height=200, fg_color="#DBDBDB", text_color="#3B8ED0", font=("Bahnschrift", 18), border_color="#3B8ED0", border_width=2)
        self.textbox.grid(row=1, column=1, sticky="nsew")

        file_button = ctk.CTkButton(self, width=20, corner_radius=0, text="⬆ ⬇", font=("Bahnschrift", 20),  fg_color="#DBDBDB", text_color="#7A7A7A", command=self.file_warning)
        file_button.grid(row=1, column=1, sticky="se", padx=10, pady=5)

    # add methods to app

    def file_warning(self):
        #update to impliment file upload and download
        self.iconify()  
        warn = File(self)
        warn.mainloop()

    def num_button_click(self, num):
        self.inputs.append(num)
        self.textbox.insert("end", str(num))

    def edit_button_click(self, value):
        if value == "Run":
            self.button_run()
        elif value == "Clear":
            self.inputs = []
            self.textbox.delete("1.0", "end")
        elif value == "Delete":
            last_char = self.textbox.get("end-2c", "end-1c")
            if len(self.inputs) > 0 and not (last_char == "\n"):
                self.inputs.pop()
            self.textbox.delete("end-2c")
        elif value == "Help":
            self.iconify()  
            help = Helper("helpEdit.txt", self)
            help.mainloop()
        elif value == "Newline":
            self.button_nl()
    
    def button_run(self): 
        #store commands in main.memory  
        self.button_nl()
        commands = []
        if len(self.inputs) < 4:
            commands = ["9999"]
        else:
            for i in range(0, len(self.inputs), 4):
                input = self.inputs[i:i+4]
                command = ""
                for num in input:
                    command += str(num)
                if len(command) == 4:
                    commands.append(command)
        error = main.load_commands(commands)
        #open new window
        self.iconify()     
        display = Runner(self, error)
        display.mainloop()

    def button_nl(self):
        current_line, _ = map(int, self.textbox.index(ctk.INSERT).split('.'))
        start = f"{current_line}.0"
        end = f"{current_line}.end"
        line_text = self.textbox.get(start, end)

        if len(line_text) == 4:
            self.textbox.insert("end", "\n")
        elif len(line_text) > 4:
            overflow = len(line_text) - 4
            for _ in range(overflow):
                self.inputs.pop()
            truncated_text = line_text[:4]
            self.textbox.delete(start, end)
            self.textbox.insert(start, truncated_text)
            self.textbox.insert("end", "\n")

class Runner(ctk.CTkToplevel):
    #run code window class 
    def __init__(self, editor, error):
        super().__init__()
        self.geometry("610x420")
        self.title("UVSIM")
        self.configure(fg_color= "lightblue")
        self.editor = editor

        # add widgets to app
        
        #label for page
        label = ctk.CTkLabel(self, text="UVSIM Simulator", fg_color="transparent", text_color="#3B8ED0", font=("Bahnschrift", 24), pady=15)
        label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        #memory
        mem_frame = ctk.CTkScrollableFrame(self, width=250, height=340, border_color="#3B8ED0", border_width=2)
        mem_frame.grid(row=1, column=0, rowspan=3, sticky="nsew", padx=10)

        self.indeces = ctk.CTkTextbox(mem_frame, width=123, height=2250, fg_color="transparent", text_color="#3B8ED0", font=("Bahnschrift", 18), activate_scrollbars=False)
        self.indeces.grid(row=0, column=0)
        self.values = ctk.CTkTextbox(mem_frame, width=123, height=2250, fg_color="transparent", text_color="#3B8ED0", font=("Bahnschrift", 18), activate_scrollbars=False)
        self.values.grid(row=0, column=1)
        
        #accumulator and program counter
        self.accLabel = ctk.CTkLabel(self, text=f"Accumulator = {main.accumulator}", fg_color="transparent", text_color="#3B8ED0", font=("Bahnschrift", 18))
        self.accLabel.grid(row=2, column=1, sticky="w", pady=15, padx=20)
        self.PCLabel = ctk.CTkLabel(self, text=f"PC = {main.program_counter}", fg_color="transparent", text_color="#3B8ED0", font=("Bahnschrift", 18), pady=15)
        self.PCLabel.grid(row=2, column=2, sticky="w")

        #console
        self.console = ctk.CTkTextbox(self, width=280, height=150, fg_color="#DBDBDB", text_color="#3B8ED0", font=("Bahnschrift", 18), activate_scrollbars=False, border_color="#3B8ED0", border_width=2)
        self.console.grid(row=1, column=1, columnspan=2)
        if error: 
            self.console.insert("end", error)
        #text box on row 1 column 1 span 2 columns
                
        self.update_mem()

        #buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.grid(row=3, column=1, columnspan=2, padx=10, pady=0, sticky="s")

        run_buttons = {"Edit code": (0,0), "Run": (0, 1), "Step in": (0, 2), "Halt": (1, 0), "Reset": (1, 1), "Help": (1, 2)}
        for button_name in run_buttons.keys():
            button = ctk.CTkButton(button_frame, height=50, width=85, text=button_name, text_color="#DBDBDB", font=("Bahnschrift", 18), 
                                   command=lambda v=button_name: self.run_button_click(v))
            button.grid(row=run_buttons[button_name][0], column=run_buttons[button_name][1], padx=6, pady=10)
        
    def show_editor(self):
        # This method is called when the Runner window is closed
        self.withdraw()
        self.editor.deiconify()
        self.quit()

    def run_button_click(self, value):
        if value == "Edit code":
            self.withdraw()
            self.editor.deiconify()
            self.quit()
        if value == "Run":
            while main.program_running:
                self.step_in()
            self.update_mem()
        elif value == "Step in":
            self.step_in()
            self.update_mem()
        elif value == "Halt":
            main.program_running = False
        elif value == "Reset":
            main.memory = { i : None for i in range(100) }
            main.accumulator = None
            main.program_counter = 0
            main.program_running = True
            self.withdraw()
            self.editor.button_run()
        elif value == "Help":
            self.iconify()  
            help = Helper("helpEdit.txt", self)
            help.mainloop()

    
    def get_val(self, val_object):
        vString = "".join(val_object.operation)
        memLoc = str(val_object.memLoc)
        if len(memLoc) < 2:
            memLoc = "0" + memLoc
        vString += memLoc
        return vString
    
    def update_mem(self):
        self.accLabel.configure(text=f"Accumulator = {main.accumulator}")
        self.PCLabel.configure(text=f"PC = {main.program_counter}")

        self.indeces.delete("1.0", "end")
        self.values.delete("1.0", "end")

        self.indeces.insert("end", "Memory\n")
        self.values.insert("end", "Value\n")

        for index, val in main.memory.items():
            if isinstance(val, main.command):
                val = f"comm {self.get_val(val)}"
            self.indeces.insert("end", f"{index}\n")
            self.values.insert("end", f"{val}\n")

    def step_in(self):
        # check if we're on a command
        if not isinstance(main.memory[main.program_counter], main.command):
            main.program_running = False
            
        
        if main.program_running:
            self.curr_command = main.memory[main.program_counter]
            if (isinstance(self.curr_command, main.IOops)):
                self.errorHandle()
            else: 
                error = self.curr_command.run()
                if error:
                    self.console.insert("end", "invalid command\n")
            if (isinstance(self.curr_command, main.BRops)):
                main.program_counter -= 1
            main.program_counter += 1
    
    def errorHandle(self):
        try:
            self.runIO()
        except:
            self.console.insert("end", "enter a number\n") 
            self.errorHandle()       
    
    def runIO(self):
        if self.curr_command.operation[1] == "0":
            self.read()
        elif self.curr_command.operation[1] == "1":
            self.curr_command.run()
            self.console.insert("end", f"{str(main.accumulator)}\n")
        else: 
            self.console.insert("end", "invalid command\n")

    def read(self):
        mem = self.curr_command.memLoc
        dialog = ctk.CTkInputDialog(text=f"enter value to store in memory location {str(mem)}: ", title="Reading Value")
        user_input = dialog.get_input()
        main.accumulator = int(user_input)
        self.curr_command.run()
        self.update_mem()

class Helper(ctk.CTkToplevel):
    def __init__(self, helper_file, editor):
        super().__init__()
        self.geometry("800x500")
        self.title("UVSIM Help")
        self.configure(fg_color="lightblue")

        with open(helper_file, "r") as file:
            file_content = file.read()

        # Add a CTkTextbox to display the file content
        text_box = ctk.CTkTextbox(self, width=800, height=400, fg_color="#DBDBDB", wrap="word", text_color="#3B8ED0", font=("Bahnschrift", 18))
        text_box.insert("end", file_content)
        text_box.pack(padx=10, pady=10)

        # # Add a Close button
        close_button = ctk.CTkButton(self, width=100, height=50, text="Close", text_color="#DBDBDB", font=("Bahnschrift", 18), command=lambda: self.show_editor(editor))
        close_button.pack(pady=10)
    
    def show_editor(self, editor):
        # This method is called when the Help window is closed
        self.withdraw()
        editor.deiconify()
        self.quit()

class File(ctk.CTkToplevel):
    def __init__(self, editor):
        super().__init__()
        self.geometry("300x250")
        self.title("UVSIM Help")
        self.configure(fg_color="lightblue")

        message = ctk.CTkTextbox(self, width=280, height=150, fg_color="#DBDBDB", text_color="#3B8ED0", font=("Bahnschrift", 18), wrap="word")
        message.insert("end", "Coming soon!\nThis feature is not yet ready, but soon you will be able to upload and download files in the code editor!")
        message.pack(pady=15)

        # # Add a Close button
        close_button = ctk.CTkButton(self, width=100, height=50, text="Close", text_color="#DBDBDB", font=("Bahnschrift", 18), command=lambda: self.show_editor(editor))
        close_button.pack()
    
    def show_editor(self, editor):
        # This method is called when the File window is closed
        self.withdraw()
        editor.deiconify()
        self.quit()


app = Editor()
app.mainloop()