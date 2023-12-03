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
        print(num)
        self.textbox.insert("end", str(num))

    def edit_button_click(self, value):
        if value == "Run":
            self.button_run()
        elif value == "Clear":
            self.inputs = []
            self.textbox.delete("1.0", "end")
        elif value == "Delete":
            if len(self.inputs) > 0:
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
        commands = []
        if len(self.inputs) < 4:
            print("input commands")
            return
        for i in range(0, len(self.inputs), 4):
            input = self.inputs[i:i+4]
            command = ""
            for num in input:
                command += str(num)
            commands.append(command)
        self.memory = main.load_commands(commands)
        
        #open new window
        if self.memory:
            self.iconify()     
            display = Runner(self)
            display.mainloop()

    def button_nl(self):
        current_line, _ = map(int, self.textbox.index(ctk.INSERT).split('.'))
        start = f"{current_line}.0"
        end = f"{current_line}.end"
        line_text = self.textbox.get(start, end)

        if len(line_text) == 4:
            self.textbox.insert("end", "\n")
        elif len(line_text) > 4:
            truncated_text = line_text[:4]
            self.textbox.delete(start, end)
            self.textbox.insert(start, truncated_text)
            self.textbox.insert("end", "\n")

class Runner(ctk.CTkToplevel):
    #run code window class 
    def __init__(self, editor):
        super().__init__()
        self.geometry("600x410")
        self.title("UVSIM")
        self.configure(fg_color= "lightblue")

        # add widgets to app

        #memory
        scrollable_frame = ctk.CTkScrollableFrame(self, width=250, height=200)
        scrollable_frame.grid(row=1, column=1, sticky="nsew")
        #accumulator and program counter
        #buttons
        button = ctk.CTkButton(self, height=50, width=85, text="edit", font=("Bahnschrift", 18), 
                                   command=lambda: self.show_editor(editor))
        button.grid(row=0, column=0)
        
    def show_editor(self, editor):
        # This method is called when the Runner window is closed
        self.withdraw()
        editor.deiconify()
        self.quit()

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
        # This method is called when the Runner window is closed
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
        # This method is called when the Runner window is closed
        self.withdraw()
        editor.deiconify()
        self.quit()


app = Editor()
app.mainloop()