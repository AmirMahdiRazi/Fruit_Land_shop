#Page Warm Drink
from All_Module import *
from wr import *
from functools import partial
from share import Txt,TI2B
import share

page_Number = 2

class MyPWD(GridLayout,Image):
    def __init__(self):
        super(MyPWD,self).__init__()
        
        self.cols=1
        self.source ='images/BGI/CD.jpg'
        self.padding=25
        self.add_widget(Items())


#Items
class Items(GridLayout):
    def __init__(self):
        super(Items, self).__init__()
        self.cols=4
        self.size_hint=(1,5)
        self.add_widget(IBL('WE',share.li_name[page_Number][0],0))
        self.add_widget(IBL('WK',share.li_name[page_Number][1],1))
        self.add_widget(IBL('WHCH',share.li_name[page_Number][2],2))
        self.add_widget(IBL('WCM',share.li_name[page_Number][3],3))
        self.add_widget(IBL('WNC',share.li_name[page_Number][4],4))
        self.add_widget(IBL('WCHM',share.li_name[page_Number][5],5))
        self.add_widget(IBL('WSHK',share.li_name[page_Number][6],6))

#Image Button And Label
class IBL(BoxLayout):
    def __init__(self,ad,txt,id,**kwargs):
        super(IBL, self).__init__(**kwargs)
        self.orientation='vertical'
        self.padding=25


        self.add_widget(Button(background_normal = 'images/PWD/{}.png'.format(ad),\
            size_hint=(1, 1.5),background_down ='images/PWD/{}_Press.png'.format(ad),on_press=partial(self.Choise, id)))
            
        self.add_widget(Label(text=txt,font_name="font/arial",\
            font_size="35",color = (1,0,1,1),size_hint=(1,.15)))

    #Function for Found Which Button Selected
    def Choise(self,id,instance):
        share.li_count[page_Number][id] += 1
        TI2B.refresh(self)



# class Myapp(App):
#     def build(self):
#         Window.maximize()
#         return MyPWD()
        

# Myapp().run()