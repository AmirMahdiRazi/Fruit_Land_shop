from All_Module import GridLayout,TextInput,Button,Label
from wr import write_file
import arabic_reshaper
import bidi.algorithm

def Txt(t):
    _name = arabic_reshaper.reshape(t)
    name = bidi.algorithm.get_display(_name)
    return name



li_name=[[Txt("آب کرفس"),Txt("آب هویج"),Txt("شیرموز"),Txt("آب سیب"),Txt("معجون"),Txt("شیک"),Txt("آیس پک"),Txt("آب پرتقال")],\
    [Txt("کیک ساده"),Txt("کیک شکلاتی"),Txt("شیرینی خامه‌ای"),Txt("تیرامیسو"),Txt("ذرت مکزیکی"),Txt("اسنک")],\
        [Txt("اسپرسو"),Txt("کاپوچینو"),Txt("هات چاکلت"),Txt("کافی میکس"),Txt("نسکافه"),Txt("چای ماسالا"),Txt("شیر کاکائو")],\
            [Txt("آب هویج 1 لیتری "),Txt("آب کرفس 1 لیتری"),Txt("آب سیب 1 لیتری"),Txt("آب پرتقال 1 لیتری"),Txt("شیرموز 1 لیتری")],\
                [Txt("نیمرو"),Txt("املت"),Txt("سوسیس تخم مرغ"),Txt("کره عسل")]]
li_count=[]

def reset():
    global li_count
    li_count=[]
    for i in range(len(li_name)):
        temp=[]
        for j in range(len(li_name[i])):
            temp.append(0)
        li_count.append(temp)

cost=0
li_cost=[
    [6000, 6000, 15000, 6000, 35000, 25000, 20000, 13000],
    [5000, 7000, 4000, 7000, 20000, 10000],
    [8000, 12000, 12000, 12000, 12000, 12000, 12000],
    [18000, 18000, 18000, 35000, 40000],
    [10000,15000,15000,-1]
    ]



#TextInput And 2 Button
class TI2B(GridLayout):
    #TextInput For Show Which Orders Selected
    IT_Order = TextInput(text="",halign="center",readonly=True \
            ,font_name="font/KamranB",font_size="50",background_color="031926",foreground_color=(1,1,1,1))
    IT_Cost = TextInput(text="",halign="center",readonly=True \
            ,font_name="font/KamranB",font_size="50",background_color="031926",size_hint=(1,.5),foreground_color=(1,1,1,1))
        
    def __init__(self,**kwargs):
        super(TI2B, self).__init__(**kwargs)
        
        self.cols=2
        
        
        #Two TextInput
        TTI=GridLayout(cols=1)
        TTI.add_widget(TI2B.IT_Order)
        TTI.add_widget(TI2B.IT_Cost)

        TB=GridLayout(cols=1,size_hint=(.3,1))
        TB.add_widget(Button(text=Txt("تایید"),font_name="font/KamranB",font_size="70",background_color='27FF0099',on_press=self.register))
        TB.add_widget(Button(text=Txt("لغو"),font_name="font/KamranB",font_size="70",background_color='FC0404b0',on_press=self.reset,size_hint=(1,.5)))
        
        self.add_widget(TTI)
        self.add_widget(TB)
        

    #Write on File and Reset IT and Variable
    def register(self,instance):
        if len(TI2B.IT_Order.text) != 0 :
            for i in range(len(li_name)):
                for j in range(len(li_name[i])):
                    if (li_count[i][j] != 0):
                        global cost
                        cost += li_count[i][j] * li_cost[i][j]
            write_file(TI2B.IT_Order.text,str(cost))
            TI2B.IT_Order.text = ''
            TI2B.IT_Cost.text = ''
            reset()
            
 

    # Restart All variable    
    def reset(self,intialize):
        TI2B.IT_Order.text = ''
        TI2B.IT_Cost.text = ''
    
    # Follow any changes IT
    def refresh(self):
        TI2B.IT_Order.text = ''
        TI2B.IT_Cost.text = ''
        cal=0
        for i in range(len(li_name)):
            for j in range(len(li_name[i])):
                if li_count[i][j] > 0 :
                    TI2B.IT_Order.text += f' و ({li_count[i][j]}){li_name[i][j]}'
                    cal += li_count[i][j] * li_cost[i][j]
            cost = cal 
        TI2B.IT_Cost.text = f'{cost}' 


        



