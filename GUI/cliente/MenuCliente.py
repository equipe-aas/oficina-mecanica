from tkinter import *
from GUI.cliente.TelaCadastro import TelaCadastro
from fachada.Fachada import Fachada


class MenuCliente:
    def __init__(self):
        self.master = Tk()
        self.master.title = 'Menu Cliente'
        self.master.geometry("500x250+400+100")
        self.master["bg"] = "white"
        self.texto = Label(self.master)
        self.texto.grid(row=3,column=0)
        self.criarBotoes()
        self.master.mainloop()

    def criarBotoes(self):
        self.botaoCadastrar = Button(self.master,text='Novo Cliente',bg='gray',width=25,bd=10,takefocus=True,command=self.cadastrar)
        self.botaoRemover = Button(self.master, text='Remover Cliente', bg='gray', width=25,bd=10, takefocus=True)
        self.botaoEditar = Button(self.master, text='Editar Cliente', bg='gray', width=25,bd=10, takefocus=True)
        self.botaoBuscar = Button(self.master, text='Buscar Cliente', bg='gray', width=25,bd=10, takefocus=True)
        self.botaoListar = Button(self.master, text='Listar Clientes', bg='gray', width=25,bd=10, takefocus=True,command=self.listar)

        self.botaoCadastrar.grid(row=0,column=0)
        self.botaoRemover.grid(row=0,column=1)
        self.botaoEditar.grid(row=1,column=0)
        self.botaoBuscar.grid(row=1,column=1)
        self.botaoListar.grid(row=2,column=0)

    def cadastrar(self):
        TelaCadastro()
    def listar(self):
        self.texto['text'] = Fachada().str_cliente()