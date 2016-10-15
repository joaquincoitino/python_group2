# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:28:02 2016

@author: lukaswolff
"""
import csv
import numpy as np
import Stock as st
import Correlations as c
import Stock_List as stl





def readCSVIntoList(name):
    """
    Reads in a csv file and returns the rows as a list. This method is used
    for the function PriceListToMatrix and in dataPrep for the csv file with 
    the sectors and names
    Input: name of the csv file
    Output: List where every line of the csv file is stored in an element
    of the list returned
    
    """
    L = []
    with open(name, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            L.append(row)
    return L

    
def priceListToMatrix(L):
    """
    Transforms a list of rows into a matrix to simplify operations on columns
    Input: List with all rows of the csv file
    Output: numpy matrix with all price entries of the csv file, 
    header containing the symbols of the companies and list with all dates
    """ 
    first_row = L[0]
    header = first_row[1:]
    trade_dates = []    
    
    
    #Creates a matrix of the size of the csv file with 0s in each cell
    num_col = len(header)
    num_row = len(L)-1
    price_matrix = np.zeros((num_row, num_col))
    
    #Fills the matrix with the stock price movements
    for i in range (len(L)-1):
        row = L[i+1]
        #Strips off the dates row and stores it in a separate list
        price_matrix[i,] = row[1:]
        trade_dates.append(row[0])
    
    return price_matrix, header, trade_dates 


def priceMatrixToStockClasses(pm, header, sectors, names):
    """
    Transforms our price matrix into a list of stocks
    Input: Price matrix, header with the symbols of the companies, a list with
    all the names of the companies and the sectors of each company
    Output: List of stocks (stock class) 
    """
    Stock_List = []
    
    for i in range(len(header)):
        name = names[i]
        price_movement = pm[:,i]
        sector = sectors[i]
        symbol = header[i]
        newStock = st.Stock(name, price_movement, sector, symbol)
        Stock_List.append(newStock)
    return Stock_List
    

def dataPrep():
    """
    Wrap up function calling all the functions defined in this file
    """
    price_sheet = readCSVIntoList('SP_500_close_2015.csv')
    price_matrix, header, trade_dates = priceListToMatrix(price_sheet)
    
    name_sheet = readCSVIntoList('SP_500_firms.csv') 
    names = []
    sectors = []
    
    for i in range(1, len(name_sheet)):
        row = name_sheet[i]
        names.append(row[1])
        sectors.append(row[2])
    stock_list = priceMatrixToStockClasses(price_matrix, header, sectors, names)
    stock_list_obj = stl.Stock_List(stock_list)
    return stock_list_obj, trade_dates
    


#print(len(stocks))
#for i in range (len(stocks)):
#    print(stocks[i].getName())
#print(Stock_List[3].getPrice_List())
#print(findStock('YHOO').getName())
#print(Stock_List[0].getSymbol())

#print(c.getCorrelation(stocks[5], stocks[80]))



