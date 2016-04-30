import battle_physics
from kivy.uix.screenmanager import Screen


class BaseBattle(Screen):

    def __init__(self):
        # create physics space
        self._physics = battle_physics.BattlePhysics()

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
