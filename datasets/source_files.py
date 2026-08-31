import pandas as pd 
from datetime import datetime, timedelta
import random

# --- CRM Source: Customers ---
customers = pd.DataFrame({
    "cust_id": [f"C{i:03d}" for i in range(1, 21)],
    "cust_name": ["Alice Johnson","Bob Smith","Charlie Brown","David Lee","Eve Adams",
                  "Frank Miller","Grace White","Hannah Scott","Ian Wright","Julia Roberts",
                  "Kevin Young","Laura Hall","Mike Turner","Nina Patel","Oscar King",
                  "Priya Singh","Quinn Davis","Rachel Kim","Sam Clark","Tina Brooks"],
    "email": [f"cust{i}@example.com" for i in range(1, 21)],
    "city": ["Chicago","Denver","Austin","Seattle","Miami","Boston","Phoenix","Atlanta",
             "Dallas","Portland","Chicago","Denver","Austin","Seattle","Miami",
             "Boston","Phoenix","Atlanta","Dallas","Portland"],
    "segment": ["SMB","Enterprise","SMB","Enterprise","SMB","SMB","Enterprise","SMB",
                "Enterprise","SMB","SMB","Enterprise","SMB","Enterprise","SMB",
                "SMB","Enterprise","SMB","Enterprise","SMB"]
})
customers.to_csv("/Volumes/retailworks/bronze/source_files/crm_customers.csv", index=False)

# --- ERP Source: Products ---
products = pd.DataFrame({
    "prod_id": [f"P{i:03d}" for i in range(1, 11)],
    "prod_name": ["Laptop","Smartphone","Tablet","Headphones","Monitor",
                  "Keyboard","Mouse","Webcam","Router","Printer"],
    "category": ["Electronics","Electronics","Electronics","Accessories","Accessories",
                 "Accessories","Accessories","Accessories","Electronics","Electronics"],
    "unit_price": [800.00, 500.00, 300.00, 150.00, 250.00, 100.00, 50.00, 70.00, 60.00, 220.00]
})
products.to_csv("/Volumes/retailworks/bronze/source_files/erp_products.csv", index=False)

# --- Orders (transactional source) ---
random.seed(42)
orders = []
start_date = datetime(2026, 7, 1)
for i in range(1, 101):
    orders.append({
        "order_id": f"ORD{i:04d}",
        "cust_id": f"C{random.randint(1,20):03d}",
        "prod_id": f"P{random.randint(1,10):03d}",
        "order_date": (start_date + timedelta(days=random.randint(0, 30))).strftime("%Y-%m-%d"),
        "quantity": random.randint(1, 5)
    })
orders_df = pd.DataFrame(orders)
orders_df.to_csv("/Volumes/retailworks/bronze/source_files/orders.csv", index=False)

print("Sample source files created for CRM, ERP, and Orders")