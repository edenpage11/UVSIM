import customtkinter as ctk

# app.geometry("600x500")
# app.title("UVSIM")
# app.configure(fg_color= "lightblue")
# ctk.set_default_color_theme("blue")

# button = ctk.CTkButton(app, height=20, width=10, text="7", font=("Arial", 18))
# button.place()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("UVSIM")
        self.configure(fg_color= "lightblue")

        # add widgets to app

        for i in range(0, 10):
            button = ctk.CTkButton(self, height=50, width=100, text=i, font=("Arial", 18),
                                    command=lambda v=i: self.num_button_click(v))
            col = 0
            if i%3 == 1 or i == 9:
                col = 1
            elif i%3 == 2:
                col = 2
            button.grid(row=i//3, column=col, padx=6, pady=10)

    # add methods to app
    def num_button_click(self, num):
        print(num)


app = App()
app.mainloop()