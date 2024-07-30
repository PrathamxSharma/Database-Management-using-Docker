import unittest
import pandas as pd
from analyze_orders import read_data, compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, top_customers_by_revenue

class TestAnalyzeOrders(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.df = read_data('orders.csv')
    
    def test_read_data(self):
        self.assertIsInstance(self.df, pd.DataFrame)
    
    def test_compute_monthly_revenue(self):
        result = compute_monthly_revenue(self.df)
        self.assertIsInstance(result, pd.DataFrame)
    
    def test_compute_product_revenue(self):
        result = compute_product_revenue(self.df)
        self.assertIsInstance(result, pd.DataFrame)
    
    def test_compute_customer_revenue(self):
        result = compute_customer_revenue(self.df)
        self.assertIsInstance(result, pd.DataFrame)
    
    def test_top_customers_by_revenue(self):
        result = top_customers_by_revenue(self.df)
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()
