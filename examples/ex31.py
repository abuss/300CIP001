from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

tablero = [0,0,0, 0,0,0, 0,0,0]

def set_label(btn):
    pos = int(btn.id)
    if btn.text=="X":
        btn.text = "O"
        tablero[pos]="O"
    else:
        btn.text = "X"
        tablero[pos]="X"
    print "check triqui",tablero

class Demo(App):
    title = "Triqui"

    def build(self):
        self.width=100
        gl = GridLayout(cols=3,rows=3, row_force_default=True, row_default_height=40,
                        col_force_default=True, col_default_width=40)

        for i in range(9):
            b1 = Button(id=str(i),font_size=30)
            b1.bind(on_press=set_label)
            gl.add_widget(b1)

        return gl

Demo().run()
