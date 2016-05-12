import base_battle
from drone_wars.structures.ship import Ship
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.button import Button


class DeepSpace(base_battle.BaseBattle):
    def __init__(self, *args, **kwargs):
        # create physics space
        super(DeepSpace, self).__init__(*args, **kwargs)

        self.add_widget(Ship(world=self._physics, pos=(50, 50)))


# Declare both screens
class MenuScreen(Screen):
    def __init__(self, *args, **kwargs):
        # create physics space
        super(MenuScreen, self).__init__(*args, **kwargs)
        self.add_widget(Button(text='Hello world 1'))
    pass


class BattleApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(DeepSpace(name='DeepSpace'))
        return sm

if __name__ == '__main__':
    BattleApp().run()
