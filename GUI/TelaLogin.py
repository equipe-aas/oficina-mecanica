from tkinter import *
from GUI.menu.MenuPrincipal import Menu

class TelaLogin(Frame):
    def __init__(self):
        self.master=Tk()
        self.master.title = 'Tela de Login'
        self.master.geometry("300x350+500+200")
        self.master["bg"] = "white"

        self.criarLabel()
        self.criarEntradas()
        self.criarImagem()

        self.botaoEntrar = Button(self.master, text='Entrar', width=15,bd=10, command=self.login)
        self.botaoEntrar.grid(row=3, column=1)

        self.master.mainloop()

    def criarEntradas(self):
        self.senha = Entry(self.master, width=30, show="*")
        self.senha.grid(row=2, column=1)

        self.nome = Entry(self.master, width=30)
        self.nome.grid(row=1, column=1)

    def criarLabel(self):
        self.nomeLabel = Label(self.master, text="Nome",bg='white')
        self.nomeLabel.grid(row=1, column=0)

        self.senhaLabel = Label(self.master, text="Senha",bg='white')
        self.senhaLabel.grid(row=2, column=0)

    def criarImagem(self):
        self.arquivo = PhotoImage(file='img/o.png')
        self.arquivo = self.arquivo.subsample(2,2)

        self.imagem = Label(self.master,image=self.arquivo)
        self.imagem.place()
        self.imagem.grid(row=0,column=1)

    def login(self):
        try:
            if self.nome.get() == '' and self.senha.get() == '':
                self.master.destroy()
                Menu()
        except BaseException as e:
            Menu()

TelaLogin()
