from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.display = TextInput(font_size=40, size_hint=(1, 0.4))
        layout.add_widget(self.display)

        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','-'],
            ['.','0','=','+']
        ]

        for row in buttons:
            button_row = BoxLayout()
            for label in row:
                button = Button(text=label)
                button.bind(on_release=self.button_pressed)
                button_row.add_widget(button)
            layout.add_widget(button_row)

        return layout

    def button_pressed(self,button):
        current = self.display.text
        button_text = button.text

        if button_text == '=':
            try:
                result = str(eval(current))
                self.display.text = result
            except Exception:
                self.display.text = 'Error'
        else:
            self.display.text = current + button_text


if __name__ == '__main__':
    Calculator().run()
