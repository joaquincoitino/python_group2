# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:27:06 2016

@author: lukaswolff
"""


import Stock as st
import Graph as g

class Stock_List():
    
    def __init__(self, stock_list):
        self.stock_list = stock_list
        self.corr_tuples = []
    
    def findStock(self, symbol):
        for i in range(len(self.stock_list)):
            if self.stock_list[i].getSymbol()==symbol:
                return self.stock_list[i]
        #if stock is not in Stock_List (probably wrong spelled?)
        return None
        
    def getElem(self, position):
        if position >=0 and position < len(self.stock_list):
            return self.stock_list[position]
    


###############################################################################
###                       FUNCTIONS FOR TASK 1                              ###
###############################################################################

    def getDailyReturnsForAllStocks(self):
        """
        Calculates the daily returns for all stocks 
        Input: List with all stocks 
        Output: List with a list of all daily returns for each stock 
        """
    
        dailyreturnforall=[]
        for i in range(len(self.stock_list)):
            dailyreturnforall.append(self.stock_list[i].getDailyReturnAll())
        return dailyreturnforall    
        
    def getMinimumDailyReturns(self):
        """
        Returns the lowest daily return for the observed period and the company
        associated to it
        """
        dailyreturnforall = self.getDailyReturnsForAllStocks()
        minforeachcompany=[]
        for i in range(len(dailyreturnforall)):
            minforeachcompany.append(min(dailyreturnforall[i]))
        min_dailyreturn = min(minforeachcompany)
        min_dailyreturn_index  = minforeachcompany.index(min_dailyreturn)
        min_dailyreturn_com = self.stock_list[min_dailyreturn_index]
        return (min_dailyreturn_com, min_dailyreturn )
    
    def getMaximumDailyReturns(self):
        """
        Returns the highest daily return for the observed period and the company
        associated to it
        """
        maxforeachcompany=[]
        dailyreturnforall = self.getDailyReturnsForAllStocks()
        for i in range(len(dailyreturnforall)):
            maxforeachcompany.append(max(dailyreturnforall[i]))
        max_dailyreturn = max(maxforeachcompany)
        max_dailyreturn_index  = maxforeachcompany.index(max_dailyreturn)
        max_dailyreturn_com = self.stock_list[max_dailyreturn_index]
        return (max_dailyreturn_com, max_dailyreturn )
        
        
    def getBestPerformingCompany(self):
        """
        WHAT COULD BE A MEASURE OF GOOD PERFORMANCE? (maybe geometric mean?)
        """
        return None
        
        
    def getWorstPerformingCompany(self):
        """
        same question as above
        """
        return None 
    
    def getCompanyWithLeastVolatility(self):
        """
        Returns the lowest standard deviation of returns
        for all observed companies and the company associated to it
        """
        allsd=[]
        for i in range(len(self.stock_list)):
            allsd.append(self.stock_list[i].getStandardDeviation())
        minsd=min(allsd)
        minsd_index = allsd.index(minsd)
        minsd_name = self.stock_list[minsd_index]
        return (minsd_name, minsd)
        
        
    def getCompanyWithHighestVolatility(self):
        """
        Returns the highest standard deviation of returns
        for all observed companies and the company associated to it
        """
        allsd=[]
        for i in range(len(self.stock_list)):
            allsd.append(self.stock_list[i].getStandardDeviation())    
        maxsd = max(allsd)
        maxsd_index = allsd.index(maxsd)
        maxsd_name = self.stock_list[maxsd_index]
        return (maxsd_name, maxsd)    
        
        
    def printTask1Summary(self):
        """
        This function wraps up all functions in this module and creates a summary
        of the dataset. 
        """
        #Maybe also include graphics?
        Min_daily_return = self.getMinimumDailyReturns()[1]
        Max_daily_return = self.getMaximumDailyReturns()[1]
        Min_return_coname = self.getMinimumDailyReturns()[0].getName()
        Max_return_coname = self.getMaximumDailyReturns()[0].getName()
        Low_v = self.getCompanyWithLeastVolatility()[1]
        High_v = self.getCompanyWithHighestVolatility()[1]
        Low_v_coname = self.getCompanyWithLeastVolatility()[0].getName()
        High_v_coname = self.getCompanyWithHighestVolatility()[0].getName()
        print('The lowest daily return for the observed period is', Min_daily_return ,' and the company associated to it is', Min_return_coname)
        print('The highest daily return for the observed period is', Max_daily_return ,' and the company associated to it is', Max_return_coname)    
        print('The company with least volatility is', Low_v_coname ,' and its standard deviation in price is', Low_v)
        print('The company with highest volatility is', High_v_coname ,'and its standard deviation in price is', High_v)    
        
    
###############################################################################
###                       FUNCTIONS FOR TASK 2                              ###
###############################################################################
    
    
    def getCorrelation(self, stock1, stock2):
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
        
    def printCorrelation(self, stock1, stock2):
        """
        Prints out the companies full names of the two given stocks and
        the correlation between those two
        """
        print("Company 1: " +stock1.getName() + ", Company 2: " + stock2.getName()) 
        print("Correlation: " + str(self.getCorrelation(stock1,stock2)))
        #Round function to format corr
        #Format 
        
    def getCorrelationList(self, stock):
        """
        Returns for a given stock a list with the correlation to all other 
        stocks inside a list of tuples (stock name, correlation) and sorts the
        list according to the correlation (descending)
        """
        corlist = []
        for i in self.stock_list:
            if i.getName() == stock.getName():
                continue
            cortup = (i.getName(), self.getCorrelation(stock,i))
            corlist.append(cortup)
        
        corlist.sort(key=lambda x: x[1], reverse=True)           
        return corlist #correlation_list
    
    def getLeastCorrelatedCompany(self,stock):
        """
        Returns for a given stock the company with the least correlation and the
        correlation to this company
        """ 
        corlist = []    
        corlist = self.getCorrelationList(stock)
        leastcor = corlist[len(corlist)-1]
        return leastcor
    
    def printLeastCorrelatedCompany(self, stock):
        """
        Prints out for a given stock the name of the company, the company it has
        the least correlation to and the name of the related company
        """
        print("Company 1: " + stock.getName() + ", Company 2: " + self.getLeastCorrelatedCompany(stock)[0])
        print("Correlation: " + str(self.getLeastCorrelatedCompany(stock)[1]))
    
    
    def getHighestCorrelatedCompany(self, stock):
        """
        Similar to LeastCorrelatedCompany
        """
        corlist = []    
        corlist = self.getCorrelationList(stock)    
        highestcor = corlist[0]
        return highestcor
    
    def printHighestCorrelatedCompany(self, stock):
        """
        Similar to LeastCorrelatedCompany
        """
        print("Company 1: " + stock.getName() + ", Company 2: " + self.getHighestCorrelatedCompany(stock)[0]) 
        print("Correlation: " + str(self.getHighestCorrelatedCompany(stock)[1]))
    
    def printTask2Summary(self):
        """
        This function wraps up all functions in this module and creates a summary
        of the dataset. 
        """
        #Maybe also include graphics?
        print('')
        
###############################################################################
###                       FUNCTIONS FOR TASK 3                              ###
###############################################################################
    
    def getCorrelationTuples(self):
        """
        Creates tuples of the form (weight, stock1, stock2) for all
        stocks in the stock_list attribute. For our initial input of 496 stocks
        this results in a total of 122760 tuples (more explicitly for a stock
        list of length n a total number of n*(n-1)/2 will be created.
        So please be patient and get yourself a cup of tea in the meantime..
        Input: None
        Output: None
        """
        
        for i in range(len(self.stock_list)):
            for j in range(i+1, len(self.stock_list)):
                cor=self.getCorrelation(self.stock_list[i], self.stock_list[j])
                self.corr_tuples.append((cor, self.stock_list[i], self.stock_list[j]))
        
        self.corr_tuples.sort()

    
    def getKClusters(self, k):
        """
        TO DO
        """
        if k > len(self.stock_list)-1:
            return None
            
        nodePointers = {}
        #Initialize cluster with Nodes pointing at each other
        for i in range(len(self.stock_list)):
            nodePointers[self.stock_list[i]] = self.stock_list[i]
        
        #Setting k new edges between the nodes
        for i in range (k):
            curr_tup = self.corr_tuples[i]
            src = curr_tup[1]
            dest = curr_tup[2]
            
            connected = False
            """
            Loop over the nodes (that src points at) until one of them 
            points at itself (or src points already points at itself than just
            take src). Then connect this one to the destination node of the
            correlation tuple
            """
            while not connected:
                if nodePointers[src]!=src:
                    nodePointers[src] = dest
                    connected = True
                    else:
                        src = nodePointers[src]
        
        #Recover sets from the linked nodes
        sets = []
        #Iterate over all 
        for item in nodePointers:
            if sets == []:
                sets.append({item}) 
            else:
                for i in range (len(sets)):
                    if nodePointers[item] in sets[i]:
                        #Add key to set i DOES NOT WORK LIKE THIS
                        sets[i][item]
                        
        
        
d = {'A', 'B'}
if 7 in d:
    print('y')
d['C':5]
#for item in d:
    #print(d[item])
if 'C' in d:
    print('yes')    




###############################################################################
###                       NOT NEEDED ANYMORE                                ###
###############################################################################

    def getCorrelationGraph(self):
        """
        Creates a graph with the stocks as the nodes and the correlation 
        between them as the edges
        """
        gr = g.Graph()
        
        for i in range(len(self.stock_list)):
            for j in range(i+1, len(self.stock_list)):
                cor = self.getCorrelation(self.stock_list[i], self.stock_list[j])
                gr.addEdge(self.stock_list[i], self.stock_list[j], cor)
        
        return gr
                
      
item = 'hello'
d = {'hello'}
if 'hello' in d:
    print('yes')