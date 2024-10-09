import math
from datetime import date

class Parabola():
  """
  Parabola Concept
  ------

  This class is created with Parabolic properties used in graphing
  """
  def __init__(
      self, 
      x1: tuple[float] = (0, 0),
      x2: tuple[float] = (0, 0), 
      y: tuple[float] = (0, 0),
      symmetry: tuple[float] = (0, 0),
      vertex: tuple[float] = (0, 0)
    ):
    self.x_int1 = x1
    self.x_int2 = x2
    self.y_int = y
    self.symmetry = symmetry
    self.vertex = vertex


class Parabola_Motion(Parabola):
  """
  Physics - Projectile Motion Concept
  ------

  Contain list of formulas in Projectile Motion concept, as part
  of the Parabola Concept.
  Source: https://phys.libretexts.org/Bookshelves/University_Physics/Physics_(Boundless)/3%3A_Two-Dimensional_Kinematics/3.3%3A_Projectile_Motion
  """
  def __init__(
      self, 
      gravity: float = 0
    ):
    super().__init__()
    self.gravity: float = gravity
    self.accel_x: float = 0           # No acceleration in horizontal direction
    self.accel_y: float = -gravity    # Acceleration in vertical direction due to gravity
  
  def veloX_initial(self, velo: float, angle: float):
    """
    Define initial velocity in horizontal direction

    """
    return velo * math.cos(angle)

  def veloY_initial(self, velo: float, angle: float):
    """
    Define initial velocity in vertical direction
    
    """
    return velo * math.sin(angle)
  
  def flightTime(self, velo: float, angle: float):
    return (2 * velo * math.sin(angle)) / self.gravity 

