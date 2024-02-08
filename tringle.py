import numpy as np
from vector import Vector
from rect import Rect
import pygame




class Triangle:
    def __init__(self, point1, point2, point3):
        """
        Initialisiert ein Dreieck mit drei Punkten.

        Args:
            point1 (Vector): Der erste Punkt des Dreiecks als Vektor.
            point2 (Vector): Der zweite Punkt des Dreiecks als Vektor.
            point3 (Vector): Der dritte Punkt des Dreiecks als Vektor.
        """
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def calculate_vertices(self):
        """
        Berechnet die Eckpunkte des Dreiecks.

        Returns:
            Eine Liste von Vektoren, die die Eckpunkte des Dreiecks darstellen.
        """
        return [self.point1, self.point2, self.point3]

    def is_collision(self, ball):
        tri_vertices = self.calculate_vertices()

        # Erstelle ein Rechteck um den Ball
        ball_rect = Rect(Vector(ball.position.x - ball.radius, ball.position.y - ball.radius),
                         ball.radius * 2, ball.radius * 2)

        normals = []
        overlaps = []
        for i in range(len(tri_vertices)):
            edge = tri_vertices[(i + 1) % len(tri_vertices)] - tri_vertices[i]
            normal = Vector(-edge.y, edge.x).normalize()
            normals.append(normal)

            # Berechne Projektionen für das Dreieck und das Ball-Rechteck
            tri_projections = [p.dot(normal) for p in tri_vertices]
            ball_rect_projections = [p.dot(normal) for p in ball_rect.calculate_vertices()]

            min_tri = min(tri_projections)
            max_tri = max(tri_projections)
            min_ball_rect = min(ball_rect_projections)
            max_ball_rect = max(ball_rect_projections)

            overlap = min(max_tri, max_ball_rect) - max(min_tri, min_ball_rect)
            overlaps.append(overlap)

            # Überprüfe die Kollision zwischen dem Ball-Rechteck und dem Dreieck
            if max_ball_rect < min_tri or min_ball_rect > max_tri:
                # Es gibt eine separierende Achse!
                return False, 0

        # Wenn keine separierende Achse gefunden wurde, gibt es eine Kollision
        min_overlap = (np.argmin(overlaps), np.min(overlaps))
        return True, normals[min_overlap[0]]
    
    
    def draw_triangle(self, screen):
        triangle_vertices = self.calculate_vertices()
        pygame.draw.polygon(screen, (255, 0, 0), [(v.x, v.y) for v in triangle_vertices],5)
