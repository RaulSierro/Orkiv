__author__ = 'Raul'
from  kivy.app import App
from  kivy.uix.boxlayout import BoxLayout
from  kivy.properties import ObjectProperty
from  kivy.uix.anchorlayout import AnchorLayout

class Orkiv(App):
    pass

class FormaCuentaDetalles(AnchorLayout):

    server_box = ObjectProperty()
    username_box = ObjectProperty()
    password_box = ObjectProperty()
    def login(self):
        print(self.server_box.text)
        print(self.username_box.text)
        print(self.password_box.text)


Orkiv().run()