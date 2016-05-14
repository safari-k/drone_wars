import base_battle
from drone_wars.structures.ship import Ship
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

from kivy.app import App
from kivy.uix.button import Button
from kivy.clock import Clock


class DeepSpace(base_battle.BaseBattle):
    def __init__(self, *args, **kwargs):
        # create physics space
        super(DeepSpace, self).__init__(*args, **kwargs)

        self.structures = []
        a_ship = Ship(world=self._physics, pos=(500, 500))
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

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        self.current_battle = DeepSpace(name='DeepSpace')
        sm.add_widget(self.current_battle)

        Clock.schedule_interval(self._update_world, 1 / 60.)

        return sm

    def _update_world(self, dt):
        self.current_battle._physics.step(dt)
        for child in self.current_battle.structures:
            child.update_from_physics()

if __name__ == '__main__':
    BattleApp().run()
