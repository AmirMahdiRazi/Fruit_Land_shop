#Screen Order


from All_Module import App,TabbedPanel,TabbedPanelHeader,GridLayout,Window,Screen,ScreenManager
from PCDP import MyPCDP
from PWD import MyPWD
from PBF import MyPBF
from PD import MyPD
from PCDL import MyPCDL
from PME import MyPME
from wr import write_file
from share import Txt,TI2B,reset

reset()

#Screen Order
class SOrder(Screen):
    def __init__(self,**kwargs):
        super(SOrder, self).__init__(**kwargs)
        tb_panel= TabbedPanel()
        tb_panel.do_default_tab=False
        tb_panel.background_color=(0,0,0,0)
        tb_panel.border=[0,0,0,0]
        tb_panel.tab_width=300
        #  Create text tab

        # Page Cold Drink 1 Person
        th_PCDP = TabbedPanelHeader(text=Txt("نوشیدنی سرد(تک نفره)"),font_name="font/arial",font_size="35") 
        th_PCDP.content= MyPCDP()
            
        # #  Create image tab
        th_DS= TabbedPanelHeader(text=Txt("دسر"),font_name="font/arial",font_size="35")
        th_DS.content= MyPD()

        # #  Create Page Warn Drink
        th_PWD = TabbedPanelHeader(text=Txt("نوشیدنی گرم"),font_name="font/arial",font_size="35")
        th_PWD.content= MyPWD()

        # # Create Page Cold Drink Liter
        th_PCDL = TabbedPanelHeader(text=Txt("نوشیدنی سرد(لیتری)"),font_name="font/arial",font_size="35")
        th_PCDL.content= MyPCDL()

        # # Create Page BF
        th_PBF = TabbedPanelHeader(text=Txt("صبحانه"),font_name="font/arial",font_size="35")
        th_PBF.content= MyPBF()

        # # Create Page ME
        th_PME = TabbedPanelHeader(text=Txt("موارد دیگر"),font_name="font/arial",font_size="35")
        th_PME.content= MyPME()


        tb_panel.add_widget(th_PCDP)
        tb_panel.add_widget(th_DS)
        tb_panel.add_widget(th_PWD)
        tb_panel.add_widget(th_PCDL)
        tb_panel.add_widget(th_PBF)
        tb_panel.add_widget(th_PME)
            
        _GL= GridLayout(cols=1)
        _GL.add_widget(tb_panel)
        _GL.add_widget(TI2B(size_hint=(1,.3)))
        Window.maximize()
        self.add_widget(_GL)
        

    def ChangePage(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Country'
#         return GL


# TabbedPanelApp().run()

class myapp(App):
    def build(self):
        return SOrder()
myapp().run()
