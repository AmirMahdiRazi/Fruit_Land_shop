#Page Warm Drink
from numpy import spacing
from All_Module import *
from wr import *
from functools import partial


import kivy.app
import kivy.uix.label
import kivy.uix.button
import kivy.uix.textinput
import kivy.uix.boxlayout
import arabic_reshaper
import bidi.algorithm
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty
from share import Txt



class IT(TextInput):
    str = StringProperty()

    def __init__(self,txt, **kwargs):
        super(IT, self).__init__(**kwargs)
        self.hint_text=Txt(txt)
        self.font_name="font/arial"
        self.font_size="50"
        self.background_color="03192677"
        self.foreground_color=(1,1,1,1)
        self.halign="center"
        self.padding_y = 75
    def insert_text(self, substring, from_undo=False):
        self.str = self.str+substring
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(IT, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape(self.str))


class MyPME(GridLayout,Image):
    cost = 0
    IT_Order=IT('سفارش را وارد کنید')
    
    IT_Cost=IT('مبلغ سفارش را وارد کنید')

    def __init__(self):
        super(MyPME,self).__init__()
        
        self.cols=1
        self.source ='images/BGI/CD.jpg'
        self.padding=50
        self.add_widget(Label(size_hint=(1,.5)))
        self.add_widget(__class__.IT_Order)
        self.add_widget(Label(size_hint=(1,.5)))
        self.add_widget(__class__.IT_Cost)
        self.add_widget(Label(size_hint=(1,.5)))
        self.add_widget(B2())


#2 Button
class B2(GridLayout):
        
    def __init__(self):
        super(B2, self).__init__()
        self.cols=1
        # self.spacing=[25,0]
        self.padding=[500,0,500,10]
        self.add_widget(Button(text=Txt("تایید"),font_name="font/KamranB",font_size="70",background_color="0FFC04b0",on_press=self.register))
        self.add_widget(Label(size_hint=(1,.4)))
        self.add_widget(Button(text=Txt("لغو"),font_name="font/KamranB",background_color="FC0404b0",font_size="70",on_press=self.reset))
        

    #Write on File and Reset IT and Variable
    def register(self,instance):
        if (len(MyPME.IT_Order.text) != 0) and (len(MyPME.IT_Cost.text) != 0) :
            write_file(MyPME.IT_Order.text,str(MyPME.IT_Cost.text))
            MyPME.IT_Order.text = ''
            MyPME.IT_Order.str = ''
            MyPME.IT_Cost.text = ''
            MyPME.IT_Cost.str = ''
    def reset(self,instance):
        MyPME.IT_Order.text = ''
        MyPME.IT_Order.str = ''
        MyPME.IT_Cost.text = ''
        MyPME.IT_Cost.str = ''
        



# class Myapp(App):
#     def build(self):
#         Window.maximize()
#         return MyPME()
        

# Myapp().run()


