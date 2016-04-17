import pymunk as pm

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

        mass = 10
        inertia = pm.moment_for_circle(mass, 0, self.radius, (0,0))
        self._body = pm.Body(mass, inertia)
        self._body.position = self.pos
        shape = pm.Circle(self._body, self.radius, (0,0))
        shape.elasticity = 0.95
        self.world.add(self._body, shape)

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

        ### Physics stuff
        self.world = pm.Space()
        self.world.gravity = (0.0, -100.0)

        ### walls
        static_lines = [pm.Segment(self.world.static_body, (0.0, 200.0), (1000.0,200.0), 5)]
        for line in static_lines:
            line.elasticity = 0.95
        self.world.add(static_lines)


        # generate circles
        self.circles = []
        for x in xrange(5):
            c = Circle(y=500 + x * 5, x=500+x, world=self.world)
            self.circles.append(c)
            root.add_widget(c)
        Clock.schedule_interval(self._update_world, 1 / 60.)

        return root

    def _update_world(self, dt):
        self.world.step(dt)
        for child in self.circles:
            child.update_from_body()

if __name__ == '__main__':
    PhysicsApp().run()
