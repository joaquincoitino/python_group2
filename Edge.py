# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:54:02 2016

@author: lukaswolff
"""

class Edge():
    
    
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight
    
    def getSource(self):
        return self.source
          
    def getDestination(self):
        return self.dest
    
    def getWeight(self):
        return self.weight
          
    def __str__(self):
        return str(self.source)+'->'+str(self.dest)