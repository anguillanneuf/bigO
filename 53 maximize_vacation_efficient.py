# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:13:08 2017

@author: harrisot
"""
class Vacation:
  def __init__(self, flights, days):
    self.flights = flights
    self.days = days
    self.memo = [[0 for _ in range(len(days))] for _ in range(len(flights))]
    
  def maximize_vacation(self, city, week):
    """O(k*n) time
    O(k*n) space
    """
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
  
  def maximize_vacation_iterative(self):
    """O(k*n*n) time 
    O(n) space"""
    
    max_by_city = [0 for _ in range(len(flights))]
    
    for k in range(len(self.days)):
      temp_max = [0 for _ in range(len(flights))]
      for i in range(len(self.flights)):
        temp = 0
        for j in range(len(self.flights)):
          if i==j or self.flights[i][j] == 1:
            temp = max(temp, max_by_city[j]+self.days[k][i])
        temp_max[i] = temp
      max_by_city = temp_max
      
    return max(max_by_city)
  
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
print(vac1.maximize_vacation_iterative())

print(vac2.maximize_vacation(0,0)) # expected 21
print(vac2.maximize_vacation_iterative())