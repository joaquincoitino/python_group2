# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 22:58:38 2016

@author: lukaswolff
"""
import DataInput as di
import Stock as st
import Correlations as c
import Stock_List as stl



class Group_Project():
    
    def __init__(self):
        self.stock_list = None
        self.graph = None
        self.Dates = None
    
    def addStock_List(self):
        self.stock_list, self.Dates = di.dataPrep()
    
    def addGraph(self):
        #how??
        self.graph = self.stock_list.getCorrelationGraph()
    
    
        

def main():
    gp = Group_Project()
    gp.addStock_List()
    print(gp.stock_list.getMinimumDailyReturns()[1])
    print(gp.stock_list.getMinimumDailyReturns()[0].getName())
    #print(gp.stock_list.getElem(100))
    #gp.addGraph()
    #print(gp.graph.rnumEdges())
    #gp.stock_list.printTask1Summary()
    #gp.stock_list.printTask2Summary()
    #gp.digraph.printTask3Summary()
    

if __name__ == "__main__":main()
    
   

    
    
        
    
    
        
    