class Light:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def move(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz

    def get_position(self):
        return self.x, self.y, self.z

    def get_position_3d(self):
        return self.get_position()

    def get_position_2d(self):
        return self.x, self.y
