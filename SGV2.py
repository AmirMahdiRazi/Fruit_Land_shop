from All_Module import App,GridLayout,Button,Label,TextInput,Image,ScrollView,Window,ScreenManager, Screen
import wr 
from Text import *
from kivy.uix.image import AsyncImage
_txt =wr.read_file("today")

result = []
for _ in range(0,len(_txt)):
    res=_txt[_].split(',')
    result.append([res[0],res[1],res[2],res[3]])

#Gozaresh Vaziat
class SGV(GridLayout,Screen):
    def __init__(self,**kwargs):
        super(SGV, self).__init__(**kwargs)
        self.cols=1
        self.padding=[50,50,50,50]
        self.add_widget(TextInput(text="Hello",size=(10,10)))
        self.add_widget(SV())
        



# ScrollView With L4(4 Label)
class SV(ScrollView):
    def __init__(self,**kwargs):
        super(SV, self).__init__(**kwargs)
        self.size_hint=(1, None)
        self.size=(Window.width, Window.height)
        self.do_scroll_x = False
        self.do_scroll_y = True
        self.GL=GridLayout(cols=1,size_hint_y=None)
        self.GL.bind(minimum_height=self.GL.setter('height'))
        for i in range(len(result)):
            # btn = L4(str(i+1),result[i][0],result[i][1],result[i][2],result[i][3])
            # self.GL.add_widget(btn)
            pass
        btn = Button(text='1')
        self.GL.add_widget(btn)
        self.add_widget(self.GL)

# 4 Label        
class L4(GridLayout):
    def __init__(self,Count,ID,Order,Cost,Time,**kwargs):
        super(L4, self).__init__(**kwargs)
        self.cols=5
        #Enter For Placement of Character Order in Label
        if len(Order) > 50:
            count = len(Order)
            count = Order.find(')',int(count/2)-5,int(count/2) + 5)
            Order = Order[:count - 7] + '\n' + Order[count - 7:]
        self.size_hint_y=None
        self.height=80
        self.add_widget(TextInput(text=Count,font_name="font/arial",font_size="30",size_hint=(.1,1)))
        self.add_widget(TextInput(text=ID,font_name="font/arial",font_size="30",size_hint=(.3,1)))
        self.add_widget(Label(text=Order,size_hint=(2,1),font_name="font/arial",font_size="30"))
        self.add_widget(TextInput(text=Cost,font_name="font/arial",font_size="30",size_hint=(.3,1)))
        self.add_widget(TextInput(text=Time,size_hint=(.5,1),font_name="font/arial",font_size="20"))

class My(App):
    def build(self):
        return SGV()
My().run()
