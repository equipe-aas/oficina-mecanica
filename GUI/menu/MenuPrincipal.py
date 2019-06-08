from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from GUI.popup.MyPopup import MyPopup
from fachada.Fachada import Fachada


class MenuInicial(ScreenManager):
    pass

class MenuPrincipal(App):
    def build(self):
        self.menuInicial = MenuInicial()
        return self.menuInicial
    def sair(self):
        self.stop()
    def login(self):
        from GUI.telaLogin.TelaLogin import TelaLogin
        TelaLogin()
    def cadastrarCliente(self,cpf,nome,endereco,telefone):
        try:
            Fachada().adicionarCliente(cpf,nome,endereco,telefone)
            MyPopup('Cliente Cadastrado!!!')
            self.menuInicial.current = 'menuCliente'
        except BaseException as e:
            MyPopup(e.__str__())
