from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class SimpleTestApp(App):
    def build(self):
        # لایه عمودی
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # یک متن ساده
        self.label = Label(text='هر چیزی بنویس و دکمه رو بزن', font_size='22sp')
        layout.add_widget(self.label)

        # یک کادر برای تایپ متن
        self.input = TextInput(hint_text='اینجا تایپ کن...', font_size='20sp', multiline=False)
        layout.add_widget(self.input)

        # یک دکمه
        btn = Button(text='کلیک کن', font_size='20sp', size_hint=(1, 0.4))
        btn.bind(on_press=self.update_text)
        layout.add_widget(btn)

        return layout

    # عملکرد دکمه
    def update_text(self, instance):
        typed_text = self.input.text
        if typed_text:
            self.label.text = f'تو اینو نوشتی: {typed_text}'
        else:
            self.label.text = 'هیچی ننوشتی!'

if __name__ == '__main__':
    SimpleTestApp().run()