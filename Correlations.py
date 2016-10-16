# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:45:12 2016
@author: lukaswolff
"""

import Stock as st
import numpy as np



def getCorrelation(stock1, stock2):
    """
    Returns the correlation for two given stocks using the formula
    given in the homework assignment
    Output: 
    """  
    x = stock1.getDailyReturnAll()
    y = stock2.getDailyReturnAll()
    n = len(x)
    
    xy = 0
    for i in range(0,len(x)):
        xy = xy + (x[i]*y[i])
    
    cor = (xy - (n*stock1.getMeanReturn()*stock2.getMeanReturn())) / (n*stock1.getStandardDeviation()*stock2.getStandardDeviation())
    return cor

def printCorrelation(stock1, stock2):
    """
    Prints out the companies full names of the two given stocks and
    the correlation between those two
    """
    print("Company 1: " +stock1.getName() + ", Company 2: " + stock2.getName()) 
    print("Correlation: " + str(getCorrelation(stock1,stock2)))
    #Round function to format corr
    #Format 
    
def getCorrelationList(stock, stock_list):
    """
    Returns for a given stock a list with the correlation to all other 
    stocks inside a list of tuples (stock name, correlation) and sorts the
    list according to the correlation (descending)
    """
    corlist = []
    for i in stock_list:
        if i.getName() == stock.getName():
            continue
        cortup = (i.getName(), getCorrelation(stock,i))
        corlist.append(cortup)
    
    corlist.sort(key=lambda x: x[1], reverse=True)           
    return corlist #correlation_list

def getLeastCorrelatedCompany(stock, stock_list):
    """
    Returns for a given stock the company with the least correlation and the
    correlation to this company
    """ 
    corlist = []    
    corlist = getCorrelationList(stock,stock_list)
    leastcor = corlist[len(corlist)-1]
    return leastcor

def printLeastCorrelatedCompany(stock, stock_list):
    """
    Prints out for a given stock the name of the company, the company it has
    the least correlation to and the name of the related company
    """
    print("Company 1: " + stock.getName() + ", Company 2: " + getLeastCorrelatedCompany(stock,stock_list)[0]) 
    print("Correlation: " + str(getLeastCorrelatedCompany(stock,stock_list)[1]))


def getHighestCorrelatedCompany(stock, stock_list):
    """
    Similar to LeastCorrelatedCompany
    """
    corlist = []    
    corlist = getCorrelationList(stock, stock_list)    
    highestcor = corlist[0]
    return highestcor

def printHighestCorrelatedCompany(stock, stock_list):
    """
    Similar to LeastCorrelatedCompany
    """
    print("Company 1: " + stock.getName() + ", Company 2: " + getHighestCorrelatedCompany(stock,stock_list)[0]) 
    print("Correlation: " + str(getHighestCorrelatedCompany(stock,stock_list)[1]))




