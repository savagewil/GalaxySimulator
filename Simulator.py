import pygame
import random
import Calculations
import Mass
import Vector

screensize = 500

def draw(mass):
    mass.draw(zoom, screen, True, screensize, 2e25)
def remover(mass):

    return not mass.mass == 0

def combinerList(mass, masses):

    map(combiner, [mass] * len(masses), masses)
def getRandomMass(num):
    return num
def combiner(mass1, mass2):
    if (mass1.position.subtract(mass2.position)).getMagnitude() < (mass1.radius + mass2.radius) and not mass1 == mass2:
        # print 1
        mass1.combine(mass2)
Generations = 0
Radius = 1.702931e+21
Radius = 1.702931e+7
Time = 1.1 ** -3
# Time = 3.154e13
initialVelocity = 2e10

Radius /= 2

zoom = Radius * 4
# , position= Vector.Vector(i = )
pygame.init()
pygame.key.set_repeat(50, 10)
screen = pygame.display.set_mode([screensize, screensize])
# print random.randint(-Radius, Radius)
masses = []
# print Radius
# print zoom
for i in range(0, 100):
    # print i
    masses.append(Mass.Mass(mass=random.randint(2e24, 2e25), radius=random.randint(int(1e3), int(2.4e4)),
                            position=Vector.Vector(i= random.randint(-Radius, Radius),
                                                   j= random.randint(-Radius, Radius)),
                            velocity=Vector.Vector(i=0, j=0)))

done = False
running = False
mini = 10e20
while not done:
    Generations += 1
    print(Generations)
    if Generations == 100:
        done = True
    print(len(masses))
    # min 6.05369995797e+17
    mini = min(mini, Calculations.getMinimumDistance(masses))
    print(mini)
    # Calculations.recursiveCombiner(masses, 0)
        ##    map(combinerList, masses, [masses] * len(masses))
    # for mass in masses:
    #     print mass.mass
##    masses = filter(remover, masses )
    map(Mass.Mass.draw, masses, [zoom] * len(masses), [screen] * len(masses),
        [True] * len(masses), [screensize] * len(masses), [2e25] * len(masses))
    pygame.display.flip()
    # pygame.time.delay(20)
    screen.fill([0, 0, 0])
    if running:
        masses = Calculations.recursiveCombiner(masses, 10000)
        map(Calculations.clearForce, masses)
        Calculations.recursiveForceCalculator(masses)
        map(Mass.Mass.accelerate, masses, [masses] * len(masses), [Time] * len(masses))
##        print "Accel",masses[0].position.getI(), masses[0].position.getJ()
##        print "Accel",masses[0].position.getI(), masses[0].position.getJ()
        map(Mass.Mass.move, masses, [Time] * len(masses))
##        print "Accel",masses[0].position.getI(), masses[0].position.getJ()
##        print "move",masses[0].position.getI(), masses[0].position.getJ()
##        # print masses[0].velocity
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running
                print(running)
            elif event.key == pygame.K_UP:
                zoom /= 1.1
            elif event.key == pygame.K_DOWN:
                zoom *= 1.1
            elif event.key == pygame.K_LEFT:
                Time /= 2
            elif event.key == pygame.K_RIGHT:
                Time *= 2
            elif event.key == pygame.K_0:
                Generations = 0

pygame.quit()
