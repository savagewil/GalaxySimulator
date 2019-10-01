import Vector, pygame


class Mass:
    def __init__(self, **kwargs):
        if "mass" in kwargs:  # kg
            self.mass = kwargs["mass"]
        else:
            self.mass = 1.99 * (10 ** 30)

        if "velocity" in kwargs:  # m/s
            self.velocity = kwargs["velocity"]
        else:
            self.velocity = Vector.Vector(i=0, j=0)

        if "position" in kwargs:  # m/s
            self.position = kwargs["position"]
        else:
            self.position = Vector.Vector(i=0, j=0)

        if "radius" in kwargs:  # km
            self.radius = kwargs["radius"]
        else:
            self.radius = 1

        self.force =  Vector.Vector(i=0, j=0)
    def getGravitationalForce(self, mass):
        r = mass.position.subtract(self.position)
        if not r.getMagnitude() == 0:
            G = 6.67408e-11
            R = r.multiply(1/r.getMagnitude())
            return R.multiply(G * self.mass * mass.mass / (r.getMagnitude() ** 2))
        else:
            return Vector.Vector(i=0, j=0)

    def getGravitationalForceScalar(self, mass):
        r = mass.position.subtract(self.position)
        if not r.getMagnitude() == 0:
            G = 6.67408e-11
            return G * self.mass * mass.mass / (r.getMagnitude() ** 2)
        else:
            return 0

    def move(self, time):  # time in seconds
        # print time
        v = self.velocity.multiply(time)
        # print v
        self.position = self.position.add(v)

    def accelerate(self, masses, time):
        v = self.force.multiply(time / self.mass)
        self.velocity = self.velocity.add(v)
        #        netforce = reduce(lambda net, mass: net.add(self.getGravitationalForce(mass)), masses, Vector.Vector(i=0, j=0))


    def draw(self, zoom, screen, scale, screensize, maxMass):
        # type: (object, object, object, object, object) -> object
        # print ":)"
        if scale:


            # print "-----"
            # print self.radius
            # print zoom
            #
            # print int(float(self.radius) / zoom)
            #
            # print (screensize/2) * self.position.getI() / zoom + screensize/2
            # print screensize/2 * self.position.getJ() / zoom + screensize/2
            # print 255 * self.mass / 2e25

            pygame.draw.circle(screen,
                               [255 * self.mass / maxMass,
                                255 * self.mass / maxMass,
                                255 * self.mass / maxMass],
                               [int((screensize/2) * self.position.getI() / zoom) + screensize/2,
                                int(screensize/2 * self.position.getJ() / zoom) + screensize/2],
                               int(self.radius / zoom))
        else:
##            print self.position.getI(),self.position.getJ()
##            print ((screensize/2) * self.position.getI()) / zoom, (screensize/2) * (self.position.getJ() / zoom)
            pygame.draw.circle(screen,
                               [150, 150, 150],
                               [int(screensize/2 * self.position.getI() / zoom) + screensize/2, int(screensize/2 * self.position.getJ() / zoom) + screensize/2],
                               10)
    def combine(self, mass):
        m1 = self.mass
        m2 = mass.mass


        self.mass += mass.mass

        self.velocity = (self.velocity.multiply(m1).add(mass.velocity.multiply(m2)).multiply(1/self.mass))

        mass.mass = 0
        mass.velocity = Vector.Vector(i=0, j=0)



