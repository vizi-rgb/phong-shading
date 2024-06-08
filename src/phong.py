import numpy as np

from src.light import Light
from src.sphere import Sphere


class Phong:

    def __init__(self, screen, light: Light, observer, k_a, k_s, k_d, n, i_a, i_p, f_att=None):
        self.screen = screen
        self.light = light
        self.observer = observer
        self.k_a = k_a
        self.k_s = k_s
        self.k_d = k_d
        self.n = n
        self.i_a = i_a
        self.i_p = i_p
        self.f_att = f_att

    def normalize(self, v):
        norm = np.linalg.norm(v)
        return v if norm == 0 else v / norm

    def phong_shading(self, point, sphere_center):
        point = np.array(point)
        N = self.normalize(point - sphere_center)
        L = self.normalize(np.array(self.light.get_position()) - point)
        V = self.normalize(np.array(self.observer) - point)
        R = 2 * np.dot(L, N) * N - L

        N_L = max(np.dot(N, L), 0.0)
        R_V = max(np.dot(R, V), 0.0)

        if not self.f_att:
            distance = self.get_distance(point, self.light.get_position())
            c1 = 0.1
            c2 = 0.001
            c3 = 1e-6
            f_att = min(1 / (c1 + c2 * distance + c3 * distance ** 2), 1)
        else:
            f_att = self.f_att

        I = self.k_a * self.i_a + f_att * self.i_p * (self.k_d * N_L + self.k_s * R_V ** self.n)
        return np.clip(I, 0, 1)

    def get_distance(self, point1, point2):
        distance = np.linalg.norm(np.array(point1) - np.array(point2))
        return distance

    def render_sphere(self, sphere: Sphere):
        for point in sphere.points:
            I = self.phong_shading(point, sphere.get_center())
            color = np.clip(np.multiply(sphere.color, I), 0, 255)
            self.screen.set_at((point[0], point[1]), color)