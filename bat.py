import pygame
import random   
from vector import Vector
from copy import copy

class Bat:
    def __init__(self, screen, color, points, angle=0, direction=1, count=0, active=1, right=False):

        '''
        Constructor method for initializing the Bat object.

        Parameters:
            screen (pygame.Surface): The surface on which the bat will be drawn.
            color (tuple): The color of the bat.
            points (list of Vector): The corner points of the bat.
            angle (int): rotation angle of the bat (default is 0).
            direction (int): rotation direction of the bat (default is 1).
            count (int): Counter to track rotations (default is 0).
            active (int): indicate whether the bat is active (default is 1).
            right (bool):indicate if the bat rotates clockwise (default is False).
        '''

        # Initialize instance variables
        self.screen = screen
        self.color = color
        self.points_vec = points
        self.points_tuple = [_.int_tuple() for _ in points]  # Convert vectors to tuples for drawing
        self.width = points[1] - points[0]
        self.height = points[3] - points[0]
        self.center = (self.points_vec[0] - self.points_vec[2]) / 2 + self.points_vec[2]  # Compute the center of the bat
        self.angle = angle
        self.direction = direction
        self.count = count
        self.active = active
        
        # Determine rotation direction
        if right:
            self.right = -1
        else:
            self.right = 1

    def update(self):
        '''
        Update method to redraw the bat on the screen after rotation.
        '''
        pygame.draw.polygon(self.screen, self.color, self.flip())

    def flip(self):
        '''
        Method to rotate the bat and return the rotated points.

        Returns:
            rotated_points_tuple (list of tuples): Rotated corner points of the bat.
        '''

        # Change rotation direction at specific angles
        if self.angle == -50 * self.right or self.angle == 20 * self.right:
            self.direction *= -1
            if self.angle == 20 * self.right:
                self.count += 1

        # Update the rotation angle
        self.angle -= 2 * self.direction * self.active

        # Rotate the corner points of the bat
        rotated_points_vec = []
        rotated_points_tuple = []

        pivot_point = self.points_vec[0]
        for point in self.points_vec:
            point = point - pivot_point 
            point = point.rotate(self.angle) + pivot_point
            rotated_points_tuple.append(point.int_tuple())
            rotated_points_vec.append(point)
  
        # Update activity based on count
        if self.count >= 1:
            self.active = 0
        if self.count < 1:
            self.active = 1
        
        # Update instance variables
        self.points_tuple = rotated_points_tuple
        self.center = (Vector(self.points_tuple[0][0], self.points_tuple[0][1]) - Vector(self.points_tuple[2][0], self.points_tuple[2][1]))/2 + Vector(self.points_tuple[2][0], self.points_tuple[2][1])
        
        return rotated_points_tuple
