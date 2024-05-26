from math import sqrt
class Sphere:
    def __init__(self, radius, x0, y0, z0, color):
        self.radius = radius
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.color = color
        self.points = self.__sphere_points()

    def get_center(self):
        return self.x0, self.y0, self.z0

    def __sphere_points(self):
        points = []
        for x in range(-self.radius, self.radius):
            for y in range(-self.radius, self.radius):
                if x**2 + y**2 <= self.radius**2:
                    z = sqrt(self.radius**2 - x**2 - y**2)
                    points.append((self.x0 + x, self.y0 + y, self.z0 + z))

        return points
