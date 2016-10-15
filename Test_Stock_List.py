# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 23:05:17 2016

@author: lukaswolff
"""


import unittest
import Stock as st
import Stock_List as stl

class TestStock_List_Methods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stock1 = st.Stock('Pear', [2,2,5,3,3,3], 'Technology', 'PPAR')
        cls.stock2 = st.Stock('Banana', [4,7,1,9,3,4], 'Energy', 'BANA')
        cls.stock_list = stl.Stock_List([cls.stock1, cls.stock2])
    

    def test_getMinimumDailyReturns(self):
        self.assertEqual(self.stock_list.getMinimumDailyReturns(), (self.stock2,-0.8571428571428571))

    
    def test_getMaximumDailyReturns(self):
        self.assertEqual(self.stock_list.getMaximumDailyReturns(), (self.stock2,8))
        

    def test_getCompanyWithLeastVolatility(self):
        self.assertEqual(self.stock_list.getCompanyWithLeastVolatility(), (self.stock1, 0.6584831053261732))

    def test_getCompanyWithHighestVolatility(self):
        self.assertEqual(self.stock_list.getCompanyWithHighestVolatility(), (self.stock2, 3.2991959440977463))

    def test_getCorrelation(self):
        self.assertEqual(round(self.stock_list.getCorrelation(self.stock1, self.stock2),3), -0.566)

if __name__ == '__main__':
    unittest.main()
