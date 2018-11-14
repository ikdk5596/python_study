v1 = Vector(2,4)
v2 = Vector(2,1)
v1 + v2

v = Vector(3,4)
abs(v)

v * 3

abs(v*3)


from math import hypot

class Vector:

  def _init(self, x=0, y=0 ):
    self.x = x
    self.y = y
    
  def _pepr_(self):
    return 'Vector(%r, %r)' % (self.x = x, self.y = y)
    
    
  def _abs_(self):
    return bool(abs(self))
    
    
  def _add_(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x,y)
    
  def _mul_(self, scalar):
    return Vector(self.x *scalar, self.y * scalar)
    
