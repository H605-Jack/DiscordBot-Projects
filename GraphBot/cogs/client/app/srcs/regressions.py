"""
  regressions.py

  This file contains code of regression formulas to interact with the
  app command in regres.py
"""
import math
import matplotlib
import statistics

class Regression():
  def __init__(self, plotx: list[float], ploty: list[float]) -> None:
    self.plotx = plotx
    self.ploty = ploty
    self.n = len(self.plotx) if len(self.plotx) == len(self.ploty) else None
    # generative slope-intercept form 
    self.yint = 0
    self.slope = 0
    # fit calculations
    self.rscore = 0
    self.r2score = 0
    # residual
    self.resd = []

  def residual(self):
    """
    Calculate residual with slope-intercept form's format y=b0+b1x

    """
    if self.n is not None:
      for i in range(0, self.n):
        self.resd.append(round(self.ploty[i] - (self.yint + self.slope * self.plotx[i]), 10))

  def r_score(self):
    """
    Calculate the Correlation Coefficient and Coefficient of
    Determination

    Correlation Coefficient range -1 to 1, Coefficient of 
    Determination range 0 to 1
    """
    self.rscore = statistics.correlation(self.plotx, self.ploty) 
    self.r2score = math.pow(statistics.correlation(self.plotx, self.ploty), 2)

class RegressionLine(Regression):
  def __init__(self, plotx: list[float], ploty: list[float]) -> None:
    super().__init__(plotx, ploty)
    self.plotx = plotx
    self.ploty = ploty
    self.sum_x = 0
    self.sum_y = 0
    self.sum_xy = 0
    self.sum_x2 = 0
    self.sum_y2 = 0

  def autoform(self):
    """
    Automatically forming a Slope-intercept form based on sum of 
    x, y, xy, x^2, and y^2 statistical data.

    """
    if self.n is not None:
      self.sum_x = sum(self.plotx)
      self.sum_y = sum(self.ploty)
      # self.sum_xy = sum(self.plotx) * sum(self.ploty)
      # self.sum_x2 = math.pow(sum(self.plotx), 2)
      for i in range(0, self.n):
        self.sum_xy += self.plotx[i] * self.ploty[i]
        self.sum_x2 += math.pow(self.plotx[i], 2)
      
      self.yint = round(((self.sum_y)*(self.sum_x2) - (self.sum_x)*(self.sum_xy))/(self.n*(self.sum_x2) - math.pow((self.sum_x), 2)), 10)
      self.slope = round((self.n*(self.sum_xy) - (self.sum_x)*(self.sum_y))/(self.n*(self.sum_x2) - math.pow((self.sum_x), 2)), 10)

  def form(self, yint: float, slope: float):
    """
    Represents a User-defined Slope-intercept form.
    
    """
    self.yint = yint
    self.slope = slope

  # using matplotlib to output the graph
  def display(self):
    pass
