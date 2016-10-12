# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:06:03 2016

@author: lukaswolff


TASK
Stock returns. Calculate the daily returns for all stocks in the data. Discuss the returns over
the year: what companies experienced the maximum and minimum daily returns - can you
find the reasons for these? Which companies performed overall best and worst over the year?
Which companies exhibited most and least volatility, as measured by the standard deviation
of their returns over the year?
"""

import Stock as st
    
    
def getMinimumDailyReturns(stock_list):
    """
    Returns the lowest daily return for the observed period and the company
    associated to it
    """
    return None
    
    
def getMaximumDailyReturns(stock_list):
    """
    Returns the highest daily return for the observed period and the company
    associated to it
    """
    return None
    
    
def getBestPerformingCompany(stock_list):
    """
    WHAT COULD BE A MEASURE OF GOOD PERFORMANCE? (maybe geometric mean?)
    """
    return None
    
    
def getWorstPerformingCompany(stock_list):
    """
    same question as above
    """
    return None        
    
    
def getCompanyWithLeastVolatility(stock_list):
    """
    Returns the lowest standard deviation of returns
    for all observed companies and the company associated to it
    """
    return None
    
    
def getCompanyWithHighestVolatility(stock_list):
    """
    Returns the highest standard deviation of returns
    for all observed companies and the company associated to it
    """
    return None
    
    
def printSummary(stock_list):
    """
    This function wraps up all functions in this module and creates a summary
    of the dataset. 
    """
    #Maybe also include graphics?
    print('')