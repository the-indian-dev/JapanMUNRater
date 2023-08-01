from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager

from kivy.lang import Builder


class JapanMUNApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen_manager = ScreenManager()
        ui_main = Builder.load_file("ui_main.kv")
        screen_manager.add_widget(ui_main)
        return screen_manager


JapanMUNApp().run()
