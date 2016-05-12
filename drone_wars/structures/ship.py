import drone_wars.components.base_component as base_component
import pymunk as pm
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.relativelayout import RelativeLayout


class Ship(RelativeLayout):
    radius = NumericProperty(20)
    hue = NumericProperty(0)

    # for physics
    world = ObjectProperty(None)
    _body = ObjectProperty(None)

    def __init__(self, world, pos, **kwargs):
        super(Ship, self).__init__(**kwargs)

        self.gun = base_component.BaseComponent(world=world, pos=(pos[0] + 0, pos[1] + 10))
        self.thruster = base_component.BaseComponent(world=world, pos=(pos[0] + 0, pos[1] + 0))
        self.gun_to_thruster = pm.PinJoint(self.gun.physics.body, self.thruster.physics.body)
        self.add_widget(self.gun)
        self.add_widget(self.thruster)


