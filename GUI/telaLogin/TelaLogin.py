from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from GUI.popup.MyPopup import MyPopup

Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '500')

class Tela(GridLayout):
    pass

class TelaLogin(App):
    def build(self):
        return Tela()
    def login(self,login,senha):
        MyPopup(login+senha)
TelaLogin().run()