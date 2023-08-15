#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 01:31:38 2022

@author: muntazirabidi
"""

import threading, queue
from PIL import Image
import numpy as np
import random

#size of the problem
size = 50

#grid initialization
grid = np.zeros((size,size),dtype=np.uint8)

#start at the center
initpos = (size/2,size/2)

#create the propagation queue
qu = queue.Queue()

#queue the starting point
qu.put((initpos,initpos))

#the starting point is queued
grid[initpos] = 1


#get the neighbouring grid cells from a position
def get_neighbours(pos):
  n1 = (pos[0]+1,pos[1]  )
  n2 = (pos[0]  ,pos[1]+1)
  n3 = (pos[0]-1,pos[1]  )
  n4 = (pos[0]  ,pos[1]-1)
  return [neigh for neigh in [n1,n2,n3,n4] 
                  if neigh[0] > -1 and \
                     neigh[0]<size and \
                     neigh[1] > -1 and \
                     neigh[1]<size \
         ]


while(not qu.empty()):
  #pop a new element from the queue
  #pos is its position in the grid
  #parent is the position of the cell which propagated this one
  (pos,parent) = qu.get()

  #get the neighbouring cells
  neighbours = get_neighbours(pos)

  #legend for grid values
  #0 -> nothing
  #1 -> stacked
  #2 -> black
  #3 -> white

  #if any neighbouring cell is black, we could join two branches
  has_black = False
  for neigh in neighbours:
    if neigh != parent and grid[neigh] == 2:
      has_black = True
      break

  if has_black:
    #blackening this cell means joining branches, abort
    grid[pos] = 3
  else:
    #this cell does not join branches, blacken it
    grid[pos] = 2

    #select all valid neighbours for propagation
    propag_candidates = [n for n in neighbours if n != parent and grid[n] == 0]
    #shuffle to avoid deterministic patterns
    random.shuffle(propag_candidates)
    #propagate the first two neighbours
    for neigh in propag_candidates[:2]:
      #queue the neighbour
      qu.put((neigh,pos))
      #mark it as queued
      grid[neigh] = 1

#render image
np.putmask(grid,grid!=2,255)
np.putmask(grid,grid<255,0)
im = Image.fromarray(grid)
im.save('data.png')