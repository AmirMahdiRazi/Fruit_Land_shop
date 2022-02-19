
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


class SOther(Screen,Image):
    cost = 0
    IT_Order=IT('سفارش را وارد کنید')
    
    IT_Cost=IT('مبلغ سفارش را وارد کنید')

    def __init__(self,**kwargs):
        super(SOther,self).__init__(**kwargs)
        self.GL = GridLayout(cols=1)
        self.cols=1
        self.source ='images/BGI/CD.jpg'
        self.GL.padding=[50,15,50,15]
        self.GL.add_widget(Label(size_hint=(1,.15)))
        self.GL.add_widget(__class__.IT_Order)
        self.GL.add_widget(Label(size_hint=(1,.15)))
        self.GL.add_widget(__class__.IT_Cost)
        self.GL.add_widget(Label(size_hint=(1,.15)))
        self.GL.add_widget(B2())
        self.GL.add_widget(Label(size_hint=(1,.15)))

        _GLB=GridLayout(cols=3,size_hint=(1,.25))
        _GLB.add_widget(Label())
        _GLB.add_widget(Button(text=Txt("منو"),font_name="font/arial",font_size="35",\
            size_hint =(.5, .005),background_color='00FFD8',on_release=self.ChangePage))
        _GLB.add_widget(Label())

        self.GL.add_widget(_GLB)
    
        self.add_widget(self.GL)


    def ChangePage(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SMenu'
        


#2 Button
class B2(GridLayout):
        
    def __init__(self):
        super(B2, self).__init__()
        self.cols=1
        
        self.add_widget(Button(text=Txt("تایید"),font_name="font/KamranB",font_size="70",background_color="0FFC04b0",on_press=self.register))
        self.add_widget(Label(size_hint=(1,.2)))
        self.add_widget(Button(text=Txt("لغو"),font_name="font/KamranB",background_color="FC0404b0",font_size="70",on_press=self.reset))
        
        


    #Write on File and Reset IT and Variable
    def register(self,instance):
        if (len(SOther.IT_Order.text) != 0) and (len(SOther.IT_Cost.text) != 0) :
            write_file(SOther.IT_Order.text,str(SOther.IT_Cost.text))
            SOther.IT_Order.text = ''
            SOther.IT_Order.str = ''
            SOther.IT_Cost.text = ''
            SOther.IT_Cost.str = ''
    def reset(self,instance):
        SOther.IT_Order.text = ''
        SOther.IT_Order.str = ''
        SOther.IT_Cost.text = ''
        SOther.IT_Cost.str = ''
        

    

# class Myapp(App):
#     def build(self):
#         Window.maximize()
#         return SOther()
        

# Myapp().run()

