from kivy.app import App
from kivy.uix.button import Button

class ButtonAction(App):
    def build(self):
        self.count = 0
        self.letter = ''
        self.button = Button(
            text = 'Hello Everyone!',
            size_hint = ( .5, .5),
            pos_hint = {'center_x': .5, 'center_y': .5}
        )
        self.button.bind(on_press=self.on_press_button)

        return self.button

    def on_press_button(self, instance):
        self.count += 1
        if self.count != 1:
           self.letter = 's'

        print('Your press the button')
        instance.text = f'The button was pressed {self.count} time{self.letter}'



if __name__ == '__main__':
    app = ButtonAction()
    app.run()
