import battle_physics
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button


class BaseBattle(Screen):

    def __init__(self, *args, **kwargs):
        # create physics space
        super(BaseBattle, self).__init__(**kwargs)
        self._physics = battle_physics.BattlePhysics()

        self.add_widget(Button(text='A button', size_hint=(0.1, 0.1)))


        pass

    def next_turn(self):
        # if cmd queue full then run

        pass

    def display_commands(self):
        pass

    def display_queue(self):
        pass

    def execute_commands(self):
        pass

    def queue_command(self, cmd):
        pass
