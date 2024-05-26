import numpy as np

from src.light import Light
from src.sphere import Sphere


class Phong:

    def __init__(self, screen, light: Light, observer, k_a, k_s, k_d, n, i_a, i_p, f_att=1):
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

        I = self.k_a * self.i_a + self.i_p * (self.f_att * self.k_d * N_L + self.f_att * self.k_s * R_V ** self.n)
        return I

    def render_sphere(self, sphere: Sphere):
        for point in sphere.points:
            I = self.phong_shading(point, sphere.get_center())
            color = np.clip(np.dot(sphere.color, I), 0, 255)
            self.screen.set_at((point[0], point[1]), color)