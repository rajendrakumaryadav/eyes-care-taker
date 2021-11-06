import tkinter as tk


class caretaker_ui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(self.get_window_size())

    def get_window_size(self):
        return self.geometry()


if __name__ == "__main__":
    app = caretaker_ui()
    app.mainloop()
