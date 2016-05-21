import pymunk as pm


class BattlePhysics(pm.Space):

    def __init__(self):
        # create physics space
        super(BattlePhysics, self).__init__()
        self.gravity = (0, -10)
