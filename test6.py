
import time

class GMassSpringSystem( object ):

    def __init__( self, m=10, k=5, b=0 ):

        self.m_mass = m
        self.m_k = k
        self.m_damping = b
        
        self.m_force = 0

        self.x = 0
        self.dx = 5

    def setForce( self, force=0 ):
        self.m_force = force

    def getMass( self ):
        return self.m_mass

    def getSpringConstant( self ):
        return self.m_k

    def getDamping( self ):
        return self.m_damping

    def motionModel( self, dt ):
        a11 = 0
        a12 = 1
        a21 = -( self.m_k / self.m_mass )
        a22 = -( self.m_damping / self.m_mass )
        f = self.m_force

        self.x  += ( a11 * self.x + a12 * self.dx + 0 ) * dt
        self.dx += ( a21 * self.x + a22 * self.dx + f ) * dt


system1 = GMassSpringSystem()

print 'system1.mass: ' , system1.getMass()

system1.setForce()

T = 50
DT = 0.001
N = int( T / DT )

for i in range( N ):
    system1.motionModel( DT )
    time.sleep( DT )
    print 'x: ', system1.x
    print 'dx: ', system1.dx
