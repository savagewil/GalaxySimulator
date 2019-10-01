# import pygame
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import Calculations
# import Mass
# import Vector

screensize = 500

# def draw(mass):
#     mass.draw(zoom, screen, True, screensize, 2e25)
# def remover(mass):
#
#     return not mass.mass == 0
#
# def combinerList(mass, masses):
#
#     map(combiner, [mass] * len(masses), masses)
# def getRandomMass(num):
#     return num
# def combiner(mass1, mass2):
#     if (mass1.position.subtract(mass2.position)).getMagnitude() < (mass1.radius + mass2.radius) and not mass1 == mass2:
#         # print 1
#         mass1.combine(mass2)
#
# pygame.init()
# pygame.key.set_repeat(50, 10)
# screen = pygame.display.set_mode([screensize, screensize])

count = 100
generations = 0
radius = 1.702931e+21
radius = 1.702931e+7
G = 6.67408e-11
time_step = 200
time_step_2 = ((time_step) ** 2) / 2
display_rate = 10000
time_limit = 100000
# Time = 3.154e13
# initialVelocity = 2e10

radius /= 2

zoom = radius * 4

masses = (np.random.randn(100, 1) + 0.5) * (2e25 - 2e24) + 2e24
positions = np.random.randn(100, 2) * radius
velocities = np.zeros((100, 2))

epsilon = 0.0000000001


def get_diff(positions):
    p1 = np.reshape(positions, (count, 1, 2))
    p2 = np.reshape(positions, (1, count, 2))
    diff = p1 - p2
    return diff


def get_distance_squared(diff):
    squared = np.square(diff)
    return squared[:, :, 0] + squared[:, :, 1]


def gravity(masses, diff, distance_squared):
    # print(masses.shape)
    # print(np.transpose(masses).shape)
    # print(distance_squared.shape)
    # print("==================")
    force = np.divide(np.multiply(G, np.dot(masses, np.transpose(masses))), distance_squared + epsilon)
    # print(diff.shape)
    # print(distance_squared.shape)
    # print("==================")
    directions = np.divide(diff, np.reshape(distance_squared, (count, count, 1)) + epsilon)
    # print(directions.shape)
    # print(force.shape)
    # print(masses.shape)
    # print("==================")
    force_d = np.negative(np.multiply(directions, np.reshape(force, (count, count, 1))))
    mass = np.divide(1, masses)

    accelerations = np.zeros((100, 2))
    accelerations[:, :1] = np.dot(force_d[:, :, 0], mass)
    accelerations[:, 1:2] = np.dot(force_d[:, :, 1], mass)
    # print(accelerations.shape)
    return accelerations


def move(positions, velocities, accelerations, time_step, time_step_2):
    positions = np.add(np.add(positions, np.multiply(time_step, velocities)), np.multiply(time_step_2, accelerations))
    velocities = np.multiply(time_step, accelerations)
    return positions, velocities


# def draw(screen, positions):
#     screen_positions = (positions * screensize / 2 + screensize / 2).astype(int)
#     map(lambda position:pygame.draw.circle(screen,
#                        [150, 150, 150],
#                        position,
#                        10), screen_positions)


while generations < time_limit:
    diff = get_diff(positions)
    distance_squared = get_distance_squared(diff)
    accelerations = gravity(masses, diff, distance_squared)
    positions, velocities = move(positions, velocities, accelerations, time_step, time_step_2)
    # print(positions.shape)
    # print(positions[:, 1].shape)

    if generations % display_rate == 0:
        print(positions[0])
        fig = sns.scatterplot(x=positions[:, 0], y=positions[:, 1])
        plt.ylim(-radius, radius)
        plt.xlim(-radius, radius)
        plt.show()
    generations += 1
    # input()
print(generations)