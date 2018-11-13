from math import hypot



v1 = Vector(2,4)
v2 = Vector(2,1)
print(v1 + v2)

v = Vector(3,4)
print(abs(v))

print(v * 3)
print(abs(v * 3))

class Vector:

    def _init_(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def _repr_(self):
        return 'Vector(%r,%r)' % (self.x, slef.y)

    def _abs_(self) :
        return hypot(self.x, self.y)

    def _bool_(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def _mul_(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    
