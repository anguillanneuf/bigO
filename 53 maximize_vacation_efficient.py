# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:13:08 2017

@author: harrisot
"""
class Vacation:
  def __init__(self, flights, days):
    self.flights = flights
    self.days = days
    self.memo = [[0]*len(days)]*len(flights)
    
  def maximize_vacation(self, city, week):
    num_cities = len(self.flights)
    num_weeks = len(self.days)
    vac = 0
    
    if week == num_weeks: 
      return 0
    
    if self.memo[city][week] > 0: 
      return self.memo[city][week]
    
    for i in range(num_cities):
      if i == city or self.flights[city][i] == 1:
        vac = max(vac, self.days[week][i] + self.maximize_vacation(i, week+1))
        self.memo[city][week] = vac
    
    return self.memo[city][week]

flights = [[0,1,1],
           [1,0,1],
           [1,1,0]]

days1   = [[1,3,1],
           [6,0,3],
           [3,3,3]]

days2   = [[7,0,0],
           [0,7,0],
           [0,0,7]]

vac1 = Vacation(flights, days1)
vac2 = Vacation(flights, days2)
print(vac1.maximize_vacation(0,0)) # expected 12
print(vac1.memo)
print(vac2.maximize_vacation(0,0)) # expected 21