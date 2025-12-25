from kivy.app import App
from kivy.uix.label import Label

class OfflineApp(App):
    def build(self):
        return Label(text="مرحباً! هذا تطبيق تحويل الكلام أوفلاين")

if __name__ == "__main__":
    OfflineApp().run()
