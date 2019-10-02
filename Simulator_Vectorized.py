import pygame
import random
import numpy as np

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# import Calculations
# import Mass
# import Vector

screensize = 800

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
pygame.init()
pygame.key.set_repeat(50, 10)
screen = pygame.display.set_mode([screensize, screensize])
zoom = 1
count = 1000
generations = 0
radius = 1.702931e+21
# radius = 1.702931e+7
limit = radius * zoom
G = -6.67408e-11
time_step = 10e18
time_step_2 = ((time_step) ** 2) / 2
display_rate = 10
time_limit = 10000000000
# Time = 3.154e13
initialVelocity = 500*2

radius /= 2

# zoom = radius * 4

masses = (np.random.rand(count, 1)) * (2e25 - 2e24) + 2e24
positions = (np.random.rand(count, 2) - .5) * 2 * radius
velocities = 0 * (np.random.rand(count, 2) - .05) * initialVelocity

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
    directions = np.divide(diff, np.reshape(np.sqrt(distance_squared), (count, count, 1)) + epsilon)
    # print("DIFF", diff)
    # print("distance_squared", distance_squared)
    # print("directions", directions)
    # print("dis", np.square(directions)[:,:,0] + np.square(directions)[:,:,1])
    # print(directions.shape)
    # print(force.shape)
    # print("masses",masses)
    # print("==================")
    # print("force", force)
    # print("force_reshape", np.reshape(force, (count, count, 1)))
    # print("dir", directions)
    force_d = np.multiply(directions, np.reshape(force, (count, count, 1)))
    # print("f_d", force_d)
    # force_d = np.multiply(np.ones((count, count)) - np.eye(count), force_d)
    # print("f_d_middle", force_d)
    mass = np.divide(1, masses)

    accelerations = np.zeros((count, 2))
    accelerations[:, :1] = np.dot(force_d[:, :, 0], mass)
    # print("accelerations_1", accelerations)
    accelerations[:, 1:2] = np.dot(force_d[:, :, 1], mass)
    # print("accelerations_2", accelerations)
    # print(accelerations.shape)
    return accelerations, directions


def move(positions, velocities, accelerations, time_step, time_step_2):
    positions = np.mod(np.add(np.add(positions, np.multiply(time_step, velocities)), np.multiply(time_step_2, accelerations)) + limit/2, limit) - limit/2
    velocities = np.add(velocities,np.multiply(time_step, accelerations))
    return positions, velocities


def draw(screen, positions, directions):
    screen_positions = ((positions) * screensize / (radius * 2 * zoom) + screensize/2).astype(int)
    screen_dir = ((positions) * screensize / (radius * 2 * zoom) + directions * 20 + screensize/2).astype(int)
    # print(screen_positions[0])
    for i in range(len(screen_positions)):
        pygame.draw.circle(screen, [150, 150, 150], screen_positions[i], 2)
        # print(screen_dir[i])
        # for j in range(len(screen_positions)):
        #     pygame.draw.circle(screen, [200, 0, 0], screen_dir[i, j], 2)

acceleration_on = True

while generations < time_limit:
    diff = get_diff(positions)
    distance_squared = get_distance_squared(diff)
    accelerations, directions = gravity(masses, diff, distance_squared)
    accelerations = accelerations * acceleration_on
    positions, velocities = move(positions, velocities, accelerations, time_step, time_step_2)
    # print(positions.shape)
    # print(positions[:, 1].shape)

    if generations % display_rate == 0:
        print("Render")
        # print(accelerations[0])
        # print(accelerations[1])
        screen.fill([0, 0, 0])
        draw(screen, positions, directions)
        pygame.display.update()
        # pygame.time.delay(10)
        # input()
        # print(positions[0])
        # fig = sns.scatterplot(x=positions[:, 0], y=positions[:, 1])
        # plt.ylim(-radius, radius)
        # plt.xlim(-radius, radius)
        # plt.show()
    generations += 1
    events = pygame.event.get()
    # input()
print(generations)
