# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:27:07 2017

@author: harrisot
"""
class Vacation:
  def __init__(self, flights, days):
    self.flights = flights
    self.days = days
    self.itineraries = []

  def create_itinerary(self, k, prefix):
    if k == 0:
      self.itineraries.append(prefix)
    else:
      curr = int(prefix[-1]) if len(prefix) > 0 else 0
      
      for j in range(len(self.flights)):
        if curr == j:
          self.create_itinerary(k-1, prefix+[str(j)])
        elif self.flights[curr][j] == 1:
          self.create_itinerary(k-1, prefix+[str(j)])
  
  def maximize_vacation(self):

    nweeks = len(self.days)
    self.create_itinerary(nweeks, [])
    max_vac = 0
    
    for itinerary in self.itineraries:
      curr_vac = 0
      for i,v in enumerate(list(itinerary)):
        curr_vac += self.days[i][int(v)]
      if curr_vac > max_vac:
        max_vac = curr_vac
    return max_vac

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
print(vac1.maximize_vacation()) # expected 12
print(vac2.maximize_vacation()) # expected 21