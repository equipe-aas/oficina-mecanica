from tkinter import *
from GUI.popup import Popup
from fachada.Fachada import Fachada


class TelaCadastro:
    def __init__(self):
        self.master = Tk()
        self.master.title = 'Menu Cliente'
        self.master.geometry("500x300+400+100")
        self.master["bg"] = "white"

        self.frame1 = Frame(self.master)
        self.frame1.pack()
        self.frame2 = Frame(self.master)
        self.frame2.pack()

        self.criarLabel()
        self.criarEntradas()
        self.criarBotoes()

        self.master.mainloop()

    def criarLabel(self):
        self.labelCpf = Label(self.frame1,text='CPF: ',bg='white')
        self.labelCpf.grid(row=0,column=0)

        self.labelNome = Label(self.frame1,text='NOME: ',bg='white')
        self.labelNome.grid(row=1,column=0)

        self.labelEndereco = Label(self.frame1,text='ENDERECO: ',bg='white')
        self.labelEndereco.grid(row=2, column=0)

        self.labelTelefone = Label(self.frame1,text='TELEFONE: ',bg='white')
        self.labelTelefone.grid(row=3, column=0)
    def criarEntradas(self):
        self.cpf = Entry(self.frame1, width=70)
        self.cpf.grid(row=0, column=1)

        self.nome = Entry(self.frame1, width=70)
        self.nome.grid(row=1, column=1)

        self.endereco = Entry(self.frame1, width=70)
        self.endereco.grid(row=2, column=1)

        self.telefone = Entry(self.frame1, width=70)
        self.telefone.grid(row=3, column=1)

    def criarBotoes(self):
        self.botaoCadastrar = Button(self.frame2,text='Cadastrar',bg='gray',width=25,bd=10,takefocus=True,command=self.cadastrar)
        self.botaoCadastrar.pack()

    def cadastrar(self):
        try:
            cpf = self.cpf.get()
            nome = self.nome.get()
            endereco = self.endereco.get()
            telefone = self.telefone.get()
            Fachada().adicionarCliente(cpf, nome, endereco, telefone)
            self.master.destroy()
            Popup("CADASTRO CONCLUIDO!!!")
        except BaseException as e:
            Popup(e.__str__())