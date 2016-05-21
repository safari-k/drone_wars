import battle_physics
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.clock import Clock


class BaseBattle(Screen):

    def __init__(self, *args, **kwargs):
        # create physics space
        super(BaseBattle, self).__init__(**kwargs)
        self.physics = battle_physics.BattlePhysics()

        next_turn_button = Button(text='Next Turn', size_hint=(0.1, 0.1))
        next_turn_button.bind(on_press=self.next_turn)
        self.add_widget(next_turn_button)

        self.structures = []  # stores any ships or asteroids or whatever

    def next_turn(self, touch):
        # if cmd queue full then run

        Clock.schedule_interval(self.update_world, 1 / 60.)
        Clock.schedule_once(self.stop_update, 2)

    def update_world(self, dt):
        self.physics.step(dt)
        for child in self.structures:
            child.update_from_physics()

    def stop_update(self, dt):
        print(dt)
        Clock.unschedule(self.update_world)

    def display_commands(self):
        pass

    def display_queue(self):
        pass

    def execute_commands(self):
        pass

    def queue_command(self, cmd):
        pass
