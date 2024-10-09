import math
import matplotlib
import statistics

class Regression():
  def __init__(self, *plots: list[float]) -> None:
    self.plots = plots
    # generative slope-intercept form 
    self.yint = 0
    self.slope = 0
    # fit calculations
    self.rscore = 0
    self.r2score = 0

  def r_score(self, value = 0):
    if value == 0:
      for i in self.plots:
        self.rscore = statistics.correlation(i[0], i[1])
    else: self.rscore = value

  def r2_score(self):
    self.r2score = math.pow(self.rscore, 2)


class RegressionLine(Regression):
  def __init__(self, *plots: list[float]) -> None:
    super().__init__(plots)
    for i in self.plots:
      self.value_x = i[0]
      self.value_y = i[1]
      self.value_xy = i[0] * i[1]
      self.value_x2 = math.pow(i[0], 2)
      self.value_y2 = math.pow(i[1], 2)

  def autoform(self):
    n = len(self.plots)
    self.yint = ((self.value_y)*(self.value_x2) - (self.value_x)*(self.value_xy))/(n*(self.value_x2) - math.pow((self.value_x), 2))
    self.slope = (n*(self.value_xy) - (self.value_x)*(self.value_y))/(n*(self.value_x2) - math.pow((self.value_x), 2))

  def form(self, yint: float, slope: float):
    self.yint = yint
    self.slope = slope

  # using matplotlib to output the graph
  def display(self):
    pass