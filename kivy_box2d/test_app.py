import Box2D as b2d

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_string('''
<Circle>:
    canvas:
        Color:
            hsv: self.hue, 1, 1
        Ellipse:
            pos: self.x - self.radius, self.y - self.radius
            size: self.radius * 2, self.radius * 2
''')


class Circle(Widget):
    radius = NumericProperty(20)
    hue = NumericProperty(0)

    # for physics
    world = ObjectProperty(None)
    _body = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Circle, self).__init__(**kwargs)
        self.hue = random()

        # Ball
        self._body = self.world.CreateDynamicBody(
            fixtures=b2d.b2FixtureDef(
                shape=b2d.b2CircleShape(radius=self.radius),
                density=1.0, friction=0.3),
            bullet=True,
            position=self.pos)
        # self._body.SetMassFromShapes()

    def update_from_body(self):
        self.pos = self._body.position.x, self._body.position.y


class PhysicsApp(App):
    def generate_one(self, instance, touch):
        c = Circle(pos=touch.pos, world=self.world)
        self.circles.append(c)
        self.root.add_widget(c)

    def build(self):
        root = Widget()
        root.bind(on_touch_move=self.generate_one)

        self.world = world = b2d.b2World(gravity=(0, -100))

        # plane for the ground, all other the window.
        # The ground
        ground = self.world.CreateBody(
            shapes=b2d.b2EdgeShape(vertices=[(0, 0), (1000, 0)])
        )

        # generate circles
        self.circles = []
        for x in xrange(5):
            c = Circle(y=500 + x * 5, x=500+x, world=world)
            self.circles.append(c)
            root.add_widget(c)
        Clock.schedule_interval(self._update_world, 1 / 60.)

        return root

    def _update_world(self, dt):
        self.world.Step(dt, 10, 8)
        for child in self.circles:
            child.update_from_body()

if __name__ == '__main__':
    PhysicsApp().run()
