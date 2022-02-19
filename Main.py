#Main Project

from All_Module import *
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from SOrd import SOrder
from SOth import SOther
from SGV import MySGV
from SMen import SMenu
class Main(App):  # display the welcome screen
    def build(self):
        Window.maximize()
        sm = ScreenManager()
        
        sm.add_widget( SMenu ( name = 'SMenu') )
        
        sm.add_widget( SOrder ( name = 'SOrder') )
        sm.add_widget( SOther ( name = 'SOther' ) )
        sm.add_widget( MySGV ( name = 'SGV') )

        
        
        
        
        return sm


if __name__ == '__main__':
    Main().run()