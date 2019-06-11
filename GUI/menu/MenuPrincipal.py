from kivy.app import App
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

    def buscarCliente(self,cpf,Ecpf,Enome,Eendereco,Etelefone,Bcpf):
        try:
            Bcpf.text = ''
            self.cliente = self.fachada.buscarCliente(cpf)

            Ecpf.text = self.cliente.cpf
            Enome.text = self.cliente.nome
            Eendereco.text = self.cliente.endereco
            Etelefone.text = self.cliente.telefone

            self.menuInicial.current = 'editarCliente'

        except BaseException as e:
            MyPopup(e.__str__())

    def cadastrarCliente(self,cpf,nome,endereco,telefone,Ecpf,Enome,Eendereco,Etelefone):
        try:
            Fachada().adicionarCliente(cpf,nome,endereco,telefone)
            MyPopup('Cliente Cadastrado!!!')

            Ecpf.text = ''
            Enome.text = ''
            Eendereco.text = ''
            Etelefone.text = ''

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

    def deletarCliente(self,cpf,Ecpf):
        try:
            self.fachada.removerCliente(cpf)
            Ecpf.text = ''

            MyPopup('Cliente Removido!!!')

        except BaseException as e:
            MyPopup(e.__str__())

    def listarClientes(self,clientes):
        try:
            clientes.text = self.fachada.str_cliente()
            self.menuInicial.current = 'listarClientes'
        except BaseException as e:
            MyPopup(e.__str__())

MenuPrincipal().run()