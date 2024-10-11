import math
import matplotlib
import numpy as np
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
    # residual
    self.resd = 0

  def residual(self, refplot: list[float]):
    # calculate residual, with slope-intercept form's format is y=b0+b1x
    self.resd = refplot[1] - (self.yint + self.slope * refplot[0])

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
    self.plots = plots
    self.sum_x = 0
    self.sum_y = 0
    self.sum_xy = 0
    self.sum_x2 = 0
    self.sum_y2 = 0

  def autoform(self):
    """
    Automatically forming a Slope-intercept form based on sum of x, y, xy, x^2, and y^2 
    statistical data.

    """
    n = len(self.plots)
    for i in self.plots:
      self.sum_x += i[0]
      self.sum_y += i[1]
      self.sum_xy += i[0] * i[1]
      self.sum_x2 += math.pow(i[0], 2)
      self.sum_y2 += math.pow(i[1], 2)
    
    self.yint = round(((self.sum_y)*(self.sum_x2) - (self.sum_x)*(self.sum_xy))/(n*(self.sum_x2) - math.pow((self.sum_x), 2)), 2)
    self.slope = round((n*(self.sum_xy) - (self.sum_x)*(self.sum_y))/(n*(self.sum_x2) - math.pow((self.sum_x), 2)), 4)

  def form(self, yint: float, slope: float):
    """
    Represents a User-defined Slope-intercept form.
    
    """
    self.yint = yint
    self.slope = slope

  # using matplotlib to output the graph
  def display(self):
    pass
