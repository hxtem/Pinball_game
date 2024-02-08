import math 
import numpy as np
import pygame

class Vector:
    """
    Eine Klasse, die einen Vektor in 2 Dimensionen repräsentiert.

    Attribute:
        x : float oder int
        y : float oder int

    Methoden:
        __init__(self, x, y)
        __str__(self)
        __add__(self, other)
        __sub__(self, other)
        __mul__(self, other)
        __truediv__(self, scalar)
        abs(self)
        rotate(self, angle)
        int_tuple(self)
        angle(self)
        cross(self, other)
        dot(self, other)
        length(self)
        normalize(self)
    """

    def __init__(self, x, y):
        """
        Initialisiere eine neue Instanz eines Vektors
        """
        self.x = x  # Setze die x-Komponente des Vektors
        self.y = y  # Setze die y-Komponente des Vektors

    def __str__(self):
        """
        Gibt eine Zeichenfolge für den Vektor als "Vector(x,y,z)" zurück
        """
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        """
        Überlade den + Operator für die Vector-Klasse
        Implementiert die Addition von zwei Instanzen der Vector-Klasse
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Überlade den - Operator für die Vector-Klasse
        Implementiert die Subtraktion von zwei Instanzen der Vector-Klasse
        """
        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other, self.y - other)

    def __mul__(self, other):
        """ 
        Überlade den * Operator für die Vector-Klasse
            - Multiplikation von zwei Instanzen der Vector-Klasse:
              Gibt ein float/int zurück, das das Skalarprodukt darstellt
            - Multiplikation eines Vektor-Objekts und eines Skalars (float oder int):
              Gibt einen Vektor zurück, dessen Komponenten mit dem Wert multipliziert sind
        """
        if isinstance(other, Vector):
            return self.mul_vector(other)
        if isinstance(other, float):
            return self.mul_scalar(other)
        if isinstance(other, int):
            return self.mul_scalar(other)

    def mul_vector(self, other):
        """
        Multipliziert zwei Vektoren und gibt das Skalarprodukt zurück
        """
        return float(self.x * other.x + self.y * other.y)

    def mul_scalar(self, other):
        """
        Multipliziert einen Vektor mit einem Skalar und gibt einen neuen Vektor zurück
        """
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, scalar):
        """
        Überlade den / Operator für die Vector-Klasse
        Führt eine Skalardivision durch
        """
        return Vector(self.x / scalar, self.y / scalar)

    def abs(self):
        """
        Gibt den Betrag des Vektor-Objekts zurück
        """
        return float(np.sqrt((self.x * self.x + self.y * self.y)))

    def rotate(self, angle):
        """
        Dreht den Vektor um einen gegebenen Winkel im Bogenmaß
        """
        angle_radians = math.radians(angle)
        new_x = self.x * math.cos(angle_radians) - self.y * math.sin(angle_radians)
        new_y = self.x * math.sin(angle_radians) + self.y * math.cos(angle_radians)
        return Vector(new_x, new_y)

    def int_tuple(self):
        """
        Gibt die Vektor-Komponenten als Ganzzahlen zurück
        """
        return (int(self.x), int(self.y))

    def angle(self):
        """
        Berechnet den Winkel des Vektors im Bogenmaß
        """
        if self.x == 0 or self.y == 0:
            return 0
        else:
            no = -360 / 2 / math.pi * math.atan2(self.y, self.x)
            return no

    def cross(self, other):
        """
        Berechnet das Kreuzprodukt von zwei Vektoren
        """
        return self.x * other.y - self.y * other.x

    def dot(self, other):
        """
        Berechnet das Skalarprodukt von zwei Vektoren
        """
        return self.x * other.x + self.y * other.y

    def length(self):
        """
        Berechnet die Länge des Vektors
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        """
        Normalisiert den Vektor
        """
        length = self.abs()
        if length != 0:
            self.x /= length
            self.y /= length
        return Vector(self.x, self.y)
    