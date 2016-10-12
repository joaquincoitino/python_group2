# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:41:58 2016

@author: lukaswolff
"""
import Edge 

class Digraph():
    
    def __init__(self):
        
        self.edges = {}
        self.numEdges = 0
    
    def addEdge(self, src, dest, weight):
        Digraph.addEdge(self, src, dest)
        Digraph.addEdge(self, src, dest)
        self.numEdges += 1
    
    def sortEdges():
        #TO BE DONE        
        
    def clusteringAlgorithm(self, k):
        #TO BE DONE
        CorrGraph = Digraph()
        for i in range(k-1):
            c_src = self.edges[i].getSource()
            c_dest = self.edges[i].getDest()
            c_weight = self.edges[i].getWeight()
            Corrgraph().addEdge(c_src, c_dest, c_weight)
        
    
    
        
        
    