import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Parameters
num_orders = 1000
num_customers = 100
num_products = 50

# Generate random data
data = {
    "order_id": [fake.uuid4() for _ in range(num_orders)],
    "customer_id": [random.randint(1, num_customers) for _ in range(num_orders)],
    "order_date": [fake.date_this_decade() for _ in range(num_orders)],
    "product_id": [random.randint(1, num_products) for _ in range(num_orders)],
    "product_name": [fake.word() for _ in range(num_orders)],
    "product_price": [round(random.uniform(10.0, 100.0), 2) for _ in range(num_orders)],
    "quantity": [random.randint(1, 5) for _ in range(num_orders)]
}

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('orders.csv', index=False)

print("orders.csv file generated successfully.")