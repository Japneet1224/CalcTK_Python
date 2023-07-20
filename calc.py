from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Calculator(App):
    def build(self):
        self.expression = ""

        main_layout = BoxLayout(orientation="vertical")

        display = Button(text="0", font_size=40, size_hint=(1, 0.75))
        display.bind(on_press=self.display_button_press)
        main_layout.add_widget(display)

        button_layout = BoxLayout()

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "=", "+"],
            ["<=", ">=", "==", "+="],
            ["-=", "!=", "<!=", ">!="]
        ]

        for button in buttons:
            btn = Button(text=button, font_size=40)
            btn.bind(on_press=self.button_press)
            button_layout.add_widget(btn)

        main_layout.add_widget(button_layout)

        return main_layout

    def button_press(self, instance):
        if instance.text == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"
        else:
            self.expression += instance.text

        self.root.children[0].text = self.expression

    def display_button_press(self, instance):
        self.expression = ""
        self.root.children[0].text = "0"


if __name__ == "__main__":
    Calculator().run()
