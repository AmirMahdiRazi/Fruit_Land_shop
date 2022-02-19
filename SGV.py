



from All_Module import TextInput,Image,ScrollView, App,TabbedPanel,TabbedPanelHeader,GridLayout,Window,Screen,Button,Label
import wr 
from Text import *
from share import Txt
from functools import partial
from persiantools.jdatetime import JalaliDateTime
#Variable
_txt = []
result = []

#Screen Order
class MySGV(Screen,Image):
    def __init__(self,**kwargs):
        super(MySGV, self).__init__(**kwargs)
        self.source = 'images/BGI/CD.jpg'
        self.cols=1
        tb_panel= TabbedPanel()
        tb_panel.do_default_tab=False
        tb_panel.background_color=(0,0,0,0)
        tb_panel.border=[0,0,0,0]
        tb_panel.tab_width=300
        tb_panel.size_hint=(1,.17)
        #  Create text tab

        # tab Report Day
        tp_rd = TabbedPanelHeader(text=Txt("گزارش روزانه"),font_name="font/arial",font_size="35") 
        rd = TIDGL()
        tp_rd.content = rd
       

        # tab report Monthly
        tp_rm = TabbedPanelHeader(text=Txt("گزارش ماهانه"),font_name="font/arial",font_size="35") 
        rm = TIMGL()
        tp_rm.content = rm

        tb_panel.add_widget(tp_rd)
        tb_panel.add_widget(tp_rm)
        
        
            
        _GL= GridLayout(cols=1)
        


        _GL.add_widget(tb_panel)
        _GL.add_widget(GVD())
        _GL.add_widget(CC())
        # Create Button For Back On menu
        _GLB=GridLayout(cols=3,size_hint=(1,.09))
        _GLB.add_widget(Label())
        _GLB.add_widget(Button(text=Txt("منو"),font_name="font/arial",font_size="35",\
            size_hint =(.5, .25),background_color='00FFD8',on_release=self.ChangePage))
        _GLB.add_widget(Label())
        # End


        _GL.add_widget(_GLB)
        Window.maximize()
        self.add_widget(_GL)
        

    def ChangePage(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'SMenu'

#For insert Date Time
class TIDGL(GridLayout):
    def __init__(self,**kwargs):
        super(TIDGL, self).__init__(**kwargs)
        self.cols=4
        self.padding=[self.width/.3,15,self.width/.3,15]
        self.spacing=100
        self.time =JalaliDateTime.now().strftime("%x => %Y %B %A %X")
        self.time=str(self.time).split(' ')
        self.time=self.time[0].replace('/','-')
        self.TI_y=TextInput(text=self.time[:2],size_hint=(1,1),font_name="font/arial",font_size="35",halign="center")
        self.add_widget(self.TI_y)

        self.TI_m=TextInput(text=self.time[3:5],size_hint=(1,1),font_name="font/arial",font_size="35",halign="center")
        self.add_widget(self.TI_m)

        self.TI_d=TextInput(text=self.time[6:8],size_hint=(1,1),font_name="font/arial",font_size="35",halign="center")
        self.add_widget(self.TI_d)

       
        # self.add_widget(Button(text=Txt('جستجو'),size_hint=(1,1),font_name="font/arial",font_size="35",on_release=partial(SV.rebuilding, self.date)))
        self.add_widget(Button(text=Txt('جستجو'),size_hint=(1,1),font_name="font/arial",font_size="35",on_release=partial(self.search)))
        

    def search(self,instance):
        global _txt,result
        cost = 0
        self.head = False
        self.date=f'{self.TI_y.text}-{self.TI_m.text}-{self.TI_d.text}'
        _txt =wr.read_file(self.date)
        if _txt != False:
            result = []
            for _ in range(0,len(_txt)):
                res=_txt[_].split(',')
                result.append([res[0],res[1],res[2],res[3]])
                if self.head:
                        cost += int(res[2])
                self.head=True
                
        else :
            result = []
        
        SV.rebuilding(SV,self.date)
        CC.Create(CC,str(cost))

class TIMGL(GridLayout):
    def __init__(self,**kwargs):
        super(TIMGL, self).__init__(**kwargs)
        self.cols=4
        self.padding=[self.width/.3,15,self.width/.3,15]
        self.spacing=100
        
        self.time =JalaliDateTime.now().strftime("%x => %Y %B %A %X")
        self.time=str(self.time).split(' ')
        self.time=self.time[0].replace('/','-')
        self.TI_y=TextInput(text=self.time[:2],size_hint=(1,1),font_name="font/arial",font_size="35",halign="center")
        self.add_widget(self.TI_y)

        self.TI_m=TextInput(text=self.time[3:5],size_hint=(1,1),font_name="font/arial",font_size="35",halign="center")
        self.add_widget(self.TI_m)


       
        # self.add_widget(Button(text=Txt('جستجو'),size_hint=(1,1),font_name="font/arial",font_size="35",on_release=partial(SV.rebuilding, self.date)))
        self.add_widget(Button(text=Txt('جستجو'),size_hint=(1,1),font_name="font/arial",font_size="35",on_release=partial(self.search)))
        

    def search(self,instance):
        global _txt,result
        self.head = False
        self.date=f'{self.TI_y.text}-{self.TI_m.text}'
        _txt =wr.read_file(self.date)
        cost = 0
        if _txt != False:
            result = []
            for _ in range(len(_txt)):
                for i in range(len(_txt[_])):
                    res=_txt[_][i].split(',')
                    result.append([res[0],res[1],res[2],res[3]])
                    if self.head:
                        cost += int(res[2])
                    self.head=True
                    
        else :
            result = []
        
        SV.rebuilding(SV,self.date)
        CC.Create(CC,str(cost))

#Gozaresh Vaziat
class GVD(GridLayout):
    def __init__(self,**kwargs):
        super(GVD, self).__init__(**kwargs)
        self.cols=1
        self.padding=[50,50,50,50]
        self.add_widget(SV())
        



# ScrollView With L5(5 Label)
class SV(ScrollView):
    
    def __init__(self,**kwargs):
        super(SV, self).__init__(**kwargs)
        global result
        SV.GL=GridLayout(cols=1,size_hint_y=None)
        SV.GL.bind(minimum_height=SV.GL.setter('height'))
        SV.GL.size_hint=(1, None)
        SV.GL.size=(Window.width, Window.height)
        SV.GL.do_scroll_x = False
        SV.GL.do_scroll_y = True
        
        if len(result) > 0:
            
            for i in range(len(result)):
                btn = L5(str(i+1),result[i][0],result[i][1],result[i][2],result[i][3])
                SV.GL.add_widget(btn)
                
        else:
            
            btn = Label(text=Txt('تاریخی انتخاب نشده است'),font_name="font/arial",font_size="50")
            SV.GL.add_widget(btn)
        self.add_widget(SV.GL)
    

    def rebuilding(__class__,date):
        global result
        
        SV.GL.clear_widgets()
        if len(result) > 0:
            for i in range(len(result)):
                btn = L5(str(i+1),result[i][0],result[i][1],result[i][2],result[i][3])
                SV.GL.add_widget(btn)
                
        else:
            
            btn = Label(text=Txt('هیچ موردی یافت نشد(ثبت سفارشی در آن روز نداشته اید)'),font_name="font/arial",font_size="50",height=80)
            SV.GL.add_widget(btn)

# 5 Label        
class L5(GridLayout):
    def __init__(self,Count,ID,Order,Cost,Time,**kwargs):
        super(L5, self).__init__(**kwargs)
        self.cols=5
        #Enter For Placement of Character Order in Label
        if len(Order) > 50:
            count = len(Order)
            count = Order.find(')',int(count/2)-5,int(count/2) + 5)
            Order = Order[:count - 7] + '\n' + Order[count - 7:]
        self.size_hint_y=None
        self.height=80
        self.add_widget(Button(text=Count,font_name="font/arial",font_size="30",size_hint=(.1,1),background_color='AC1680',disabled=True))
        self.add_widget(Button(text=ID,font_name="font/arial",font_size="30",size_hint=(.32,1),background_color='AC1680',disabled=True))
        self.add_widget(Button(text=Order,size_hint=(2,1),font_name="font/arial",font_size="30",background_color='AC1680',disabled=True))
        self.add_widget(Button(text=Cost,font_name="font/arial",font_size="30",size_hint=(.3,1),background_color='AC1680',disabled=True))
        self.add_widget(Button(text=Time,size_hint=(.45,1),font_name="font/arial",font_size="20",background_color='AC1680',disabled=True))

#Calculate Cost
class CC(GridLayout):
    
    def __init__(self,**kwargs):
        super(CC, self).__init__(**kwargs)
        GL= GridLayout(cols=1)
        GL.add_widget(Button())
        CC.cols=2
        CC.padding=[1500,0,50,0]
        CC.BT_Cost = Button(text='',font_name="font/arial",font_size="30",background_color=(0,0,0,0))
        CC.BT_CC = Button(text='',font_name="font/arial",font_size="30",background_color=(0,0,0,0))
        self.add_widget(CC.BT_CC)
        self.add_widget(CC.BT_Cost)
        self.size_hint=(1,.1)
        self.spacing = 15
    def Create(self,cost):
        CC.BT_Cost.text = Txt('جمع کل')
        CC.BT_CC.text = cost
        
        

# class My(App):
#     def build(self):
#         return SGV()
# My().run()
