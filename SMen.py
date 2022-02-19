#Screen Menu

from All_Module import GridLayout,Image,Screen,Button,App,Window
from share import Txt
from kivy.animation import Animation
from functools import partial



class SMenu(Screen,Image):
    def __init__(self, **kwargs):
        super(SMenu,self).__init__(**kwargs)
        self.GL= GridLayout(cols=1,padding=[700,70,700,70],spacing=100)
        self.source ='images/BGI/CD.jpg'
        self.GL.add_widget(Button(text=Txt(" ثبت سفارش"),font_name="font/KamranB",background_color='6402B021',font_size="70",on_release=partial(self.End, 1)))
        self.GL.add_widget(Button(text=Txt("ثبت دیگر سفارشات"),font_name="font/KamranB",background_color='6402B021',font_size="70",on_release=partial(self.End, 2)))
        self.GL.add_widget(Button(text=Txt("گزارش سفارشات"),font_name="font/KamranB",background_color='6402B021',font_size="70",on_release=partial(self.End, 3)))
        self.add_widget(self.GL)

    def End(self,id,Widget,*args):
        animation = Animation(color=(1,0,0,1),duration=.5)
        animation += Animation(color=(0,1,0,1),duration=.5)
        animation += Animation(color=(1,1,0,1),duration=.5)

        animation += Animation(color=(0,0,1,1),duration=.5)
        animation += Animation(color=(1,0,1,1),duration=.5)
        animation += Animation(color=(0,1,1,1),duration=1)
        animation.start(Widget)
        if (id == 1) :
            animation.bind(on_complete = self.Gorder)
        elif(id == 2):
            animation.bind(on_complete = self.Gother)
        elif(id == 3):
            animation.bind(on_complete = self.GGV)


    #Go Screen Order
    def Gorder(self,*args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SOrder'
    

    #Go Screen Other
    def Gother(self,*args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SOther'
    

    #Go Screen Gozaresh Vaziat
    def GGV(self,*args):
        self.manager.transition.direction = 'down'
        self.manager.current = 'SGV'



    

# class Myapp(App):
#     def build(self):
#         Window.maximize()
#         return SMenu()
        

# Myapp().run()

