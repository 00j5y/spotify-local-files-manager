import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Spotify Local Files Manager")
        self.geometry("400x180")

app = App()
app.mainloop()