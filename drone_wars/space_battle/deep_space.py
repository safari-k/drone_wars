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

        a_ship = Ship(world=self.physics, pos=(500, 500))
        self.structures.append(a_ship)
        self.add_widget(a_ship)


# Declare both screens
class MenuScreen(Screen):
    def __init__(self, *args, **kwargs):
        # create physics space
        super(MenuScreen, self).__init__(*args, **kwargs)
        self.add_widget(Button(text='Hello world 1'))
    pass


class BattleApp(App):
    def __init__(self, **kwargs):
        super(BattleApp, self).__init__(**kwargs)
        self.current_battle = None

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        self.current_battle = DeepSpace(name='DeepSpace')
        sm.add_widget(self.current_battle)

        return sm

if __name__ == '__main__':
    BattleApp().run()
