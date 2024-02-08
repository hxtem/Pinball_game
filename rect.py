import pygame
import random
import numpy as np
import math
from vector import Vector


class Rect:
    def __init__(self, position : Vector, width : float, height: float):
        """
        Initialisiert ein Rechteck mit einer Position, Breite und Höhe.

        Args:
            position (Vector): Die Position des Rechtecks als Vektor.
            width (float or int): Die Breite des Rechtecks.
            height (float or int): Die Höhe des Rechtecks.
        """
        self.position = position  # Die Position des Rechtecks
        self.width = width  # Die Breite des Rechtecks
        self.height = height  # Die Höhe des Rechtecks

    def calculate_vertices(self):
        """
        Berechnet die Eckpunkte des Rechtecks.

        Returns:
            Eine Liste von Vektoren, die die Eckpunkte des Rechtecks darstellen.
        """
        return [
            Vector(self.position.x, self.position.y),
            Vector(self.position.x + self.width, self.position.y),
            Vector(self.position.x + self.width, self.position.y + self.height),
            Vector(self.position.x, self.position.y + self.height)
        ]

    def is_collision(self, ball):
        rect_vertices = self.calculate_vertices()
        
        # Erstelle ein Rechteck um den Ball
        ball_rect = Rect(Vector(ball.position.x - ball.radius, ball.position.y - ball.radius),
                         ball.radius * 2, ball.radius * 2)

        normals = []
        overlaps = []
        for i in range(len(rect_vertices)):
            edge = rect_vertices[(i + 1) % len(rect_vertices)] - rect_vertices[i]
            normal = Vector(-edge.y,edge.x).normalize()
            normals.append(normal)

            # Berechne Projektionen für das Rechteck und das Ball-Rechteck
            rect_projections = [p.dot(normal) for p in rect_vertices]
            ball_rect_projections = [p.dot(normal) for p in ball_rect.calculate_vertices()]

            min_rect = min(rect_projections)
            max_rect = max(rect_projections)
            min_ball_rect = min(ball_rect_projections * 2)
            max_ball_rect = max(ball_rect_projections * 2)

            overlap =  min(max_rect, max_ball_rect) - max(min_rect, min_ball_rect)
            overlaps.append(overlap)

            # Überprüfe die Kollision zwischen dem Ball-Rechteck und dem Rechteck
            if max_ball_rect < min_rect or min_ball_rect > max_rect:
                # Es gibt eine separierende Achse!
                return False, 0

        # Wenn keine separierende Achse gefunden wurde, gibt es eine Kollision
        min_overlap = (np.argmin(overlaps), np.min(overlaps))
        return True, normals[min_overlap[0]]
    
    def push(self, ball, is_aktiv):
        if is_aktiv and ball.position.x == 16:
            if self.position.y < 670:
                return False
            self.position -= Vector(0, 10)
            ball.velocity += Vector(0, -10)
            return False
        else:
            self.position = Vector(5,670)
            return False
            