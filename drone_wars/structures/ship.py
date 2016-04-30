import base_structure
import pymunk as pm
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix import relativelayout


class Ship(relativelayout):
    radius = NumericProperty(20)
    hue = NumericProperty(0)

    # for physics
    world = ObjectProperty(None)
    _body = ObjectProperty(None)

    def __init__(self, world, pos, **kwargs):
        super(Ship, self).__init__(**kwargs)

        self.gun = base_structure.BaseStructure(world=world, pos=pos + (0, 5))
        self.thruster = base_structure.BaseStructure(world=world, pos=pos + (0, -5))
        self.gun_to_thruster = pm.PinJoint(self.gun.body, self.thruster.body)


