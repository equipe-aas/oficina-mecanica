from tkinter import Tk, Label, Button


class Popup:
    def __init__(self,msg):
        self.master = Tk()
        self.master.title = 'AVISO'
        self.master.geometry("300x150")
        self.master["bg"] = "white"

        self.label = Label(self.master,text=msg)
        self.label.grid(row=0,column=0)
        self.botao = Button(self.master,text="OK",command=self.sair,width=20,bd=10)
        self.botao.grid(row=1,column=0)

        self.master.mainloop()

    def sair(self):
        self.master.destroy()