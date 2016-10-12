# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 18:24:31 2016

@author: lukaswolff
"""
import unittest
import Stock as st
import Correlations as c


class TestCorrelationsMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.stock1 = st.Stock('Pear', [2,2,5,3,3,3], 'Technology', 'PPAR')
        cls.stock2 = st.Stock('Banana', [4,6,4,6,4,6], 'Energy', 'BANA')
    
    def test_getCorrelation(self):
        self.assertEqual(round(c.getCorrelation(self.stock1, self.stock2),3), -0.657)
        

if __name__ == '__main__':
    unittest.main()