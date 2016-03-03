# encoding: UTF-8

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.W+tk.E)
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.btn = tk.Button(self)
        self.btn['text'] = 'Button'
        self.btn['command'] = self.btn_cmd
        self.btn.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E)

        self.columnconfigure(1, weight=1)
        self.QUIT = tk.Button(self, text='QUIT', fg='red', command=root.destroy)
        self.QUIT.grid(row=1, column=1, sticky=tk.N+tk.S+tk.W+tk.E)

    def btn_cmd(self):
        print('Btn clicked! Command is running.')

root = tk.Tk()
app = Application(master=root)
app.btn.invoke()
app.mainloop()