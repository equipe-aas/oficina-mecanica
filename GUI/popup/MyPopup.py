from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class MyPopup(Popup):
    def __init__(self,msg,**kwargs):
        super().__init__(**kwargs)
        label = Label(text=msg,font_size=20,size_hint_y=None)
        botao = Button(text='OK',size_hint_y=None)

        box = BoxLayout(orientation='vertical',padding=15)
        box.add_widget(label)
        box.add_widget(botao)

        popup = Popup(title='AVISO!!!', content=box,auto_dismiss=False,size=(300,300))
        botao.bind(on_press=popup.dismiss)
        popup.open()