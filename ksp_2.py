#!/usr/bin/python
from openopt import *
from numpy import sin, cos

#N = 150

#items = [
#         {
#             'name': 'item %d' % i, # pay attention that Python indexation starts from zero
#             'cost': 1.5*(cos(i)+1)**2, 
#             'volume': 2*sin(i) + 3, 
#             'mass': 4*cos(i)+5,
#             'n':  1 if i < N/3 else 2 if i < 2*N/3 else 3 # number of elements
#         } 
#         for i in range(N) # i = 0, ... , N-1
#         ]
         
N = 4

items = [
         {
             'name': 'VM %d' % 1, # pay attention that Python indexation starts from zero
             'cpu': 35, 
             'mem': 16, 
             'net': 2,
             'n':  1
         }, 
         {
             'name': 'VM %d' % 2, # pay attention that Python indexation starts from zero
             'cpu': 12, 
             'mem': 7, 
             'net': 13,
             'n':  1
         }, 
         {
             'name': 'VM %d' % 3, # pay attention that Python indexation starts from zero
             'cpu': 40, 
             'mem': 60, 
             'net': 10,
             'n':  1
         }, 
         {
             'name': 'VM %d' % 4, # pay attention that Python indexation starts from zero
             'cpu': 27, 
             'mem': 40, 
             'net': 70,
             'n':  1
         } 
#         for i in range(N) # i = 0, ... , N-1
         ]

constraints = lambda values: (
                              values['cpu'] < 100, 
                              values['mem'] < 100,
                              values['net'] < 100,
                              values['nItems'] <= 10, 
#                              values['nItems'] >= 5
                              # we could use lambda-func, e,g.
                              # values['mass'] + 4*values['volume'] < 100
                              )
objective = 'cpu'
# we could use lambda-func, e.g. 
# objective = lambda val: 5*value['cost'] - 2*value['volume'] - 5*value['mass'] + 3*val['nItems']
p = KSP(objective, items, goal = 'max', constraints = constraints) 
r = p.solve('glpk', iprint = 0) # requires cvxopt and glpk installed, see http://openopt.org/KSP for other solvers
print(r.xf) # {'item 131': 2, 'item 18': 1, 'item 62': 2, 'item 87': 1, 'item 43': 1}
# pay attention that Python indexation starts from zero: item 0, item 1 ...
# if fields 'name' are absent in items, you'll have list of numbers instead of Python dict
