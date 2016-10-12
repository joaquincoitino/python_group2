# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:05:13 2016

@author: lukaswolff
"""

import unittest
import Stock as st
import Stock_Returns as str

class TestStock_ReturnsMethod(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stock1 = st.Stock('Pear', [2,2,5,3,3,3], 'Technology', 'PPAR')
        cls.stock2 = st.Stock('Banana', [4,7,1,9,3,4], 'Energy', 'BANA')
        cls.stock_list = [cls.stock1, cls.stock2]
    

    def test_getMinimumDailyReturns(self):
        self.assertEqual(str.getMinimumDailyReturns(self.stock_list), -0.857142)

    
    def test_getMaximumDailyReturns(self):
        self.assertEqual(str.getMinimumDailyReturns(self.stock_list), 8)
        

    def test_getCompanyWithLeastVolatility(self):
        self.assertEqual(str.getCompanyWithLeastVolatility(self.stock_list), (self.stock1, 0.658))

    def test_getCompanyWithHighestVolatility(self):
        self.assertEqual(str.getCompanyWithLeastVolatility(self.stock_list), (self.stock2, 3.2991959440977463))



if __name__ == '__main__':
    unittest.main()