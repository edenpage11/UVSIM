# gui2.py

import customtkinter as ctk
import main

class Editor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.geometry("600x400")
        self.title("UVSIM code editor")
        self.configure(fg_color="lightblue")

        # Add widgets to app

        # Text box for commands
        self.command_text = ctk.CTkTextbox(self, height=5, width=40, font=("Arial", 14), wrap="word")

        self.command_text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Number buttons
        for i in range(10):
            button = ctk.CTkButton(self, height=2, width=5, text=i, font=("Arial", 14),
                                    command=lambda v=i: self.num_button_click(v))
            col = 0
            if i % 3 == 1 or i == 9:
                col = 1
            elif i % 3 == 2:
                col = 2
            button.grid(row=(i // 3) + 1, column=col, padx=6, pady=6)

        # Edit page function buttons
        edit_buttons = {"Run": (5, 2), "Clear": (5, 1), "Delete": (5, 0), "Help": (4, 0), "Newline": (4, 2)}

        for button_name in edit_buttons.keys():
            button = ctk.CTkButton(self, height=2, width=5, text=button_name, font=("Arial", 14),
                                   command=lambda v=button_name: self.edit_button_click(v))
            button.grid(row=edit_buttons[button_name][0], column=edit_buttons[button_name][1], padx=6, pady=6)

        # Output label
        self.output_label = ctk.CTkLabel(self, text="Output: ", font=("Arial", 14), pady=10)
        self.output_label.grid(row=6, column=0, columnspan=3)

    def num_button_click(self, num):
        self.command_text.insert("end", str(num))

    def edit_button_click(self, value):
        if value == "Run":
            self.button_run()
        elif value == "Clear":
            self.button_clr()
        elif value == "Delete":
            self.button_del()
        elif value == "Help":
            self.button_help()
        elif value == "Newline":
            self.button_newline()

    def button_run(self):
        commands = self.command_text.get("1.0", "end-1c").split("\n")
        commands = [cmd.strip() for cmd in commands if cmd.strip()]  # Remove empty lines

        # Reset program state and load commands into main.py
        main.reset_program_state()
        main.load_commands(commands)

        # Run the program in main.py
        main.run_all()

        # After the program finishes running, update the output label with the final values
        self.update_output_label()

    def button_clr(self):
        self.command_text.delete("1.0", "end")

    def button_del(self):
        self.command_text.delete("end-2c", "end-1c")

    def button_help(self):
        # Provide help information as needed
        pass

    def button_newline(self):
        self.command_text.insert("end", "\n")

    def update_output_label(self):
        # Retrieve the values from main.py and update the output label
        memory_values = main.get_memory()
        accumulator_value = main.get_accumulator()
        program_counter_value = main.get_program_counter()

        # Example: self.output_label.config(text=f"Output: Memory={memory_values}, Accumulator={accumulator_value}, Program Counter={program_counter_value}")
        # Update your output label accordingly

class Runner(ctk.CTk):
    def __init__(self, editor):
        super().__init__()
        self.geometry("600x350")
        self.title("UVSIM")
        self.configure(fg_color="lightblue")

        # add widgets to app

        # memory
        memory_label = ctk.CTkLabel(self, text="Memory: ", font=("Arial", 16), pady=10)
        memory_label.pack()

        # accumulator and program counter
        accumulator_label = ctk.CTkLabel(self, text="Accumulator: ", font=("Arial", 16), pady=10)
        accumulator_label.pack()

        program_counter_label = ctk.CTkLabel(self, text="Program Counter: ", font=("Arial", 16), pady=10)
        program_counter_label.pack()

        # buttons
        button = ctk.CTkButton(self, height=50, width=85, text="edit", font=("Arial", 18),
                               command=lambda: self.show_editor(editor))
        button.pack()

    def show_editor(self, editor):
        # This method is called when the Runner window is closed
        editor.deiconify()
        self.withdraw()

if __name__ == "__main__":
    app = Editor()
    app.mainloop()
