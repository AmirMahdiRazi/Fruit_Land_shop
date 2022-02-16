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
class Main(App):  # display the welcome screen
    def build(self):
        Window.maximize()
        sm = ScreenManager()
        
       
        
        sm.add_widget( SOrder ( name = 'Login') )
        sm.add_widget( SOther ( name = 'Recovery Password' ) )
        # sm.add_widget( Player ( name = 'Player') )
        # sm.add_widget( Country( name = 'Country' ) )
        # sm.add_widget( Team ( name = 'Team' ) )
        # sm.add_widget( Competition ( name = 'Competition') )
        # sm.add_widget( CA_Lay ( name = 'Create Account') )
        
        
        return sm


if __name__ == '__main__':
    Main().run()