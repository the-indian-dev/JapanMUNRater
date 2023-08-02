from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivymd.toast import toast

from kivy.lang import Builder

import requests
import json

url = "https://munjapan-aad9.restdb.io/rest/main"
headers = {
    'content-type': "application/json",
    'x-apikey': "7328b39783cfc8a0ce4599d2a33ed65f6c5f1",
    'cache-control': "no-cache"
}


class JapanMUNApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen_manager = ScreenManager()
        self.ui_main = Builder.load_file("ui_main.kv")
        self.stars = [self.ui_main.ids.star1, self.ui_main.ids.star2, self.ui_main.ids.star3, self.ui_main.ids.star4,
                      self.ui_main.ids.star5]
        self.current_rate = -1
        screen_manager.add_widget(self.ui_main)
        return screen_manager

    def push_results(self, name: str, rating: int, review: str):
        payload = json.dumps({"name": name, "rating": rating, "review": review})
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)

    def push_data(self, name, review):
        print("Starting Data Push")
        print(name, review)
        print(self.current_rate)
        if self.current_rate == -1:
            toast("Please rate your experience")
        elif name == "":
            toast("Please write your name")
        else:
            #print("TEST!")
            self.ui_main.ids.name.text, self.ui_main.ids.review.text = ("", "")
            self.push_results(name, self.current_rate, review)
            toast("Thank you for sharing your feedback!")
            self.clear_stars()

    def clear_stars(self):
        for star in self.stars:
            star.icon = 'star-outline'
        self.current_rate = -1

    def on_rate(self, number: int):
        self.clear_stars()
        for i in range(number):
            cur_star = self.stars[i]
            cur_star.icon = 'star'
        print(self.current_rate)
        self.current_rate = number


JapanMUNApp().run()
