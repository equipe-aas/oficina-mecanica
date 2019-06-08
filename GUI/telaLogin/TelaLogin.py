from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from GUI.menu.MenuPrincipal import MenuPrincipal

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

class Tela(GridLayout):
    pass

class TelaLogin(App):
    def build(self):
        return Tela()
    def login(self,login,senha):
        if login == '' and senha == '':
            self.stop()
            MenuPrincipal().run()

TelaLogin().run()