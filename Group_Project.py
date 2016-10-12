# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:58:38 2016

@author: lukaswolff
"""
import DataInput as di

class Group_Project():
    
    def __init__(self):
        self.stock_list = None
        self.digraph = None
        self.Dates = None
    
    def addStock_List(self):
        self.stock_list, self.Dates = di.dataPrep()
    
    def addDigraph(self):
        #how??
        self.digraph = self.stock_list.getCorrelationGraph()
    
    def main():
        #gp = Group_Project()
        #gp.addStock_List()
        #gp.addDigraph()
        #gp.stock_list.printTask1Summary()
        #gp.stock_list.printTask2Summary()
        #gp.digraph.printTask3Summary()


    
    
    
    
    
    
    
        
    
    
        
    