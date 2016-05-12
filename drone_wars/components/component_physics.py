import pymunk as pm


class ComponentPhysics:
    def __init__(self, world, pos):
        self.world = world

        vertices = [(-10, 10), (10, 10), (20, -10), (-20, -10)]
        mass = 10
        inertia = pm.moment_for_poly(mass, vertices,  offset=(0, 0), radius=0)
        self.body = pm.Body(mass, inertia)
        self.body.position = pos
        shape = pm.Poly(self.body, vertices, transform=None, radius=0)
        shape.elasticity = 0.95
        self.world.add(self.body, shape)
