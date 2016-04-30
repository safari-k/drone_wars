import pymunk as pm


class BattlePhysics(pm.Space):

    def __init__(self):
        # create physics space
        super(self.__class__, self).__init__()
        self.gravity = (0, 0)
