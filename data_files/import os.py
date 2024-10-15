import os
import csv

def load_data(file_name):
    data = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Print the current directory for debugging
current_dir = os.path.dirname(__file__)
print(f"Current directory: {current_dir}")

# List files in the current directory for debugging
print("Files in the current directory:")
for file in os.listdir(current_dir):
    print(file)

# Construct full paths for the CSV files
orders_path = os.path.join(current_dir, 'orders.csv')
order_products_prior_path = os.path.join(current_dir, 'order_products__prior.csv')
products_path = os.path.join(current_dir, 'products.csv')

# Print the full paths for debugging
print(f"Orders file path: {orders_path}")
print(f"Order Products Prior file path: {order_products_prior_path}")
print(f"Products file path: {products_path}")

# Load the data
orders = load_data(orders_path)
order_products_prior = load_data(order_products_prior_path)
products = load_data(products_path)

# Create a dictionary for products to quickly look up product names by product_id
product_dict = {product['product_id']: product['product_name'] for product in products}

# Create a dictionary to store transactions by order_id
transactions = {}

# Merge orders and products manually
for row in order_products_prior:
    order_id = row['order_id']
    product_id = row['product_id']
    
    # Get product name from the product_dict
    product_name = product_dict.get(product_id, 'Unknown')
    
    # Add the product to the corresponding order in the transactions dictionary
    if order_id not in transactions:
        transactions[order_id] = []
    transactions[order_id].append(product_name)

# Check a few transactions
for i, (order_id, products) in enumerate(transactions.items()):
    if i >= 5:  # Only print first 5 transactions
        break
    print(f"Order ID: {order_id}, Products: {products}")