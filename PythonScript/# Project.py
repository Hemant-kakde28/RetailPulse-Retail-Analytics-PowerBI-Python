# Project.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

sku = pd.read_csv("sku_master.csv")
store = pd.read_csv("store_master.csv")
sales =pd.read_csv("sales_transactions.csv")
customer = pd.read_csv("customer_master.csv")
inventory = pd.read_csv("inventory_snapshot.csv")
promotions = pd.read_csv("promotions.csv")
flags = pd.read_csv("sku_inventory_flags.csv")

print("---------STEP1--------")
print("SKU",sku.shape)
print("STORE",store.shape)
print("sales",sales.shape)
print("CUSTOMER",customer.shape)
print("INVENTORY",inventory.shape)
print("PROMOTIONS",promotions.shape)
print("FLAGS",flags.shape)
print("---------STEP2----------")
print(sku.head())
print(store.head())
print(sales.head())
print(customer.head())
print(inventory.head())
print(promotions.head())
print(flags.head())
print("---------STEP3-----------")
print(sku.tail())
print(store.tail())
print(sales.tail())
print(customer.tail())
print(inventory.tail())
print(promotions.tail())
print(flags.tail())
print("--------------STEP4----------")
print(sku.info())
print(store.info())
print(sales.info())
print(customer.info())
print(inventory.info())
print(promotions.info())
print(flags.info())
print("-------------STEP5----------")
print(sku.describe())
print(store.describe())
print(sales.describe())
print(customer.describe())
print(inventory.describe())
print(promotions.describe())
print(flags.describe())
print("----------STEP6-----------")
print(sku.isnull().sum())
print(store.isnull().sum())
print(store.isnull().sum())
print(customer.isnull().sum())
print(inventory.isnull().sum())
print(promotions.isnull().sum())
print(flags.isnull().sum())
print("-----------STEP7-----------")
print(sku.duplicated().sum())
print(store.duplicated().sum())
print(sales.duplicated().sum())
print(customer.duplicated().sum())
print(inventory.duplicated().sum())
print(promotions.duplicated().sum())
print(flags.duplicated().sum())
print("---------STEP8------------")
store["Opening_Date"] =pd.to_datetime(store["opening_date"])
customer["Registration_date "] =pd.to_datetime(customer["registration_date"])
inventory["Last_Restock_Date"]=pd.to_datetime(inventory["last_restock_date"])
promotions["Start_Date"] =pd.to_datetime(promotions["start_date"])
promotions["End_Date"] =pd.to_datetime(promotions["end_date"])
sales["date"] = pd.to_datetime(sales["date"])
a=sales["store_id"].isin(store["store_id"]).mean()
print(a)
b=sales["sku_id"].isin(sku["sku_id"]).mean()
print(b)
c=sales["customer_id"].isin(customer["cust_id"]).mean()
print(c)

print("---------STEP10---------")
print(sales["quantity"].describe())
print(sales[sales ["quantity"]<=0])
print(sales[sales["unit_price"]<=0])
print("*"*50)
print((sales["discount_pct"] <= 0).sum())
print(sales["discount_pct"].isnull().sum())
print("Zero discount:", (sales["discount_pct"] == 0).sum())
print("Positive discount:", (sales["discount_pct"] > 0).sum())
print(sales[sales["discount_pct"] > 100])

sales["gross_sales"] = (sales["quantity"] * sales["unit_price"])
print(sales["gross_sales"])
sales["discount_amount"] = (sales["gross_sales"] *sales["discount_pct"]     
                            / 100)
print(sales["discount_amount"])
sales["date"] = pd.to_datetime(sales["date"])
print(sales["date"])
print(sales["date"].dtype)
print("----------STEP10-------")
sales = sales.merge(
    sku[["sku_id", "cost_price", "category", "subcategory", "brand"]],
    on="sku_id",
    how="left"
)
sales["total_cost"] = (sales["quantity"] * sales["cost_price"])
sales["gross_profit"] = (sales["total_value"] - sales["total_cost"])
sales["profit_margin %"]=np.where(sales["total_value"]!=0,  
                         sales["gross_profit"]/sales["total_value"]*100,0)
print("----------STEP11--------")
bins = [17, 25, 35, 45, 55, 65, 100]
labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65",
    "66+"
]
customer["age_group"] = pd.cut(
    customer["age"],
    bins=bins,
    labels=labels
)
inventory["reorder_required"] = np.where(
    inventory["stock_on_hand"] <= inventory["reorder_point"],
    "Yes",
    "No"
)
inventory["below_safety_stock"] = np.where(
    inventory["stock_on_hand"] <= inventory["safety_stock"],
    "Yes",
    "No"
)
inventory["stock_status"] = np.select(
    [
        inventory["stock_on_hand"] == 0,
        inventory["stock_on_hand"] <= inventory["safety_stock"],
        inventory["stock_on_hand"] <= inventory["reorder_point"]
    ],
    [
        "Out of Stock",
        "Below Safety Stock",
        "Reorder Required"
    ],
    default="Healthy"
)

Total_Revenue=sales["total_value"].sum()
print("Total_Revenue",Total_Revenue)
Total_Unit=sales["quantity"].sum()
print("Total_Unit",Total_Unit)
Total_Order=sales["receipt_id"].nunique()
print("Total_Order",Total_Order)
Total_Customer=sales["customer_id"].nunique()
print("Total_Customer",Total_Customer)
Average_order_value= (sales["total_value"].sum()/sales["receipt_id"].nunique())
print("Average_order_value",Average_order_value)
Total_Profit=sales["gross_profit"].sum()
print("Total_Profit",Total_Profit)
Profit_Margin= sales["gross_profit"].sum()/sales["total_value"].sum()*100
print("Profit_Margin",Profit_Margin)

sales.to_csv(
    r"D:\Downloads\SyntheticRetail\retail_clean_dataset\sales_cleaned_for_powerbi.csv",
    index=False
)

print("Cleaned_File")
