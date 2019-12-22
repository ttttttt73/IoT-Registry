print("hello")

import tkinter as tk

class windows_tkinter:
    def __init__(self, winodw):
        self.window = window
        self.window.title("GATEWAY")
        #self.window.geometry("640x400+100+100")
        self.window.resizable(True, True)

        self.arg1 = 1
        self.arg2 = "alpha"
        self.arg3 = "beta"
        self.__main__()

    def command_args(self, argument1, argument2, argument3):
        print(argument1, argument2, argument3)
        self.arg1 = argument1 * 2

    def __main__(self):
        button = tk.Button(self.window, width=25, height=10, text="btn1", command=lambda: self.command_args(self.arg1, self.arg2, self.arg3))
        button.pack(expand=True, anchor="center")
    
        
if __name__=='__main__':
    window = tk.Tk()
    windows_tkinter(window)
    window.mainloop()
