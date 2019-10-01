import Vector

def Combiner(mass1, mass2, diff):
    # print (mass1.position.subtract(mass2.position)).getMagnitude()
    if (mass1.position.subtract(mass2.position)).getMagnitude() < diff:
        mass1.combine(mass2)


def recursiveCombiner(masses, diff):
    if len(masses) > 1:
        map(Combiner, [masses[0]] * (len(masses ) - 1), masses[1:len(masses)], [diff] * (len(masses) - 1))

        return [masses[0]] + recursiveCombiner(filter(massNotZero, masses[1:len(masses)]), diff)
    else:
        return masses


def massNotZero(mass):
    return mass.mass != 0

def getDistance(mini, masses):
    return min((masses[0].position.subtract(masses[1].position)).getMagnitude(), mini)


def getMinimumDistance(masses):
    if len(masses) > 1:
        mini = reduce(getDistance, map(lambda m1, m2: [m1, m2], [masses[0]] * (len(masses) - 1), masses[1:len(masses)]), 10e20)
        return min(mini, getMinimumDistance(masses[1:len(masses)]) )
    else:
        return 10e20



def forceCalculator(mass1, mass2):
    # print (mass1.position.subtract(mass2.position)).getMagnitude
    if mass1.position.subtract(mass2.position).getMagnitude() > 0:
        mass1.force = mass1.force.add(mass1.getGravitationalForce(mass2))
        mass2.force = mass2.force.add(mass2.getGravitationalForce(mass1))


def recursiveForceCalculator(masses):
    if len(masses) > 1:
        map(forceCalculator, [masses[0]] * (len(masses) - 1), masses[1:len(masses)])
        recursiveForceCalculator(masses[1:len(masses)])

def clearForce(mass):
    mass.force = Vector.Vector(i=0, j=0)