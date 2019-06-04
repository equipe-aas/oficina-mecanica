from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class Menu(BoxLayout):
    pass

class MenuPrincipal(App):
    def build(self):
        return Menu()
    def sair(self):
        self.stop()