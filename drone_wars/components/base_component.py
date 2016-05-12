import component_physics
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.graphics import Color, Rectangle


class BaseComponent(Widget):
    # for physics
    world = ObjectProperty(None)
    _body = ObjectProperty(None)

    def __init__(self, world, pos, **kwargs):
        super(BaseComponent, self).__init__(**kwargs)
        self.world = world
        self.pos = pos
        self.physics = component_physics.ComponentPhysics(world=world, pos=pos)

        with self.canvas:
            # Add a red color
            Color(1., 0, 0)
            # Add a rectangle
            Rectangle(pos=pos, size=(10, 10))

    def update_from_physics(self):
        self.pos = self.physics.body.position.x, self.physics.body.position.y

