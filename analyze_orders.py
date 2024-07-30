import pandas as pd

def read_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None

def compute_monthly_revenue(df):
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['month'] = df['order_date'].dt.to_period('M')
    monthly_revenue = df.groupby('month').apply(lambda x: (x['product_price'] * x['quantity']).sum()).reset_index(name='total_revenue')
    return monthly_revenue

def compute_product_revenue(df):
    product_revenue = df.groupby('product_name').apply(lambda x: (x['product_price'] * x['quantity']).sum()).reset_index(name='total_revenue')
    return product_revenue

def compute_customer_revenue(df):
    customer_revenue = df.groupby('customer_id').apply(lambda x: (x['product_price'] * x['quantity']).sum()).reset_index(name='total_revenue')
    return customer_revenue

def top_customers_by_revenue(df, top_n=10):
    customer_revenue = compute_customer_revenue(df)
    top_customers = customer_revenue.sort_values(by='total_revenue', ascending=False).head(top_n)
    return top_customers

def main():
    file_path = 'orders.csv'
    df = read_data(file_path)

    if df is not None:
        monthly_revenue = compute_monthly_revenue(df)
        print("Monthly Revenue:\n", monthly_revenue)

        product_revenue = compute_product_revenue(df)
        print("Product Revenue:\n", product_revenue)

        customer_revenue = compute_customer_revenue(df)
        print("Customer Revenue:\n", customer_revenue)

        top_customers = top_customers_by_revenue(df)
        print("Top Customers by Revenue:\n", top_customers)

if __name__ == "__main__":
    main()
