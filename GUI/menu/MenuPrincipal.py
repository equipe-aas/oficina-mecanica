from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from GUI.popup.MyPopup import MyPopup
from fachada.Fachada import Fachada
from negocio.entidades.Cliente import Cliente
from kivy.config import Config

from negocio.entidades.PecaQuantidade import PecaQuantidade

Config.set('graphics', 'width', '650')
Config.set('graphics', 'height', '500')

class Menu(ScreenManager):
    pass

class MenuPrincipal(App):
    def __init__(self,**kwargs):
        super(MenuPrincipal,self).__init__(**kwargs)
        self.cliente = Cliente('22211133311', 'TESTE TESTE', 'RUA TESTE', '88888888')
        self.fachada = Fachada()
        self.tamanhoFonte = 20
        self.height = 150

    def build(self):
        self.menuInicial = Menu()
        return self.menuInicial

    def getCliente(self):
        return self.cliente

    def login(self,login,senha,EntLogin,EntSenha):
        try:
            EntLogin.text = ''
            EntSenha.text = ''

            Fachada().login(login,senha)
            self.menuInicial.current = 'menu'
        except BaseException as e:
            MyPopup(e.__str__())

    def buscarCliente(self,BuscarCpf,EntradaCpf,EntradaNome,EntradaEndereco,EntradaTelefone):
        try:

            self.cliente = self.fachada.buscarCliente(BuscarCpf.text)
            BuscarCpf.text = ''

            EntradaCpf.text = self.cliente.cpf
            EntradaNome.text = self.cliente.nome
            EntradaEndereco.text = self.cliente.endereco
            EntradaTelefone.text = self.cliente.telefone

            self.menuInicial.current = 'editarCliente'

        except BaseException as e:
            MyPopup(e.__str__())

    def cadastrarCliente(self,EntradaCpf,EntradaNome,EntradaEndereco,EntradaTelefone):
        try:
            self.fachada.adicionarCliente(EntradaCpf.text,EntradaNome.text,EntradaEndereco.text,EntradaTelefone.text)
            MyPopup('Cliente Cadastrado!!!')

            EntradaCpf.text = ''
            EntradaNome.text = ''
            EntradaEndereco.text = ''
            EntradaTelefone.text = ''

            self.menuInicial.current = 'menuCliente'
        except BaseException as e:
            MyPopup(e.__str__())

    def editarCliente(self,cpf,nome,endereco,telefone):
        try:
            self.fachada.atualizarCliente(cpf,nome,endereco,telefone)
            MyPopup('Modificações Salvas!!!')
            self.menuInicial.current = 'menuCliente'

        except BaseException as e:
            MyPopup(e.__str__())

    def deletarCliente(self,DeletarCpf):
        try:
            self.fachada.removerCliente(DeletarCpf.text)
            DeletarCpf.text = ''

            MyPopup('Cliente Removido!!!')

        except BaseException as e:
            MyPopup(e.__str__())

    def listarClientes(self,boxClientes):
        try:
            boxClientes.clear_widgets()
            for cliente in self.fachada.clientes.all_clientes():
                label = Label(text=cliente.__str__(),size_hint_y=None,height=self.height,font_size=self.tamanhoFonte)
                boxClientes.add_widget(label)

            self.menuInicial.current = 'listarClientes'
        except BaseException as e:
            MyPopup(e.__str__())

    def listarFornecedores(self, boxFornecedor):
        try:
            boxFornecedor.clear_widgets()
            for fornecedor in self.fachada.fornecedores.all_fornecedores():
                label = Label(text=fornecedor.__str__(), size_hint_y=None, height=self.height, font_size=self.tamanhoFonte)
                boxFornecedor.add_widget(label)

            self.menuInicial.current = 'listarFornecedores'
        except BaseException as e:
            MyPopup(e.__str__())

    def cadastrarFornecedor(self,EntradaCnpj,EntradaNome,EntradaTelefone,EntradaEmail,EntradaEndereco):
        try:
            self.fachada.adicionarFornecedor(EntradaCnpj.text, EntradaNome.text, EntradaTelefone.text,\
                                             EntradaEmail.text, EntradaEndereco.text)

            MyPopup('Fornecedor Cadastrado!!!')

            EntradaCnpj.text = ''
            EntradaNome.text = ''
            EntradaTelefone.text = ''
            EntradaEmail.text = ''
            EntradaEndereco.text = ''

            self.menuInicial.current = 'menuFornecedor'
        except BaseException as e:
            MyPopup(e.__str__())

    def editarFornecedor(self,EditCnpj,EditNomeForn,EditTelefoneForn,EditEmailForn,EditEnderecoForn):
        try:
            self.fachada.atualizarFornecedor(EditCnpj.text, EditNomeForn.text, EditTelefoneForn.text,\
                                             EditEmailForn.text, EditEnderecoForn.text)
            MyPopup('Modificações Salvas!!!')
            self.menuInicial.current = 'menuCliente'

        except BaseException as e:
            MyPopup(e.__str__())

    def buscarFornecedor(self,BuscarCnpj,EditCnpj,EditNomeForn,EditTelefoneForn,EditEmailForn,EditEnderecoForn):
        try:

            self.fornecedor = self.fachada.buscarFornecedor(BuscarCnpj.text)
            BuscarCnpj.text = ''

            EditCnpj.text = self.fornecedor.cnpj
            EditNomeForn.text = self.fornecedor.nome
            EditTelefoneForn.text = self.fornecedor.telefone
            EditEmailForn.text = self.fornecedor.email
            EditEnderecoForn.text = self.fornecedor.endereco

            self.menuInicial.current = 'editarFornecedor'

        except BaseException as e:
            MyPopup(e.__str__())

    def deletarFornecedor(self,DeletarCnpj):
        try:
            self.fachada.removerFornecedor(DeletarCnpj.text)
            DeletarCnpj.text = ''

            MyPopup('Fornecedor Removido!!!')

        except BaseException as e:
            MyPopup(e.__str__())

    def adicionarPeca(self, EntradaIdPeca, EntradaQuantidade, boxVenda):
        try:
            peca = self.fachada.buscarPeca(int(EntradaIdPeca.text))
            if(peca.quantidade < 1):
                MyPopup('Estoque Baixo!!!\n'+peca.__str__())

            pecaQuantidade = PecaQuantidade(peca,int(EntradaQuantidade.text))
            label = Label(text=pecaQuantidade.__str__(), size_hint_y=None, height=self.height, font_size=self.tamanhoFonte)
            boxVenda.add_widget(label)

        except BaseException as e:
            MyPopup(e.__str__())

    def cadastrarPeca(self, EntDescricaoPeca,EntFornecedor,EntPrecoCusto,EntPrecoVenda,EntQuantidadePeca):
        try:
            fornecedor = self.fachada.buscarFornecedor(EntFornecedor.text)
            self.fachada.adicionarPeca(EntDescricaoPeca.text, fornecedor, float(EntPrecoCusto.text),\
                                          float(EntPrecoVenda.text), int(EntQuantidadePeca.text))

            MyPopup('Peca Cadastrada!!!')

            EntDescricaoPeca.text = ''
            EntFornecedor.text = ''
            EntPrecoCusto.text = ''
            EntPrecoVenda.text = ''
            EntQuantidadePeca.text = ''

            self.menuInicial.current = 'menuPeca'
        except BaseException as e:
            MyPopup(e.__str__())

    def editarPeca(self, EditIdPeca, EditDescricaoPeca, EditFornecedor, EditPrecoCusto, EditPrecoVenda, EditQuantidadePeca):
        try:
            self.fachada.atualizarPeca(int(EditIdPeca.text), EditDescricaoPeca.text, EditFornecedor.text,\
                                       float(EditPrecoCusto.text), float(EditPrecoVenda.text),int(EditQuantidadePeca.text))

            MyPopup('Modificações Salvas!!!')
            self.menuInicial.current = 'menuPeca'

        except BaseException as e:
            MyPopup(e.__str__())

    def buscarPeca(self, BuscarIdPeca,EditIdPeca,EditDescricaoPeca,EditFornecedor,EditPrecoCusto,EditPrecoVenda,EditQuantidadePeca):
        try:

            self.peca = self.fachada.buscarPeca(int(BuscarIdPeca.text))
            BuscarIdPeca.text = ''

            EditIdPeca.text = self.peca.codigo
            EditDescricaoPeca.text = self.peca.descricao
            EditFornecedor.text = self.peca.fornecedor
            EditPrecoCusto.text = self.peca.preco_custo
            EditPrecoVenda.text = self.peca.preco_venda
            EditQuantidadePeca.text = self.peca.quantidade

            self.menuInicial.current = 'editarPeca'

        except BaseException as e:
            MyPopup(e.__str__())

    def listarPecas(self, boxPecas):
        try:
            boxPecas.clear_widgets()
            for peca in self.fachada.pecas.all_pecas():
                label = Label(text=peca.__str__(),size_hint_y=None,height=self.height,font_size=self.tamanhoFonte)
                boxPecas.add_widget(label)

            self.menuInicial.current = 'listarPecas'
        except BaseException as e:
            MyPopup(e.__str__())

    def deletarPeca(self, DeletarPeca):
        try:
            self.fachada.removerPeca(int(DeletarPeca.text))
            DeletarPeca.text = ''

            MyPopup('Peca Removida!!!')

        except BaseException as e:
            MyPopup(e.__str__())

MenuPrincipal().run()