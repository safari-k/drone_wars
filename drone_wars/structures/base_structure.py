import structure_physics
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty


class BaseStructure(Widget):
    # for physics
    world = ObjectProperty(None)
    _body = ObjectProperty(None)

    def __init__(self, world, pos, **kwargs):
        super(Widget, self).__init__(**kwargs)
        self.world = world
        self.pos = pos
        self.physics = structure_physics.StructurePhysics(world=world, pos=pos)

    def update_from_physics(self):
        self.pos = self.physics.body.position.x, self.physics.body.position.y

