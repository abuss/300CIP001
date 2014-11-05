from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


def set_label(btn):
    if btn.text=="X":
        btn.text = "O"
    else:
        btn.text = "X"

class Demo(App):
    title = "Triqui"

    def build(self):
        self.width=100
        gl = GridLayout(cols=3,rows=3, row_force_default=True, row_default_height=40,
                        col_force_default=True, col_default_width=40)

        b1 = Button(font_size=30)
        b1.bind(on_press=set_label)
        gl.add_widget(b1)

        b2 = Button(font_size=30)
        b2.bind(on_press=set_label)
        gl.add_widget(b2)

        b3 = Button(font_size=30)
        b3.bind(on_press=set_label)
        gl.add_widget(b3)

        b4 = Button(font_size=30)
        b4.bind(on_press=set_label)
        gl.add_widget(b4)

        b5 = Button(font_size=30)
        b5.bind(on_press=set_label)
        gl.add_widget(b5)

        b6 = Button(font_size=30)
        b6.bind(on_press=set_label)
        gl.add_widget(b6)

        b7 = Button(font_size=30)
        b7.bind(on_press=set_label)
        gl.add_widget(b7)

        b8 = Button(font_size=30)
        b8.bind(on_press=set_label)
        gl.add_widget(b8)

        b9 = Button(font_size=30)
        b9.bind(on_press=set_label)
        gl.add_widget(b9)

        return gl

Demo().run()
