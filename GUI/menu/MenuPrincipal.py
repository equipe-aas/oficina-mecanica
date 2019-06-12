from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from GUI.popup.MyPopup import MyPopup
from fachada.Fachada import Fachada
from negocio.entidades.Cliente import Cliente
from kivy.config import Config

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
            Fachada().adicionarCliente(EntradaCpf.text,EntradaNome.text,EntradaEndereco.text,EntradaTelefone.text)
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

MenuPrincipal().run()