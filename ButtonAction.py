from kivy.app import App
from kivy.uix.button import Button

class ButtonAction(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
        self.letter = ''
        self.button = None

    def build(self):
        self.button = Button(
            text = 'Hello Everyone!',
            size_hint = ( .5, .5),
            pos_hint = {'center_x': .5, 'center_y': .5}
        )
        self.button.bind(on_press=self.on_press_button)
        return self.button

    def on_press_button(self, instance):
        self.count += 1
        self.letter = 's' if self.count != 1 else ''

        print('Your press the button')
        instance.text = f'The button was pressed {self.count} time{self.letter}'



if __name__ == '__main__':
    app = ButtonAction()
    app.run()