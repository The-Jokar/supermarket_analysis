import csv

def load_data(file_name):
    data = []
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Since the CSV files are in the same folder as the script, you can use the file names directly
orders = load_data('orders.csv')
order_products_prior = load_data('order_products__prior.csv')
products = load_data('products.csv')

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
