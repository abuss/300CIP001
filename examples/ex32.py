from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget

tablero = [0,0,0, 0,0,0, 0,0,0]

ximg = Image(source='x.png')
oimg = Image(source='o.png')

def set_label(btn):
    pos = int(btn.id)
    if tablero[pos]=="X":
        btn.background_normal = "o.png"
        tablero[pos]="O"
    else:
        btn.background_normal = "x.png"
        tablero[pos]="X"
    print "check triqui",tablero

class Demo(App):
    title = "Triqui"

    def build(self):
        self.width=100
        gl = GridLayout(cols=3,rows=3,size_hint=(1,1))

        for i in range(9):
            b1 = Button(id=str(i), background_normal='empty.png')
            b1.bind(on_press=set_label)
            gl.add_widget(b1)

        return gl

Demo().run()
