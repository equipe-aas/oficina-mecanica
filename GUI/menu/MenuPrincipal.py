from tkinter import *
from tkinter.messagebox import showinfo
from GUI.cliente.MenuCliente import MenuCliente

class Menu:
    def __init__(self):
        self.master = Tk()
        self.master.title = 'Menu Pricipal'
        self.master.geometry("800x500+400+100")
        self.master["bg"] = "white"

        self.frameImagem = Frame(self.master)
        self.frameImagem.pack()
        self.frameBotoes = Frame(self.master)
        self.frameBotoes.pack()

        self.criarImagem()
        self.criarBotoes()
        self.master.mainloop()

    def criarImagem(self):
        self.arquivo = PhotoImage(file='img/o.png')
        self.arquivo = self.arquivo.subsample(2,2)

        self.imagem = Label(self.frameImagem,image=self.arquivo)
        self.imagem.place()
        self.imagem.grid(row=0,column=1)

    def criarBotoes(self):
        self.botaoCliente = Button(self.frameBotoes,text='Clientes',bg='gray',width=25,bd=10,takefocus=True,command=self.clietes)
        self.botaoFornecedor = Button(self.frameBotoes, text='Fornecedores', bg='gray', width=25,bd=10, takefocus=True)
        self.botaoFuncionario = Button(self.frameBotoes, text='Funcionario', bg='gray', width=25,bd=10, takefocus=True)
        self.botaoPecas = Button(self.frameBotoes, text='Pecas', bg='gray', width=25,bd=10, takefocus=True)
        self.botaoPedido = Button(self.frameBotoes, text='Pedidos', bg='gray', width=25,bd=10, takefocus=True)
        self.botaoServicos = Button(self.frameBotoes, text='Servicos', bg='gray', width=25,bd=10, takefocus=True)
        self.botaoVenda = Button(self.frameBotoes, text='Vendas', bg='gray', width=25,bd=10, takefocus=True)
        self.sair = Button(self.frameBotoes, text='Vendas', bg='gray', width=25,bd=10, takefocus=True)

        self.botaoCliente.grid(row=1,column=0)
        self.botaoFornecedor.grid(row=1,column=1)
        self.botaoFuncionario.grid(row=1,column=2)
        self.botaoPecas.grid(row=2,column=0)
        self.botaoPedido.grid(row=2,column=1)
        self.botaoServicos.grid(row=2,column=2)
        self.botaoVenda.grid(row=3,column=0)

    def clietes(self):
        try:
            MenuCliente()
        except BaseException as e:
            showinfo("AVISO!!!",e.__str__())
